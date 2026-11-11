# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


def dijkstra(graph, src):  # 定义函数 dijkstra（参数：graph, src）
    """Dijkstra 单源最短路径（优先队列实现）。graph: 邻接表 list[list[(to, weight)]]。"""
    n = len(graph)  # 把 长度(graph) 存入 元素个数
    dist = [float("inf")] * n  # 把 [float('inf')] 乘 元素个数 存入 dist
    dist[src] = 0  # 把 0 写入 dist[src]
    parent = [-1] * n  # 把 [ 减 1] 乘 元素个数 存入 parent
    pq = [(0, src)]  # 把 [(0, src)] 存入 优先队列
    while pq:  # 循环，直到不满足「优先队列」
        d, u = heapq.heappop(pq)  # 把 heapq.heappop(优先队列) 写入 d, u
        if d > dist[u]:  # 若 d 超过 dist[节点 u]
            continue  # 跳过本轮，进入下一次
        for v, w in graph[u]:  # for 值, 权重 in graph[节点 u]:
            if dist[u] + w < dist[v]:  # 若 dist[节点 u] 加 权重 小于 dist[值]
                dist[v] = dist[u] + w  # 把 dist[节点 u] 加 权重 写入 dist[v]
                parent[v] = u  # 把 节点 u 写入 parent[v]
                heapq.heappush(pq, (dist[v], v))  # heapq.heappush(优先队列, (dist[值], 值))
    return dist, parent  # 返回 dist, parent


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 带权有向图
    graph = [
        [(1, 4), (2, 1)],  # 0
        [(3, 1)],  # 1
        [(1, 2), (3, 5)],  # 2
        [(4, 3)],  # 3
        [],  # 4
    ]
    dist, parent = dijkstra(graph, 0)  # 把 dijkstra(graph, 0) 写入 dist, parent
    print("从源点 0 出发的最短距离:", dist)  # 打印输出
    print("父指针:", parent)  # 打印输出
