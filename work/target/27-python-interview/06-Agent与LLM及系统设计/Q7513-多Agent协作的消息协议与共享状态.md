---
title: [Q7513] 多 Agent 协作：消息协议与共享状态边界
date: 2026-11-19
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7513 · 多 Agent 协作的消息协议

> 难度:★★★ | 标签:多 Agent, 消息协议, 编排

**问**：规划者/执行者/审查者三 Agent 协作——消息 schema 要哪些字段（trace_id/血缘/预算）？共享状态（黑板）和消息传递怎么选，「下游 Agent 幻觉了上游的输出」怎么防（输出验证 + 血缘追溯）？循环依赖（A 等 B、B 等 A）怎么破？

**答**：① 消息 schema 五必填：`trace_id`（贯穿全链路日志）、`sender/recipient`（路由与审计）、`task_ref`（血缘：引用哪条任务/消息产生的）、`budget_snapshot`（剩余预算随消息传递——Q7511 的预算在协作里要分层）、`payload_schema_version`（Agent 升级后新旧消息兼容）。② 黑板（共享状态）vs 消息传递：黑板（共享 KV+版本）适合「多 Agent 读同一上下文」（协作编辑），强一致要求低、简单；消息传递适合「职责清晰流转」（流水线）——混用原则：**状态放黑板、决策走消息**，共享状态必须带版本号防「Agent A 读到改了一半的状态」。③ 幻觉防御：上游输出进黑板前过**结构验证**（schema 校验 + 关键事实抽查：引用的文件/数据是否存在——执行者声称「已写入 500 行」，审查者调接口核实），血缘让「这个结论哪来的」可追溯，LLM 编造的输出通常血缘断链。④ 死锁：A 等 B 的输出、B 又等 A——编排层用 DAG 表达依赖（无环校验在构图时做）或超时+重试+优先级继承；绝不允许 Agent 自由互发请求（无全局视图必死锁）。

```python
# 全部标准库；demo 实现 DAG 编排校验 + 带血缘黑板 + 输出验证
import json, time, hashlib
from collections import defaultdict

def validate_dag(tasks: dict[str, list[str]]) -> list[str]:
    """编排层构图校验：环检测（Kahn 算法）。"""
    indeg = {t: 0 for t in tasks}
    for t, deps in tasks.items():
        for d in deps:
            indeg[t] += 1
    ready = [t for t, d in indeg.items() if d == 0]
    seen = 0
    while ready:
        t = ready.pop()
        seen += 1
        for other, deps in tasks.items():
            if t in deps:
                indeg[other] -= 1
                if indeg[other] == 0:
                    ready.append(other)
    return [t for t, d in indeg.items() if d > 0]   # 非空 = 有环（死锁风险任务清单）

class Blackboard:
    """黑板 + 版本 + 血缘：状态放黑板，写前验证。"""
    def __init__(self):
        self.state: dict[str, dict] = {}
        self.lineage: dict[str, list[str]] = defaultdict(list)   # key -> 产生它的消息链
    def write(self, key: str, value, task_ref: str, expect_version: int | None = None):
        cur = self.state.get(key)
        if cur and expect_version != cur["version"]:
            raise ValueError(f"版本冲突 {key}: 期望 {expect_version} 实际 {cur['version']}")
        version = (cur["version"] + 1) if cur else 1
        self.state[key] = {"version": version, "value": value, "task_ref": task_ref}
        self.lineage[key].append(task_ref)
    def read(self, key: str):
        return self.state[key]

def verify_output(blackboard: Blackboard, key: str, checker) -> bool:
    """下游消费前验证上游输出（防幻觉：声称写入 500 行要能核实）。"""
    return checker(blackboard.read(key)["value"])

if __name__ == "__main__":
    # 环检测：plan→execute→review→plan 是死锁设计
    bad = {"plan": ["review"], "execute": ["plan"], "review": ["execute"]}
    print("DAG 校验发现环:", validate_dag(bad))
    bb = Blackboard()
    bb.write("rows_written", 500, task_ref="msg-1")
    # 幻觉防御：审查者核实「声称 500 行」是否真实
    fake_db = {"actual_rows": 0}                        # 模拟 DB 实际 0 行
    honest = verify_output(bb, "rows_written", lambda v: v == fake_db["actual_rows"])
    print("输出核实（声称 500 vs 实际 0）:", "幻觉拦截 ✅" if not honest else "一致")
    try:
        bb.write("rows_written", 600, task_ref="msg-2", expect_version=99)
    except ValueError as e:
        print("版本冲突拦截:", e)
    print("血缘:", dict(bb.lineage))
```

**追问**：1) 为什么预算要随消息传递而不是全局查询？——分布式协作里「全局剩余」要加锁查询（竞争热点），随消息传递是快照语义（各 Agent 按收到的快照决策，编排层仲裁冲突）——低延迟且可审计（Q7519 联动）。2) 黑板版本冲突的处理策略？——乐观锁语义：写入带 expect_version 失败则重读重算（Agent 层面 = 重新规划该子任务）；写冲突率高说明任务拆分边界有问题（两个 Agent 写同一 key = 职责重叠）。3) Agent 输出的 schema 校验怎么落地？——每类消息定义 JSON Schema / Pydantic 模型，收到即验，不合格直接打回（附错误信息让上游重试）——宽松解析是幻觉扩散的温床。

## 背诵要点
1. 消息五必填：trace_id、sender/recipient、task_ref（血缘）、budget_snapshot、schema_version。
2. 分工：状态放黑板（带版本乐观锁）、决策走消息；「声称的结果」消费前必须核实（血缘+接口验证防幻觉）。
3. 协作依赖用 DAG 表达并在构图时环检测——Agent 自由互发请求必然死锁。

## 复盘追问
1. 三个 Agent 都改同一文档（协作编辑），黑板模式怎么防相互覆盖？（提示：分段写（各自 key）或文档级乐观锁+合并策略；写冲突率高=任务拆分问题）
2. 血缘链在消息队列场景怎么持久？（提示：消息体带 task_ref 链（trace_id + parent_msg_id），消费侧写库时落血缘表，追溯 API 反查）
