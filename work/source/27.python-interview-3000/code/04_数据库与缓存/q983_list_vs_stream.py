"""List 抢夺消费 vs Stream 消费组 的最小对照"""
import collections
import threading

# ---- List 语义: 消费即删, 无重试 ----
lst = collections.deque(["m1", "m2", "m3"], maxlen=100)
got = []
while lst:
    got.append(lst.popleft())          # BRPOP: 弹出后消息即消失
print("List 消费后:", got, "队列空, 无处追溯")

# ---- Stream 语义: 日志留存 + 消费组 offset ----
class Stream:
    def __init__(self):
        self.log, self.seq = [], 0

    def xadd(self, payload):
        self.seq += 1
        self.log.append((f"{self.seq}-0", payload))

    def create_group(self):
        return {"last_delivered": 0, "pel": {}}

    def xreadgroup(self, group, consumer, count=10):
        out = []
        for mid, payload in self.log:
            if int(mid.split("-")[0]) > group["last_delivered"]:
                out.append((mid, payload))
                group["pel"][mid] = consumer
                group["last_delivered"] = int(mid.split("-")[0])
                if len(out) >= count:
                    break
        return out

    def xack(self, group, mid):
        group["pel"].pop(mid, None)

if __name__ == "__main__":
    s = Stream()
    for i in range(3):
        s.xadd(f"task{i}")
    g = s.create_group()
    msgs = s.xreadgroup(g, "worker1")
    print("Stream 消费:", msgs)
    s.xack(g, msgs[0][0])
    print("PEL 未确认:", g["pel"], "<- 未 ack 的消息可重投/转移")
