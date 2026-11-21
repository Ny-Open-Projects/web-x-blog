"""最小跳表: 概率层高 + 插入 + 范围查询"""
import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * level

class SkipList:
    MAX = 8
    P = 0.5

    def __init__(self):
        self.head = Node(None, self.MAX)
        self.level = 1

    def _rand_level(self):
        lvl = 1
        while random.random() < self.P and lvl < self.MAX:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [self.head] * self.MAX           # 顶层之上统一指向 head
        node = self.head
        for i in reversed(range(self.level)):
            while node.forward[i] and node.forward[i].key < key:
                node = node.forward[i]
            update[i] = node
        lvl = self._rand_level()
        self.level = max(self.level, lvl)
        new = Node(key, lvl)
        for i in range(lvl):
            new.forward[i] = update[i].forward[i]
            update[i].forward[i] = new

    def range_(self, lo, hi):
        out, node = [], self.head
        for i in reversed(range(self.level)):
            while node.forward[i] and node.forward[i].key < lo:
                node = node.forward[i]
        node = node.forward[0]
        while node and node.key <= hi:
            out.append(node.key)
            node = node.forward[0]
        return out

if __name__ == "__main__":
    random.seed(7)
    sl = SkipList()
    for k in [3, 1, 4, 1, 5, 9, 2, 6]:
        sl.insert(k)
    print("范围 [2,6):", sl.range_(2, 6), "<- 底层有序链表天然支持")
    print("查找路径: 从顶层逐层向右下, 期望 O logN")
