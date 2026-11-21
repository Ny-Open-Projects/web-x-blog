"""异步回调的幂等落库与状态机: 重投不重放副作用(纯标准库)。"""

ALLOWED = {"created": {"paid"}, "paid": {"shipped"}, "shipped": set()}


class CallbackStore:
    """(channel, event_id) 唯一索引先落库再执行, 重复投递直接回首次结果。

    非法状态转换也落库: 下次重投同一事件时命中索引原样返回,
    不会在状态推进后再被误判为非法。
    """

    def __init__(self):
        self.seen = {}
        self.orders = {}

    def handle(self, channel, event_id, order, action):
        key = (channel, event_id)
        if key in self.seen:
            return {"status": "duplicate", "result": self.seen[key]}
        current = self.orders.get(order, "created")
        if action not in ALLOWED.get(current, set()):
            self.seen[key] = {"ok": False, "why": "illegal_%s_to_%s" % (current, action)}
            return {"status": "stored", "result": self.seen[key]}
        self.orders[order] = action
        self.seen[key] = {"ok": True, "state": action}
        return {"status": "stored", "result": self.seen[key]}


store = CallbackStore()
r1 = store.handle("pay", "e1", "o1", "paid")
assert r1 == {"status": "stored", "result": {"ok": True, "state": "paid"}}
r2 = store.handle("pay", "e1", "o1", "paid")
assert r2["status"] == "duplicate" and r2["result"] == r1["result"], "重投回放首次结果"
assert store.orders["o1"] == "paid", "副作用只发生一次"

r3 = store.handle("pay", "e2", "o1", "created")  # 乱序旧事件: paid 退回 created 非法
assert r3["status"] == "stored" and not r3["result"]["ok"]
r4 = store.handle("pay", "e2", "o1", "created")
assert r4["status"] == "duplicate" and r4["result"] == r3["result"]

r5 = store.handle("pay", "e3", "o1", "shipped")
assert r5["result"]["ok"], "合法转换继续推进"
assert store.orders["o1"] == "shipped"
print("正常链: created->paid->shipped 各一次副作用")
print("重复投递 -> duplicate 原结果; 非法转换 -> 落库失败结果, 重投不再重算")
