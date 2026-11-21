"""Webhook 死信队列: 入队、盘点与人工重投(纯标准库)。"""


class Dlq:
    def __init__(self, max_attempts):
        self.max = max_attempts
        self.pending = {}     # event_id -> {payload, attempts, ...}
        self.dead = {}        # event_id -> {..., reason}

    def record_failure(self, event_id, payload, status):
        item = self.pending.setdefault(event_id, {"payload": payload, "attempts": 0})
        item["attempts"] += 1
        item["last_status"] = status
        if item["attempts"] >= self.max:
            item["reason"] = "接收方持续 5xx, 重试耗尽" if status >= 500 else "接收方明确拒绝"
            self.dead[event_id] = self.pending.pop(event_id)

    def record_success(self, event_id):
        self.pending.pop(event_id, None)
        self.dead.pop(event_id, None)            # 重投成功可从死信移除

    def replay(self, event_id):
        if event_id in self.dead:
            item = self.dead.pop(event_id)
            item["attempts"] = 0
            self.pending[event_id] = item
            return True
        return False


dlq = Dlq(max_attempts=3)
dlq.record_failure("ev1", {"type": "order.paid"}, 503)
dlq.record_failure("ev1", {"type": "order.paid"}, 503)
dlq.record_failure("ev2", {"type": "user.signup"}, 503)
dlq.record_failure("ev2", {"type": "user.signup"}, 503)
dlq.record_success("ev2")                        # 第三次成了
dlq.record_failure("ev1", {"type": "order.paid"}, 503)
print("死信:", {k: (v["attempts"], v["reason"]) for k, v in dlq.dead.items()})
print("重投 ev1:", dlq.replay("ev1"), "重投不存在:", dlq.replay("ev9"))
dlq.record_failure("ev1", {"type": "order.paid"}, 200)
print("重投成功后 pending:", list(dlq.pending), "dead:", list(dlq.dead))
print("要点: event_id 唯一防重复入队; 死信要带原因与最后状态; 人工重投走白名单接口")
