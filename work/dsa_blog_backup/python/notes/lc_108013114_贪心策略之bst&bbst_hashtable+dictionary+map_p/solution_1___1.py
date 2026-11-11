# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class BST:  # 定义类
    """二叉搜索树（BST）：左子树 < 根 < 右子树。"""

    class Node:  # 定义类
        def __init__(self, val):  # 构造函数：初始化成员
            self.val = val  # 把 值 写入 值
            self.left = None  # 把 None 写入 左边界
            self.right = None  # 把 None 写入 右边界

    def __init__(self):  # 构造函数：初始化成员
        self.root = None  # 把 None 写入 根节点

    def insert(self, val):  # 定义函数 insert（参数：self, 值）
        if not self.root:  # 若 not self.根节点
            self.root = self.Node(val)  # 把 self.Node(值) 写入 根节点
            return  # return
        cur = self.root  # 把 self.根节点 存入 当前值
        while True:  # 循环，直到不满足「True」
            if val < cur.val:  # 若 值 小于 当前值.值
                if cur.left is None:  # 若 当前值.左边界 is None
                    cur.left = self.Node(val)  # 把 self.Node(值) 写入 左边界
                    break  # 跳出循环
                cur = cur.left  # 把 当前值.左边界 存入 当前值
            elif val > cur.val:  # 否则，若 值 超过 当前值.值
                if cur.right is None:  # 若 当前值.右边界 is None
                    cur.right = self.Node(val)  # 把 self.Node(值) 写入 右边界
                    break  # 跳出循环
                cur = cur.right  # 把 当前值.右边界 存入 当前值
            else:  # 否则
                break  # 已存在

    def search(self, val):  # 定义函数 search（参数：self, 值）
        cur = self.root  # 把 self.根节点 存入 当前值
        while cur:  # 循环，直到不满足「当前值」
            if val == cur.val:  # 若 值 等于 当前值.值
                return True  # 返回 True
            cur = (
                cur.left if val < cur.val else cur.right
            )  # 把 当前值.左边界 if 值 小于 当前值.值 else 当前值.右边界 存入 当前值
        return False  # 返回 False


def kruskal_mst(edges):  # 定义函数 kruskal_mst（参数：边集）
    """Kruskal 最小生成树：按权重升序加边，用并查集避免成环。edges = [(u, v, w), ...]"""
    parent = {}  # 把 {} 存入 parent

    def find(x):  # 定义函数 find（参数：x）
        parent.setdefault(x, x)  # parent.setdefault(x, x)
        while parent[x] != x:  # 循环，直到不满足「parent[x] 不等于 x」
            parent[x] = parent[parent[x]]  # 把 parent[parent[x]] 写入 parent[x]
            x = parent[x]  # 把 parent[x] 存入 x
        return x  # 返回 x

    def union(a, b):  # 定义函数 union（参数：数组, b）
        ra, rb = find(a), find(b)  # 把 find(数组), find(b) 写入 ra, rb
        if ra == rb:  # 若 ra 等于 rb
            return False  # 返回 False
        parent[ra] = rb  # 把 rb 写入 parent[ra]
        return True  # 返回 True

    total = 0  # 把 0 存入 总和
    for u, v, w in sorted(
        edges, key=lambda e: e[2]
    ):  # 把 lambda e: e[2]): 写入 for u, v, w in sorted(edges, key
        if union(u, v):  # 若 union(节点 u, 值
            total += w  # 总和累加 权重
    return total  # 返回 总和


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    bst = BST()  # 把 BST() 存入 bst
    for v in [5, 3, 7, 1, 9]:  # for 值 in [5, 3, 7, 1, 9]:
        bst.insert(v)  # bst 插入 值)
    print("search 7:", bst.search(7), " search 4:", bst.search(4))  # 打印输出
    print("mst cost:", kruskal_mst([[0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 2]]))  # 打印输出
