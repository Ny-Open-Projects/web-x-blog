"""pub/sub 在线广播(离线丢) vs stream 落盘回放"""
import queue

class MiniPubSub:
    def __init__(self):
        self.subs = {}

    def subscribe(self, ch):
        q = queue.Queue()
        self.subs.setdefault(ch, []).append(q)
        return q

    def publish(self, ch, msg):
        for q in self.subs.get(ch, []):
            q.put(msg)                     # 只有在线订阅者收到

class MiniStream:
    def __init__(self):
        self.log = []

    def xadd(self, msg):
        self.log.append(msg)

    def read_from(self, offset):
        return self.log[offset:]           # 离线消息仍可回放

if __name__ == "__main__":
    ps = MiniPubSub()
    q = ps.subscribe("cfg")
    ps.publish("cfg", "v2")
    print("pub/sub 在线收到:", q.get())
    print("pub/sub 离线消息: 发布时无订阅者 -> 直接丢弃")

    ms = MiniStream()
    ms.xadd("event1"); ms.xadd("event2")     # 消费者此刻离线
    print("stream 离线后回放:", ms.read_from(0), "<- 不丢")
    print("选择: 丢了无所谓用 pub/sub, 不可丢用 stream 或 MQ")
