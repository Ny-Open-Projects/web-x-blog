"""手写 LRU: 哈希表 + 双向链表, 哨兵简化边界"""
class Node:
    def __init__(self, key=None, val=None):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head, self.tail = Node(), Node()      # 哨兵
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_front(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key, value):
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self._add_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, "a"); cache.put(2, "b")
    print("get 1:", cache.get(1), "<- 1 变为最新")
    cache.put(3, "c")                               # 淘汰 2
    print("get 2(已淘汰):", cache.get(2))
    print("get 3:", cache.get(3))
    print("Redis 近似 LRU: 随机采样 maxmemory-samples 挑最久未用, 非全局链表")
