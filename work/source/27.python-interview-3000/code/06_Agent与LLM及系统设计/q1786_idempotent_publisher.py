"""幂等发布器:发布侧窗口去重,接收端幂等确认,双端合力保证副作用恰好一次。"""


class Receiver:
    """接收端桩:按 event_id 幂等消费,重复事件记为 duplicate。"""

    def __init__(self):
        self.applied = []
        self.duplicates = 0

    def deliver(self, event):
        if event["event_id"] in self.applied:
            self.duplicates += 1
            return "duplicate"
        self.applied.append(event["event_id"])
        return "applied"


class IdempotentPublisher:
    def __init__(self, receiver, window=4):
        self.receiver = receiver
        self.window = window
        self.sent = []                           # 窗口内已发布 event_id
        self.skipped = 0

    def publish(self, event_id, payload):
        if event_id in self.sent:
            self.skipped += 1
            return "skipped"                     # 窗口内重复:发布侧拦截
        self.sent.append(event_id)
        if len(self.sent) > self.window:
            self.sent.pop(0)                     # 窗口滑动:老事件允许重发
        return self.receiver.deliver({"event_id": event_id, "payload": payload})


if __name__ == "__main__":
    rx = Receiver()
    pub = IdempotentPublisher(rx, window=4)

    assert pub.publish("evt-1", {"order": "o1"}) == "applied"
    assert pub.publish("evt-1", {"order": "o1"}) == "skipped", "窗口内重复被拦截"
    for i in range(2, 7):                        # 连发 5 个新事件,evt-1 滑出窗口
        pub.publish("evt-%d" % i, {"n": i})
    assert pub.publish("evt-1", {"order": "o1"}) == "duplicate", "窗口外靠接收端兜底"
    assert rx.duplicates == 1
    assert rx.applied == ["evt-1", "evt-2", "evt-3", "evt-4", "evt-5", "evt-6"]
    assert len(rx.applied) == len(set(rx.applied)), "副作用严格一次"
    print("幂等发布通过:窗口内发布侧拦截,窗口外接收端幂等兜底,副作用计数为 1")
