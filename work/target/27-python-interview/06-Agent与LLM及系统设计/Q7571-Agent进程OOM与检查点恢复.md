---
title: "[Q7571] Agent 长任务进程 OOM 与检查点恢复复盘"
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7571 · Agent 长任务进程 OOM 与检查点恢复复盘

难度：P6 ｜ 标签：Agent / OOM / 检查点 / 事故复盘

**问**：一个跑数小时的 Agent 任务（多步工具调用 + 大量工具结果驻留内存）被 OOM kill，会话状态全丢，用户从头再跑一遍还要再付一遍 token 钱。复盘：状态为什么会全丢？怎么设计检查点让长任务可续跑？

**答**：

**结论**：根因是把 Agent 会话状态（消息历史、工具结果、中间变量）只放在进程内存里，且不加节制地累积——每个工具结果（可能是几 MB 的文档/截图）都 append 进列表，几小时后进程 RSS 超限被 OOM killer 干掉。恢复设计三层：① 检查点持久化：每完成一步（或每 N 步）把会话快照（消息列表 + 工具状态 + 版本号）写入外部存储（DB/对象存储），崩溃后从最近快照 + 待办队列恢复；② 内存节流：工具结果落盘引用（内存里只存 ID + 摘要），消息历史按窗口/摘要压缩；③ 幂等续跑：工具调用带幂等键，恢复时已完成的工具调用不再重执行——否则续跑会重复付钱、重复副作用。

**取舍**：检查点频率的两难：每步 checkpoint 存储写入多、延迟增加（外部存储写 50-200ms/步）；稀疏 checkpoint 崩溃后重跑的步数多、token 重付多。按"步的代价"定频率：贵的步（每次几万 token）每步 checkpoint，便宜的步每 5-10 步一次。另一个取舍：摘要压缩省内存/token 但丢细节，评估类任务（要精确引用）不能摘要，只能外部存储 + 按需检索。

**实战**：生产实现要点：快照 schema 带版本号（Agent 框架升级后旧快照可迁移或显式作废）；恢复入口与正常入口共用同一套工具执行器；监控 RSS 水位 + 步数上限双熔断（到上限优雅 checkpoint 后结束，而不是等 OOM）。Python 演示一个可续跑的执行器骨架：状态外置、工具幂等、崩溃注入后恢复。

```python
# 可检查点续跑的 Agent 执行器骨架（仅标准库，Python 3.9+）
from __future__ import annotations

import json


class CheckpointedAgent:
    def __init__(self, store: dict) -> None:
        self.store = store  # 模拟外部存储（生产用 DB/对象存储）

    def snapshot(self, run_id: str, state: dict) -> None:
        self.store[run_id] = json.dumps(
            {**state, "v": 1}, ensure_ascii=False)

    def restore(self, run_id: str) -> dict | None:
        raw = self.store.get(run_id)
        return json.loads(raw) if raw else None


def run_tool(state: dict, step: str, executed: set) -> float:
    """幂等工具：同 key 不重执行，返回本步 token 成本。"""
    key = f"{state['run_id']}:{step}"
    if key in executed:
        return 0.0
    executed.add(key)
    state["history"].append({"step": step, "summary": f"done:{step}",
                             "blob_ref": f"s3://blobs/{key}"})  # 大结果只留引用
    return 5000.0  # 每步 5k token


def main() -> None:
    store: dict = {}
    agent = CheckpointedAgent(store)
    executed: set = set()
    steps = ["plan", "search", "extract", "report"]

    # 第一段执行：跑到第 2 步进程被 OOM kill
    state = {"run_id": "r1", "history": [], "next": 0}
    for i, s in enumerate(steps[:2]):
        run_tool(state, s, executed)
        state["next"] = i + 1
        agent.snapshot("r1", state)
    assert state["next"] == 2

    # 崩溃后：从快照恢复，已执行的步不重跑
    restored = agent.restore("r1")
    assert restored["next"] == 2
    for i in range(restored["next"], len(steps)):
        s = steps[i]
        cost = run_tool(restored, s, executed)
        assert cost == 5000.0  # 新步才花钱
        restored["next"] = i + 1
        agent.snapshot("r1", restored)
    assert restored["next"] == 4
    assert len(restored["history"]) == 4  # 无重复步
    print("结论：外置快照 + 工具幂等 → OOM 后续跑，零重复副作用零重复计费")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么恢复时"已完成的工具调用不重执行"这么重要，光靠 checkpoint 记 next 指针不够吗？——崩溃可能发生在"工具已产生外部副作用（已写库/已发邮件）但 checkpoint 未落"的窗口；只有工具侧幂等键才能消灭重复副作用，指针只解决执行流位置。两套机制缺一不可。
- 追问 1.1：快照 schema 版本号解决什么问题？——Agent 框架升级（消息格式、工具协议变化）后旧快照无法直接恢复；带版本号可以在恢复时迁移升级或明确作废并通知用户重跑，避免恢复出语义错乱的状态。
- 追问 2：RSS 熔断和步数熔断为什么都要有？——OOM killer 是粗暴的最后一道墙，被杀时状态丢失；RSS 水位熔断（如 80%）触发主动 checkpoint + 压缩 + 继续或优雅结束；步数熔断兜"逻辑死循环"（步数涨但内存不涨的循环）——两种失控模式不同，监控一个会漏另一个。

**背诵要点**：

1. 会话状态只放内存 + 工具结果无节制累积 = OOM 必然；大结果落盘存引用，内存只留 ID+摘要。
2. 检查点三层：外部快照（带 schema 版本号）+ 工具幂等键（防重复副作用/计费）+ 双熔断（RSS 水位 + 步数上限）。
3. checkpoint 频率按步代价定：贵步每步一存，便宜步 5-10 步一存；崩溃恢复零重复执行是验收标准。

**复盘追问**：

1. 如果被 OOM 的任务已经产生了外部副作用且没有幂等键，你如何事后对账与修复？
2. 检查点存储本身的成本怎么进账（快照大小 × 频率 × 保留期）？
