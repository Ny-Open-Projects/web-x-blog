# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
# LRU 缓存 - 方案3: 手动双向链表 + dict


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Node:  # 定义类
    __slots__ = ("key", "value", "prev", "next")  # 把 ('key', 'value', '前一个', '下一个') 存入 __slots__

    def __init__(self, key=None, value=None):  # 构造函数：初始化成员
        self.key = key  # 把 key 写入 self.key
        self.value = value  # 把 value 写入 self.value
        self.prev = None  # 把 None 写入 前一个
        self.next = None  # 把 None 写入 下一个


class LRUCache:  # 定义类
    def __init__(self, length):  # 构造函数：初始化成员
        self.length = length  # 把 长度 写入 长度
        self.data = {}  # 把 {} 写入 self.data
        self.head = Node()  # 把 Node() 写入 头节点
        self.tail = Node()  # 把 Node() 写入 尾节点
        self.head.next = self.tail  # 把 self.尾节点 写入 下一个
        self.tail.prev = self.head  # 把 self.头节点 写入 前一个

    def _remove(self, node):  # 定义函数 _remove（参数：self, 节点）
        node.prev.next = node.next  # 把 节点.下一个 写入 下一个
        node.next.prev = node.prev  # 把 节点.前一个 写入 前一个

    def _add_to_tail(self, node):  # 定义函数 _add_to_tail（参数：self, 节点）
        node.prev = self.tail.prev  # 把 self.尾节点.前一个 写入 前一个
        node.next = self.tail  # 把 self.尾节点 写入 下一个
        self.tail.prev.next = node  # 把 节点 写入 下一个
        self.tail.prev = node  # 把 节点 写入 前一个

    def set(self, key, value):  # 定义函数 set（参数：self, key, value）
        if key in self.data:  # 若 key in self.data
            self._remove(self.data[key])  # self._remove(self.data[key])
        node = Node(key, value)  # 把 Node(key, value) 存入 节点
        self.data[key] = node  # 把 节点 写入 self.data[key]
        self._add_to_tail(node)  # self._add_to_tail(节点)
        if len(self.data) > self.length:  # 若 长度(self.data) 超过 self.长度
            lru = self.head.next  # 把 self.头节点.下一个 存入 lru
            self._remove(lru)  # self._remove(lru)
            del self.data[lru.key]  # del self.data[lru.key]

    def get(self, key):  # 定义函数 get（参数：self, key）
        if key not in self.data:  # 若 key not in self.data
            return None  # 返回 None
        node = self.data[key]  # 把 self.data[key] 存入 节点
        self._remove(node)  # self._remove(节点)
        self._add_to_tail(node)  # self._add_to_tail(节点)
        return node.value  # 返回 节点.value


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    lru_cache = LRUCache(2)  # 把 LRUCache(2) 存入 lru_cache
    lru_cache.set(1, 1)  # lru_cache.set(1, 1)
    lru_cache.set(2, 2)  # lru_cache.set(2, 2)
    print(lru_cache.get(1))  # 1
    lru_cache.set(3, 3)  # lru_cache.set(3, 3)
    print(lru_cache.get(2))  # None
    lru_cache.set(4, 4)  # lru_cache.set(4, 4)
    print(lru_cache.get(1))  # None
    print(lru_cache.get(3))  # 3
    print(lru_cache.get(4))  # 4
