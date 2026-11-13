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
    visited[node] = Node(node.val)  # 把 Node(节点.值) 写入 visited[node]
    q = [node]  # 把 [节点] 存入 节点
    while q:  # 循环，直到不满足「节点」
        n = q.pop(0)  # 把 节点 弹出 0) 存入 元素个数
        for ne in n.neighbors:  # 逐个取出 元素个数 的元素（ne）
            if ne not in visited:  # 若 ne not in 已访问集合
                q.append(ne)  # 把 ne 追加到列表尾部
                visited[ne] = Node(ne.val)  # 把 Node(ne.值) 写入 visited[ne]
            visited[n].neighbors.append(visited[ne])  # 把 已访问集合[ne] 追加到列表尾部
    return visited[node]  # 返回 已访问集合[节点]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    n1 = Node(1)  # 把 Node(1) 存入 n1
    n2 = Node(2)  # 把 Node(2) 存入 n2
    n3 = Node(3)  # 把 Node(3) 存入 n3
    n4 = Node(4)  # 把 Node(4) 存入 n4
    n1.neighbors = [n2, n4]  # 把 [n2, n4] 写入 n1.neighbors
    n2.neighbors = [n1, n3]  # 把 [n1, n3] 写入 n2.neighbors
    n3.neighbors = [n2, n4]  # 把 [n2, n4] 写入 n3.neighbors
    n4.neighbors = [n1, n3]  # 把 [n1, n3] 写入 n4.neighbors
    c = cloneGraph(n1)  # 把 cloneGraph(n1) 存入 字符
    print(c.val, [x.val for x in c.neighbors])  # 打印输出
