# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
import sys  # 引入依赖

sys.setrecursionlimit(10000)  # sys.setrecursionlimit(10000)


def dfs(graph, start):  # 定义函数 dfs（参数：graph, 起点）
    """深度优先搜索：记录发现/结束时间戳，并对边分类(TREE/BACKWARD/FORWARD/CROSS)。"""
    n = len(graph)  # 把 长度(graph) 存入 元素个数
    status = ["UNDISCOVERED"] * n  # 把 ['UNDISCOVERED'] 乘 元素个数 存入 status
    d_time = [0] * n  # 把 [0] 乘 元素个数 存入 d_time
    f_time = [0] * n  # 把 [0] 乘 元素个数 存入 f_time
    parent = [-1] * n  # 把 [ 减 1] 乘 元素个数 存入 parent
    edges = {}  # 把 {} 存入 边集
    clock = 0  # 把 0 存入 clock

    def visit(v):  # 定义函数 visit（参数：值）
        nonlocal clock  # nonlocal clock
        clock += 1  # clock累加 1
        d_time[v] = clock  # 把 clock 写入 d_time[v]
        status[v] = "DISCOVERED"  # 把 'DISCOVERED' 写入 status[v]
        for u in graph[v]:  # 逐个取出 graph 的元素（节点 u）
            if status[u] == "UNDISCOVERED":  # 若 status[节点 u] 等于 'UNDISCOVERED'
                edges[(v, u)] = "TREE"  # 把 'TREE' 写入 edges[(v, u)]
                parent[u] = v  # 把 值 写入 parent[u]
                visit(u)  # visit(节点 u)
            elif status[u] == "DISCOVERED":  # 否则，若 status[节点 u] 等于 'DISCOVERED'
                edges[(v, u)] = "BACKWARD"  # 把 'BACKWARD' 写入 edges[(v, u)]
            else:  # 否则
                edges[(v, u)] = "FORWARD" if d_time[v] < d_time[u] else "CROSS"
        clock += 1  # clock累加 1
        f_time[v] = clock  # 把 clock 写入 f_time[v]
        status[v] = "VISITED"  # 把 'VISITED' 写入 status[v]

    visit(start)  # visit(起点)
    return d_time, f_time, edges, parent  # 返回 d_time, f_time, 边集, parent


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 有向图
    graph = [
        [1, 5],  # 0
        [2],  # 1
        [],  # 2
        [4],  # 3
        [5, 6],  # 4
        [1, 6],  # 5
        [],  # 6
    ]
    d, f, edges, parent = dfs(graph, 0)  # 把 dfs(graph, 0) 写入 d, f, edges, parent
    print("dTime:", d)  # 打印输出
    print("fTime:", f)  # 打印输出
    print("边分类:", edges)  # 打印输出
