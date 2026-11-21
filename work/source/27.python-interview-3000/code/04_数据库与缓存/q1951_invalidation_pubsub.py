"""写后失效的订阅实现: 失效广播与乱序容忍"""
import threading

class EventBus:
    """极简进程内发布订阅 模拟 keyspace 通知或 binlog 消费"""
    def __init__(self):
        self.subs = []
        self.lock = threading.Lock()
    def subscribe(self, fn):
        with self.lock:
            self.subs.append(fn)
    def publish(self, key, version):
        with self.lock:
            subs = list(self.subs)
        for fn in subs:
            fn(key, version)

class LocalCache:
    """每个节点一份本地缓存 只接受版本号不小于本地的失效事件"""
    def __init__(self, name, bus):
        self.name = name
        self.data = {}
        self.versions = {}
        bus.subscribe(self.on_invalidate)
    def on_invalidate(self, key, version):
        old = self.versions.get(key, 0)
        if version >= old:
            self.data.pop(key, None)
            self.versions[key] = version
            return "invalidated"
        return "ignored-stale"
    def load(self, key, value, version):
        self.data[key] = value
        self.versions[key] = version
    def get(self, key):
        return self.data.get(key)

bus = EventBus()
node_a = LocalCache("node-a", bus)
node_b = LocalCache("node-b", bus)
for node in (node_a, node_b):
    node.load("u:1", "Alice-v1", 1)
print("失效前  两节点读到:", node_a.get("u:1"), node_b.get("u:1"))

bus.publish("u:1", 2)     # 写库成功后发布失效事件
print("广播失效后 node-a:", node_a.get("u:1"), " node-b:", node_b.get("u:1"))

# 乱序事件: 迟到的旧版本事件不能误删新数据
node_a.load("u:1", "Alice-v2", 2)
print("迟到版本 1 事件 ->", node_a.on_invalidate("u:1", 1), " node-a 仍有:", node_a.get("u:1"))
print("新版本 3 事件   ->", node_a.on_invalidate("u:1", 3), " node-a 读到:", node_a.get("u:1"))

# 失效失败的兜底: 节点离线期间错过事件 靠重连后全量拉版本或短 TTL 收敛
print("结论: 失效广播把缓存从同步写改成异步通知 版本号守门容忍乱序 错过事件的节点靠重连同步与短 TTL 兜底")
