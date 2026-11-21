"""简化两级 B+Tree: 演示根节点路由到叶子与叶子链表范围扫描"""
from bisect import bisect_right
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Leaf:
    keys: list = field(default_factory=list)
    values: list = field(default_factory=list)
    next: Optional["Leaf"] = None  # 模拟叶子间的双向链表

    def range_scan(self, lo, hi):
        """叶子链表上的范围扫描: 索引高效支持 BETWEEN / ORDER BY 的原因"""
        out, node, i = [], self, bisect_right(self.keys, lo) - 1
        while node:
            while i < len(node.keys) and node.keys[i] < hi:
                out.append((node.keys[i], node.values[i]))
                i += 1
            node, i = node.next, 0
        return out


@dataclass
class Branch:
    """非叶子节点: 只存分隔 key 与子节点指针"""
    separators: list                # 例: [11, 41, 71]
    children: list

    def find_leaf(self, key) -> Leaf:
        idx = bisect_right(self.separators, key)
        child = self.children[idx]
        return child.find_leaf(key) if isinstance(child, Branch) else child


if __name__ == "__main__":
    l1, l2, l3 = Leaf([1, 5, 9], ["a", "b", "c"]), Leaf([11, 25], ["d", "e"]), Leaf([41, 60], ["f", "g"])
    l1.next, l2.next = l2, l3
    root = Branch([11, 41], [l1, l2, l3])

    print("等值查找 key=25:", root.find_leaf(25).values[root.find_leaf(25).keys.index(25)])
    print("范围扫描 5..45:", l1.range_scan(5, 45))
