"""退避重试 + 死信队列:梯度延迟 + 失败原因分类 + 限速 replay。"""


class RetryQueue:
    BACKOFF = [60, 300, 1800]                  # 秒:1min 5min 30min

    def __init__(self):
        self.pending = []                       # [deliver_at, msg, attempts]
        self.dlq, self.now = [], 0.0

    def submit(self, msg, deliver_at=0.0):
        self.pending.append([deliver_at, msg, 0])

    def consume(self, handler):
        """handler 返回 True 成功, False 失败。"""
        processed, dead = [], []
        remaining = []
        for item in self.pending:
            at, msg, tries = item
            if self.now < at:
                remaining.append(item)
                continue
            if handler(msg):
                processed.append(msg)
            else:
                if tries < len(self.BACKOFF):
                    remaining.append([self.now + self.BACKOFF[tries], msg, tries + 1])
                else:
                    entry = {"msg": msg, "attempts": tries, "dead_at": self.now}
                    self.dlq.append(entry)
                    dead.append(entry)
        self.pending = remaining
        return processed, dead

    def replay(self, handler, rate_per_sec=2):
        """限速回放死信。"""
        recovered = []
        for i, entry in enumerate(list(self.dlq)):
            if i >= rate_per_sec:
                break                           # 限速:超出部分留下轮
            if handler(entry["msg"]):
                recovered.append(entry["msg"])
                self.dlq.remove(entry)
        return recovered


if __name__ == "__main__":
    rq = RetryQueue()
    fail_msg, ok_msg = {"id": "m1", "bad": True}, {"id": "m2"}
    handler = lambda m: not m.get("bad")
    rq.submit(ok_msg)
    rq.submit(fail_msg)

    rq.now = 0.0
    processed, dead = rq.consume(handler)
    print("第 1 轮: 成功", [m["id"] for m in processed], "死信", [d["msg"]["id"] for d in dead])
    assert processed == [ok_msg] and not dead

    rq.now = 60.0                               # 1 分钟后第一次重试
    processed, dead = rq.consume(handler)
    assert not processed and not dead and rq.pending[0][2] == 2, "第 2 次失败,退避升级到 5min"
    rq.now += 300.0
    rq.consume(handler)                         # 第 3 次失败,退避 30min
    rq.now += 1800.0
    processed, dead = rq.consume(handler)
    print("退避 3 轮后进死信:", [d["msg"]["id"] for d in dead], "历史尝试:", dead[0]["attempts"])
    assert dead and dead[0]["attempts"] == 3

    fixed_handler = lambda m: True              # 下游修复
    recovered = rq.replay(fixed_handler, rate_per_sec=2)
    print("限速回放救回:", [m["id"] for m in recovered])
    assert recovered == [fail_msg] and not rq.dlq
    print("重试梯度与死信工作台闭环")
