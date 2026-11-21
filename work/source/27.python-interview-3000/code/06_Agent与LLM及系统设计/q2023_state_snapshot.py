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
