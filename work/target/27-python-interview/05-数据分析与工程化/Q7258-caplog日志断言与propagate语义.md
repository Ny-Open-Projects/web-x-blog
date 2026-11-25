---
title: "[Q7258] 本地过 CI 挂的日志断言：caplog 的 propagate 与 handler 注入语义"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7258 · 本地过 CI 挂的日志断言：caplog 的 propagate 与 handler 注入语义

难度：P6 ｜ 标签：pytest、caplog、logging、propagate、测试隔离

基线：Python 3.12 + logging；实测 propagate=False 的 logger 不进 caplog 的机制与三种修复，全标准库实跑。

**问**：测试要断言"业务代码打了 WARNING 日志"。用 pytest 的 caplog 断言，本地全过、CI 稳定失败——因为业务模块自己配了 `propagate = False` 的 logger。caplog 到底怎么收日志？为什么 propagate=False 就收不到？断言日志的正确姿势是什么？

**答**：
- **结论**：logging 的传播模型：logger 记录一条日志后，**先交给自己的 handler，再传给祖先 logger 的 handler（propagate=True 时）**。caplog 的实现是在 **root logger 上临时挂一个捕获 handler**——所以日志要到达 caplog，必须能沿传播链走到 root。业务模块 `logger.propagate = False`（生产里常见：自己挂 handler 输出到文件，避免重复打印）后，日志到不了 root，caplog 收空，断言失败。修复三选：① 测试里对目标 logger 临时挂自己的捕获 handler（最直接，与 propagate 无关）；② `caplog.set_level(logging.WARNING, logger="business")` 配合恢复 propagate（临时改回来，用例结束还原）；③ 更根本的：**断言行为而不是日志文本**——日志是给人看的副作用，能断言返回值/状态变化就别断言日志。测试与生产日志配置的耦合（dictConfig 覆盖已建 logger，Q7240）是这一族问题的另一面。
- **取舍**：① 日志断言的价值边界：值得断言的是"异常路径确实留了可观测痕迹"（告警日志、审计日志），常规路径的日志文本断言又脆又没用；② handler 注入的清理纪律：挂了 handler 用例结束必须摘除，否则泄漏到后续用例（Q7221 yield fixture teardown 纪律同源）；③ set_level 的双重语义：既设捕获级别又改 logger 级别——它恢复的只是级别，propagate 需要自己管；④ 断言粒度：用 `caplog.records` 检查 level/loggerName/getMessage，比整段文本 contains 稳。
- **实战**：① 测试基建提供 `log_capture("business")` 夹具：挂 handler + 自动清理，用例即插即用；② propagate=False 的模块进库时写清测试契约（怎么断言它的日志）；③ 级别相关的测试用 `caplog.at_level()` 上下文管理器，离开自动还原；④ 日志断言数量控制：一个用例最多断言"发生了该级别的日志"，别逐字段断言格式（那是日志格式化器的单测）。

```python
"""caplog 语义实测：propagate 模型与三种修复路径。"""
import logging

# 业务模块: 自己挂 handler + propagate=False (生产常见配置)
biz = logging.getLogger("business")
biz.setLevel(logging.WARNING)
biz.propagate = False


class ListHandler(logging.Handler):
    def __init__(self) -> None:
        super().__init__()
        self.records: list[logging.LogRecord] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.records.append(record)


def biz_fails() -> None:
    biz.warning("订单同步失败 order=123")


if __name__ == "__main__":
    # 场景1: root 捕获 handler (caplog 的工作原理)
    root_capture = ListHandler()
    root = logging.getLogger()
    root.addHandler(root_capture)
    biz_fails()
    got_caplog = root_capture.records
    print(f"场景1 propagate=False: root 捕获到 {len(got_caplog)} 条 -> "
          f"caplog 断言失败 (这就是'本地过 CI 挂'的机理)")
    root.removeHandler(root_capture)

    # 场景2 修复: 临时恢复 propagate -> 日志沿链到 root
    root_capture = ListHandler()
    root.addHandler(root_capture)
    biz.propagate = True
    biz_fails()
    print(f"场景2 恢复 propagate: root 捕获到 {len(root_capture.records)} 条 -> "
          f"{root_capture.records[0].getMessage()!r}")
    biz.propagate = False                  # 测试后还原!
    root.removeHandler(root_capture)

    # 场景3 修复: 直接对目标 logger 挂捕获 handler (与 propagate 无关)
    own = ListHandler()
    biz.addHandler(own)
    biz_fails()
    recs = [(r.levelname, r.getMessage()) for r in own.records]
    print(f"场景3 目标 logger 挂 handler: 捕获 {recs} -> 与 propagate 配置无关")
    biz.removeHandler(own)                 # 清理纪律: 用例结束摘除

    # 场景4: 不清理的泄漏后果
    leak = ListHandler()
    biz.addHandler(leak)
    other_cap = ListHandler()
    root.addHandler(other_cap)
    biz.propagate = True
    biz_fails()
    print(f"场景4 漏摘 handler: 目标 handler {len(leak.records)} 条 + "
          f"root {len(other_cap.records)} 条 -> 日志重复入两条链, 影响后续断言")
    biz.removeHandler(leak)
    root.removeHandler(other_cap)
    biz.propagate = False

    ok = not got_caplog and recs
    print(f"\n校验: 机理复现 + 两种修复可用 -> {'通过' if ok else '异常'}")
    print("\n结论：caplog 收的是'走到 root 的日志'; propagate=False 挡在链上;")
    print("      修复=目标 logger 挂 handler(需清理) 或临时恢复 propagate;")
    print("      能断言行为就别断言日志文本")
```

**追问一**：为什么"断言日志"经常是坏味道？

→ 解析：日志文本是**给人读的实现细节**：改措辞、改格式、改级别都会让断言翻红，而业务行为没变——这是把断言耦合在无关变更上。caplog 适合的场景收敛为三类：① 副作用本身没有返回值（fire-and-forget 的告警发送），日志是唯一可观测证据；② 断言"级别"而非内容（出了 WARNING 级事件本身是契约）；③ 审计日志的必达性（合规要求关键动作必须留痕，断言存在性）。之外的情况优先断言行为：注入一个 mock 的告警接口断言它被调用，比断言"打了日志"既稳又表达真实意图（Q1080 mocker 边界）。日志格式本身的测试独立做一次，别散在各业务用例里。

**追问二**：测试里改 propagate/set_level，用例结束后怎么保证还原？

→ 解析：两条纪律。一是**夹具化的 try/finally**：把"改配置 + 注入 handler + 执行 + 还原"封装成 yield fixture（pytest 的 fixture teardown 在断言失败后仍执行），禁止用例体里裸改 logging 配置——裸改 + 用例中途异常 = 配置泄漏到整个测试会话，后面的用例在错误级别/传播状态下跑，产生莫名 flaky。二是**会话级自检**：conftest 里加一个自动 fixture，在每个用例结束对比 logging 树的 handler 数量与 propagate 状态，发现泄漏直接让该用例报错（fail fast），把泄漏消灭在引入时而不是排查时。这与 Q7240 dictConfig 事故同根：**logging 全局状态是共享资源，测试必须显式借用显式归还**。
