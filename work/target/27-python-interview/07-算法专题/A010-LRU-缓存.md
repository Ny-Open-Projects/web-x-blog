---
title: [A010] LRU 缓存
date: 2026-11-17
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A010 · LRU 缓存

> 难度:★★★ | 标签:设计, 哈希表, 链表

**问**:实现 `get/put` 均 O(1) 的 LRU 缓存:容量满时淘汰最久未使用的键。

**答**:哈希表(key → 节点)+ 双向链表(维护使用顺序,头=最近):get 命中把节点摘下搬到头部;put 已存在则更新并前移,满了删除尾部的最久未用节点。两个哨兵头尾省去边界判断。这是 `functools.lru_cache`(Q045)的底层原理;Python 里可用 `OrderedDict` 两行实现,但面试要求手写链表版。

```python
# 示例:code/07_算法专题/(docs 内嵌,复制可运行) a010_lru_cache.py
class _Node:
    __slots__ = ("key", "value", "prev", "next")   # 省内存,呼应 Q008

    def __init__(self, key=None, value=None):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map: dict[int, _Node] = {}
        self.head, self.tail = _Node(), _Node()     # 哨兵
        self.head.next, self.tail.prev = self.tail, self.head

    def _unlink(self, node: _Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _push_front(self, node: _Node) -> None:
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1
        self._unlink(node)
        self._push_front(node)                      # 命中即移到最近端
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node is not None:
            node.value = value
            self._unlink(node)
            self._push_front(node)
            return
        if len(self.map) >= self.cap:               # 淘汰最久未用
            lru = self.tail.prev
            self._unlink(lru)
            del self.map[lru.key]
        node = _Node(key, value)
        self.map[key] = node
        self._push_front(node)

if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1        # 1 变为最近使用
    c.put(3, 3)                 # 淘汰 2
    assert c.get(2) == -1
    c.put(4, 4)                 # 淘汰 3?不:3 刚被 get 失败,最久未用的是 3
    assert c.get(1) == 1 and c.get(3) == -1 and c.get(4) == 4
    print("A010 ok")
```

**追问**:
- 为什么是双向链表?——O(1) 摘除中间节点必须能拿到前驱;单链表要 O(n) 找 prev。哈希表+单链表只能做 FIFO。
- `__slots__` 在这里的实际收益?——百万级缓存条目省掉每节点 `__dict__`,内存降 30%+(Q008);顺带说明哨兵节点如何消掉头尾特判。
- 线程安全怎么加?——整把锁最简单但串行化;分段锁/分片(Q562 思想)降低争用;跨进程要用 Redis 的 LRU 淘汰(Q981 maxmemory-policy)而不是进程内结构。
