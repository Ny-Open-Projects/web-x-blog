# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Node:  # 定义类
    def __init__(self, val=0, neighbors=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):  # 定义函数 cloneGraph（参数：节点）
    if not node:  # 若 not 节点
        return None  # 返回 None
    visited = {}  # 把 {} 存入 已访问集合

    def dfs(n):  # 定义函数 dfs（参数：元素个数）
        if n in visited:  # 若 元素个数 in 已访问集合
            return visited[n]  # 返回 已访问集合[元素个数]
        clone = Node(n.val)  # 把 Node(元素个数.值) 存入 clone
        visited[n] = clone  # 把 clone 写入 visited[n]
        for neighbor in n.neighbors:  # 逐个取出 元素个数 的元素（neighbor）
            clone.neighbors.append(dfs(neighbor))  # 把 dfs(neighbor 追加到列表尾部
        return clone  # 返回 clone

    return dfs(node)  # 返回 dfs(节点)


def build_graph(adj):  # 定义函数 build_graph（参数：邻接表）
    # adj: list of lists (1-indexed values)
    nodes = {i: Node(i) for i in range(1, len(adj) + 1)}
    for i, nbrs in enumerate(adj, start=1):  # 同时取 下标 i 与 nbrs 遍历
        for nb in nbrs:  # 逐个取出 nbrs 的元素（nb）
            nodes[i].neighbors.append(nodes[nb])  # 把 nodes[nb] 追加到列表尾部
    return nodes[1]  # 返回 nodes[1]


def graph_signature(node):  # 定义函数 graph_signature（参数：节点）
    visited = {}  # 把 {} 存入 已访问集合

    def dfs(n):  # 定义函数 dfs（参数：元素个数）
        if n.val in visited:  # 若 元素个数.值 in 已访问集合
            return  # return
        visited[n.val] = sorted(
            x.val for x in n.neighbors
        )  # 把 sorted(x.值 for x in 元素个数.neighbors) 写入 visited[n.val]
        for x in n.neighbors:  # 逐个取出 元素个数 的元素（x）
            dfs(x)  # dfs(x)

    dfs(node)  # dfs(节点)
    return visited  # 返回 已访问集合


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = build_graph(
        [[2, 4], [1, 3], [2, 4], [1, 3]]
    )  # 把 build_graph([[2, 4], [1, 3], [2, 4], [1, 3]]) 存入 根节点
    cloned = cloneGraph(root)  # 把 cloneGraph(根节点) 存入 cloned
    print(graph_signature(cloned))  # 打印输出
