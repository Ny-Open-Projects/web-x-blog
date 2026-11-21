"""PEL 重投与死信转移: delivery_count 超限进 DLQ"""
import time

class Group:
    def __init__(self):
        self.pel = {}                       # mid -> {consumer, count, ts}

    def delivered(self, mid, consumer):
        rec = self.pel.setdefault(mid, {"consumer": consumer, "count": 0,
                                        "ts": time.monotonic()})
        rec["count"] += 1

    def ack(self, mid):
        self.pel.pop(mid, None)

    def autoclaim(self, dead_after_count=3, idle=0.1):
        now = time.monotonic()
        reclaim, dead = [], []
        for mid, rec in list(self.pel.items()):
            if now - rec["ts"] > idle:
                if rec["count"] >= dead_after_count:
                    dead.append(mid)
                    del self.pel[mid]          # 转入死信队列后移出 PEL
                else:
                    reclaim.append(mid)
        return reclaim, dead

if __name__ == "__main__":
    g = Group()
    for mid in ("1-0", "2-0", "3-0"):
        g.delivered(mid, "w1")              # w1 崩溃未 ack
    time.sleep(0.2)
    reclaim, dead = g.autoclaim()
    print("第一轮可重投:", reclaim, "死信:", dead)
    for mid in reclaim:
        g.delivered(mid, "w2")              # 转给健康 worker, 重试计数+1
    g.ack("1-0")                            # w2 处理成功
    reclaim, dead = g.autoclaim()
    for mid in reclaim:
        g.delivered(mid, "w3")              # 又重试一轮
    _, dead = g.autoclaim()                 # 计数到 3 -> 死信
    print("毒消息进死信:", dead, "<- 记录并告警, 人工介入")
    print("剩余 PEL:", g.pel)
