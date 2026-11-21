"""Redlock 多数派获取模拟 + fencing token 概念"""
import time

class Node:
    def __init__(self, name, fail=False):
        self.name, self.locked, self.fail = name, None, fail

    def lock(self, token, ttl):
        if self.fail:
            return False
        self.locked = token
        return True

def redlock(nodes, token, ttl=1.0):
    won = [n for n in nodes if n.lock(token, ttl)]
    return len(won) > len(nodes) // 2, [n.name for n in won]

if __name__ == "__main__":
    nodes = [Node(f"n{i}") for i in range(5)]
    nodes[3].fail = True                      # 一个节点故障
    ok, won = redlock(nodes, "t1")
    print("多数派获锁:", ok, "赢得节点:", won)

    # fencing token: 存储端拒绝旧令牌
    class Store:
        def __init__(self):
            self.max_token = 0
        def write(self, token):
            if token <= self.max_token:
                return "rejected: 旧令牌"
            self.max_token = token
            return "ok"
    store = Store()
    print("持锁方写入 token=7:", store.write(7))
    print("停顿后旧会话写入 token=7:", store.write(7), "<- fencing 兜底")
