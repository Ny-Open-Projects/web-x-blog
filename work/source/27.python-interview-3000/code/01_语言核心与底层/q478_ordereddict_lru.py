from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return None
        self.data.move_to_end(key)            # 命中即最新
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.cap:
            self.data.popitem(last=False)     # 淘汰最旧

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    print(cache.get("a"))                     # a 变为最新
    cache.put("c", 3)                         # 超容:淘汰 b
    print("b evicted:", cache.get("b"))
    print("a kept:", cache.get("a"), "c:", cache.get("c"))
