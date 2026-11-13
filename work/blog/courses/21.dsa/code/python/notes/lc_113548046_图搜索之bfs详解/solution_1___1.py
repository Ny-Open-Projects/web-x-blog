# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import deque  # from collections import deque


def bfs(graph, start):  # 定义函数 bfs（参数：graph, 起点）
    """广度优先搜索：逐层扩散（前锋面），返回访问顺序与生成树父指针。"""
    n = len(graph)  # 把 长度(graph) 存入 元素个数
    status = ["UNDISCOVERED"] * n  # UNDISCOVERED / DISCOVERED / VISITED
    parent = [-1] * n  # 把 [ 减 1] 乘 元素个数 存入 parent
    order = []  # 把 [] 存入 order
    q = deque([start])  # 把 deque([起点]) 存入 节点
    status[start] = "DISCOVERED"  # 把 'DISCOVERED' 写入 status[start]
    clock = 0  # 把 0 存入 clock
    while q:  # 循环，直到不满足「节点」
        v = q.popleft()  # 把 节点.popleft() 存入 值
        clock += 1  # clock累加 1
        order.append(v)  # 把 值 追加到列表尾部
        for u in graph[v]:  # 逐个取出 graph 的元素（节点 u）
            if status[u] == "UNDISCOVERED":  # 若 status[节点 u] 等于 'UNDISCOVERED'
                status[u] = "DISCOVERED"  # 把 'DISCOVERED' 写入 status[u]
                parent[u] = v  # 把 值 写入 parent[u]
                q.append(u)  # 把 节点 u 追加到列表尾部
            # 否则为跨边 CROSS，无需处理
        status[v] = "VISITED"  # 把 'VISITED' 写入 status[v]
    return order, parent  # 返回 order, parent


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 无向图邻接表
    graph = [
        [1, 2],  # 0
        [0, 3, 4],  # 1
        [0, 5],  # 2
        [1],  # 3
        [1],  # 4
        [2],  # 5
    ]
    order, parent = bfs(graph, 0)  # 把 bfs(graph, 0) 写入 order, parent
    print("BFS 访问顺序:", order)  # 打印输出
    print("父指针:", parent)  # 打印输出
