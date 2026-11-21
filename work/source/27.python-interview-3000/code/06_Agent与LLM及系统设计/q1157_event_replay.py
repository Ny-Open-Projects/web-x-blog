"""事件溯源会话:快照 + 增量重放恢复状态,副作用事件幂等跳过。"""


def reducer(state, ev):
    """唯一的状态折叠函数:线上写入与恢复重放共用。"""
    t = ev["type"]
    if t == "user_msg":
        state["messages"].append(("user", ev["text"]))
    elif t == "assistant_msg":
        state["messages"].append(("assistant", ev["text"]))
    elif t == "slot":
        state["slots"][ev["key"]] = ev["value"]
    elif t == "side_effect":                       # 外部副作用
        if ev["id"] not in state["done_effects"]:
            state["done_effects"].add(ev["id"])
            state["effects_executed"] += 1
    return state


class SessionLog:
    def __init__(self):
        self.events, self.snapshot_at = [], -1
        self.snapshot = None

    def append(self, ev):
        ev["seq"] = len(self.events)
        self.events.append(ev)

    def take_snapshot(self, state):
        self.snapshot, self.snapshot_at = state, len(self.events) - 1

    def restore(self):
        import copy
        if self.snapshot is None:
            state = {"messages": [], "slots": {}, "done_effects": set(), "effects_executed": 0}
            start = 0
        else:
            state = copy.deepcopy(self.snapshot)
            state["done_effects"] = set(state["done_effects"])
            start = self.snapshot_at + 1
        for ev in self.events[start:]:
            state = reducer(state, ev)
        return state


if __name__ == "__main__":
    log = SessionLog()
    for ev in [{"type": "user_msg", "text": "订酒店"}, {"type": "slot", "key": "city", "value": "上海"},
               {"type": "side_effect", "id": "sms-1"}]:
        log.append(ev)
    state = log.restore()
    print("全量重放:", state["messages"], state["slots"], "副作用执行", state["effects_executed"])
    log.take_snapshot(state)
    log.append({"type": "assistant_msg", "text": "已订好上海酒店"})
    log.append({"type": "side_effect", "id": "sms-1"})   # 重放中会再次出现
    state2 = log.restore()
    assert state2["effects_executed"] == 1, "副作用必须幂等,重放不重复执行"
    assert state2["messages"][-1] == ("assistant", "已订好上海酒店")
    print("快照后增量重放 2 条事件,副作用去重生效")
