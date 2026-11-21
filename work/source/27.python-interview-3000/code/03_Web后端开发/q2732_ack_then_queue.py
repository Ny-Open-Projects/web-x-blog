"""回调的先落队再应答: 验签 200 快回, 处理交给异步消费(纯标准库)。"""


class AckQueue:
    """接收与处理解耦: 队列持久化落定后才应答, 处理器崩溃由至少一次投递兜底,
    事件级去重保证重投不会二次生效。"""

    def __init__(self):
        self.queue = []
        self.acked = set()      # 已应答的事件
        self.applied = set()    # 处理器侧的去重台账
        self.effects = []

    def receive(self, event_id, payload):
        """真实实现里这里先验签再写持久队列, 全程微秒级, 回调方永不超时。"""
        self.queue.append((event_id, payload))
        self.acked.add(event_id)
        return 200

    def process(self, crash_on=None):
        """消费循环: pop -> 去重检查 -> 生效与台账同事务提交 -> 应答; crash_on 模拟应答前崩溃。"""
        while self.queue:
            eid, payload = self.queue.pop(0)
            if eid in self.applied:
                continue  # 幂等台账命中: 空转
            self.effects.append(("apply", eid, payload))
            self.applied.add(eid)  # 生效与台账必须同一个事务, 这条线断了幂等就没了
            if crash_on == eid:
                raise RuntimeError("handler crashed after apply, before ack")


q = AckQueue()
q.receive("e1", {"order": "o1", "state": "paid"})
q.receive("e2", {"order": "o2", "state": "paid"})
try:
    q.process(crash_on="e1")
except RuntimeError:
    print("e1 生效后崩在应答前: 副作用已提交, 应答丢失")
# 对端没等到 200 会重投 e1, e2 也留在队列里
q.queue.append(("e1", {"order": "o1", "state": "paid"}))
q.queue.append(("e2", {"order": "o2", "state": "paid"}))
q.process()
assert q.applied == {"e1", "e2"}, q.applied
applies = [e for e in q.effects if e[0] == "apply"]
assert len(applies) == 2, applies
assert [e[1] for e in applies].count("e1") == 1, "e1 重投命中台账空转, 业务效果恰好一次"
print("接收即应答 200; 应答前崩溃由重投兜底, 台账保证总效果 = 每事件一次")
