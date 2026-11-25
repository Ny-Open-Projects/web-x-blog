---
title: [Q7638] MCP server 崩溃导致工具全不可用的事故复盘
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7638 · MCP server 崩溃导致工具全不可用的事故复盘

难度：P6 ｜ 标签：事故复盘 / MCP / 工具治理

**问**：Agent 依赖的某个 MCP server（stdio 子进程形态）在一次崩溃后自动重启，但重启期间所有会话的工具调用全部失败，且恢复后部分会话的连接句柄仍指向死进程，持续报错。为什么一个 server 的崩溃会放大成全局故障？崩溃恢复的正确设计是什么？

**答**：
- **结论**：放大机制三层：① **stdio 形态的会话绑定**：stdio MCP server 是随会话/客户端启动的子进程，一个 server 进程崩溃 = 所有持有该 server 的会话同时失去整组工具（不是单个工具，是整组——工具注册与进程生命周期绑定，Q7611 的并发容量问题在这里变成可用性问题）；② **无健康探测的盲用**：客户端在 server 死后仍按缓存的 tool list 发调用，错误集中爆发且重试打到死句柄上；③ **重启后状态丢失**：server 侧的会话状态（初始化协商、资源订阅）不持久化，重启后旧会话 ID 全部失效，客户端若不做 re-initialize 就一直失败。正确设计：客户端侧维护 server 进程管理器（supervisor 模式：崩溃检测 → 指数退避重启 → re-initialize → 工具列表刷新），调用层加熔断（连续失败 N 次把该 server 标记为 down，拒绝快速失败而不是挂着超时），并在 Agent 提示词/工具路由层支持**降级**：该 server 不可用时告知模型"工具暂时不可用，走兜底路径"，而不是让模型对着报错无限重试。
- **取舍**：stdio（每会话独立子进程，隔离好但重启即丢会话、句柄管理重）vs 远程 server（SSE/HTTP，独立进程可多会话共享、可加 LB 与健康检查，但引入网络层）。事故后的常见整改是把关键 MCP server 从 stdio 迁到远程形态——代价是多一跳延迟与部署运维。熔断阈值低（快速降级）会牺牲短暂抖动场景的可用性，高则拖长故障时间；按"server 历史稳定性"分级配置。
- **实战**：① 子进程管理用 asyncio 监控 + 退避重启（1s/2s/5s 上限），重启后强制 re-initialize 并重新 list_tools；② 工具调用错误分类：进程死/超时/业务错分别计数，只有"进程死"触发熔断降级；③ Agent 层在工具结果里注入明确的"降级说明"，让模型切换路径而不是反复重试；④ 演练：kill -9 server 进程，验证恢复时长与期间调用表现。

```python
# MCP server 崩溃恢复: supervisor 重启 + 熔断 + 会话 re-initialize
# 基线: Python 3.9+ 标准库 (生产用 mcp SDK / asyncio 子进程管理)
from dataclasses import dataclass, field


@dataclass
class McpServer:
    name: str
    alive: bool = False
    restart_count: int = 0
    fail_streak: int = 0
    initialized_sessions: set[str] = field(default_factory=set)

    def crash(self) -> None:
        self.alive = False
        self.initialized_sessions.clear()   # 会话状态不持久 -> 全失效


class Supervisor:
    """崩溃检测 -> 指数退避重启 -> re-initialize -> 刷新工具列表。"""
    BACKOFF = [1, 2, 5, 5]      # 秒

    def __init__(self, server: McpServer) -> None:
        self.s = server

    def restart(self) -> bool:
        if self.s.restart_count >= len(self.BACKOFF):
            return False                      # 超限: 上报人工
        self.s.alive = True
        self.s.fail_streak = 0
        self.s.restart_count += 1
        return True

    def call(self, session: str, ok: bool) -> str:
        if not self.s.alive:
            return "circuit-open: server down, 走降级路径"
        if not ok:
            self.s.fail_streak += 1
            if self.s.fail_streak >= 3:
                self.s.crash()
                return "circuit-open: 连续失败熔断"
            return "error: 交给重试"
        return "ok"


def main() -> None:
    s = McpServer("tools-server")
    sup = Supervisor(s)
    s.alive = True
    s.initialized_sessions = {"s1", "s2"}
    s.crash()
    assert not s.initialized_sessions          # 证据: 会话绑定进程, 崩溃全失效
    assert sup.call("s1", True) == "circuit-open: server down, 走降级路径"
    assert sup.restart()
    assert sup.call("s1", True) == "ok"
    # 熔断: 连续 3 次失败 -> 第 3 次触发 crash + 熔断返回
    results = [sup.call("s1", False) for _ in range(3)]
    assert not s.alive and "熔断" in results[-1]
    assert sup.call("s1", False).startswith("circuit-open")  # 后续快速失败
    assert sup.restart()
    print("OK: supervisor 退避重启 + re-init + 3 连败熔断降级; 会话状态需重建")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么工具调用失败要区分"进程死"和"业务错"，只有前者熔断？
→ 一句话提示：业务错（参数错/权限错）重试无害且是模型自愈循环的一部分（Q7524）；进程死是基础设施故障，重试只会放大积压——语义不同的错误用不同恢复策略。

**追问 2**：stdio 迁移到远程 MCP server 后，还剩哪些单点？
→ 一句话提示：server 自身仍是单点，需要健康检查 + 多副本 + 客户端连接池；且网络层引入新故障面（TLS/代理/超时），stdio 的"进程死=立即知道"变成"网络分区=慢失败"，故障语义反而更复杂。

## 背诵要点
- stdio MCP server 与会话生命周期绑定：一个进程崩溃 = 所有会话失去整组工具 + 会话状态全失效（需 re-initialize + list_tools 刷新）。
- 恢复设计：supervisor 指数退避重启（1/2/5s）+ 3 连败熔断降级 + Agent 层注入"工具不可用走兜底"提示，模型不无限重试。
- stdio（隔离好、重启丢会话）vs 远程（可共享多副本、多一跳网络故障面）；错误分类：进程死熔断、业务错进自愈循环。

## 复盘追问
- 演练脚本应该验证哪些指标？提示：kill -9 后恢复时长、恢复期间调用是快速失败还是挂超时、恢复后旧会话是否成功 re-init、工具列表是否刷新。
- 熔断期间模型收到什么才能避免死循环重试？提示：结构化的"工具不可用 + 建议替代路径"返回值，而不是裸异常字符串——模型对"明确降级指令"的服从远高于对报错的猜测。
