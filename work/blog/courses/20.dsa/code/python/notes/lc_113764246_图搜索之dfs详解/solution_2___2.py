# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
import sys  # 引入依赖

sys.setrecursionlimit(10000)  # sys.setrecursionlimit(10000)


def topo_sort_dfs(graph):  # 定义函数 topo_sort_dfs（参数：graph）
    """基于 DFS 的拓扑排序：以终为始，回溯时将结点压栈，逆序即为拓扑序。"""
    n = len(graph)  # 把 长度(graph) 存入 元素个数
    status = ["UNDISCOVERED"] * n  # 把 ['UNDISCOVERED'] 乘 元素个数 存入 status
    stack = []  # 把 [] 存入 栈

    def visit(v):  # 定义函数 visit（参数：值）
        status[v] = "DISCOVERED"  # 把 'DISCOVERED' 写入 status[v]
        for u in graph[v]:  # 逐个取出 graph 的元素（节点 u）
            if status[u] == "UNDISCOVERED":  # 若 status[节点 u] 等于 'UNDISCOVERED'
                visit(u)  # visit(节点 u)
        status[v] = "VISITED"  # 把 'VISITED' 写入 status[v]
        stack.append(v)  # 回溯时入栈（出度为 0 的点最先入栈）

    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        if status[i] == "UNDISCOVERED":  # 若 status[下标 i] 等于 'UNDISCOVERED'
            visit(i)  # visit(下标 i)

    return stack[::-1]  # 逆序得到拓扑序


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 课程依赖：A(0)->C(2), B(1)->C(2), C(2)->D(3), D(3)->E(4), E(4)->F(5)
    graph = [
        [2],  # 0 A
        [2],  # 1 B
        [3],  # 2 C
        [4],  # 3 D
        [5],  # 4 E
        [],  # 5 F
    ]
    print("拓扑序:", topo_sort_dfs(graph))  # [0, 1, 2, 3, 4, 5] 等合法序
