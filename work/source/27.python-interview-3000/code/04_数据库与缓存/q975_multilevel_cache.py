"""两级缓存 + 失效广播: 本实例写后通知其他实例删 L1"""
import queue
import threading

class Node:
    def __init__(self, name, bus):
        self.name, self.l1, self.bus = name, {}, bus
        bus.register(self)

    def get(self, key, l2, db):
        if key in self.l1:
            return self.l1[key], "L1"
        v = l2.get(key) or db.get(key)
        self.l1[key] = v
        return v, "L2/DB"

    def invalidate(self, key):
        self.l1.pop(key, None)

class Bus:
    def __init__(self):
        self.nodes, self.box = [], queue.Queue()

    def register(self, node):
        self.nodes.append(node)

    def broadcast_invalidate(self, src, key):
        for n in self.nodes:                  # pub/sub: 逐节点投递失效
            if n is not src:
                n.invalidate(key)

if __name__ == "__main__":
    db, l2 = {"stock": 10}, {"stock": 10}
    bus = Bus()
    a, b = Node("nodeA", bus), Node("nodeB", bus)

    print("B 读:", b.get("stock", l2, db))
    # nodeA 更新库并失效两级
    db["stock"], l2["stock"] = 99, 99
    bus.broadcast_invalidate(a, "stock")     # 广播已同步清空 B 的 L1
    print("广播后 B 再读:", b.get("stock", l2, db), "<- 已看到新值")
