---
title: [Q2023] Agent 状态快照与回滚:深拷贝检查点
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2023 · Agent 状态快照与回滚:深拷贝检查点

> 难度:★★★☆ | 标签:Agent, 快照, 回滚

**问**:Agent 走了五步发现方向错了,怎么让它干净地回到第二步重来?

**答**:在关键节点前存状态快照,回滚就是把状态整体恢复到那个快照。实现要点是深拷贝:messages、scratch 这类嵌套结构必须与活状态彻底断开引用,否则后续修改会污染快照,回滚回来的还是脏数据。回滚后可以反复试错,快照本身不受再次修改影响;标签不存在时显式报错,而不是静默留在当前状态。这个机制是 HITL 审批、危险操作回退、失败重放的地基——先有能回到过去,才谈重试策略。

```python
# file: code/06_Agent与LLM及系统设计/q2023_state_snapshot.py
"""Agent 状态快照与回滚:deepcopy 检查点与活状态断开引用,试错后一键回滚。"""
import copy


class AgentState:
    def __init__(self):
        self.messages = []
        self.scratch = {}
        self.step = 0

    def apply(self, role, content, patch=None):
        self.messages.append({"role": role, "content": content})
        if patch:
            self.scratch.update(patch)
        self.step += 1


class SnapshotManager:
    def __init__(self):
        self.snapshots = {}

    def save(self, state, label):
        """存快照:必须深拷贝,否则后续 mutate 会污染快照。"""
        self.snapshots[label] = copy.deepcopy(vars(state))

    def rollback(self, state, label):
        if label not in self.snapshots:
            raise KeyError("快照 %s 不存在" % label)
        restored = copy.deepcopy(self.snapshots[label])
        state.__dict__.update(restored)
        return state


if __name__ == "__main__":
    state = AgentState()
    mgr = SnapshotManager()

    state.apply("user", "查订单 A100")
    state.apply("assistant", "调用 query_order", patch={"order": "A100"})
    mgr.save(state, "before_risky")
    saved_step = state.step
    saved_msgs = len(state.messages)

    # 试错:又走了三步,还改了嵌套结构
    state.apply("assistant", "危险操作:删除全部数据", patch={"danger": True})
    state.apply("user", "完了")
    state.scratch["order"] = "被改坏了"
    assert state.step == saved_step + 2 and state.scratch["danger"] is True

    mgr.rollback(state, "before_risky")
    assert state.step == saved_step and len(state.messages) == saved_msgs
    assert state.scratch["order"] == "A100" and "danger" not in state.scratch

    # 快照独立性:回滚后再乱改,原快照不受影响,可反复回滚
    state.scratch["order"] = "又改坏了"
    mgr.rollback(state, "before_risky")
    assert state.scratch["order"] == "A100"

    try:
        mgr.rollback(state, "no_such")
        raise AssertionError("不存在标签必须报错")
    except KeyError:
        pass
    print("快照回滚通过:深拷贝隔离嵌套修改,可重复回滚,未知标签显式报错")
```

**追问**:
- 状态里挂着文件句柄或网络连接怎么办? 答:快照只存可序列化的逻辑状态,资源句柄放进登记簿,回滚时由资源管理器统一释放重建
- 每步都深拷贝太贵怎么办? 答:升级为增量检查点,只存相对上一点的 delta,配哈希链防篡改
