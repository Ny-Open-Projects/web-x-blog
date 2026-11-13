# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130717572
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findCheapestPrice(
    n, flights, src, dst, k
):  # 定义函数 findCheapestPrice（参数：元素个数, flights, src, dst, 下标 k）
    INF = float("inf")  # 把 float('inf') 存入 INF
    w = [[INF] * n for _ in range(n)]  # 把 [[INF] 乘 元素个数 for _ in range(元素个数)] 存入 权重
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        w[i][i] = 0  # 把 0 写入 w[i][i]
    for frm, to, price in flights:  # for frm, to, price in flights:
        w[frm][to] = price  # 把 price 写入 w[frm][to]

    dist = [INF] * n  # 把 [INF] 乘 元素个数 存入 dist
    dist[src] = 0  # 把 0 写入 dist[src]
    # 邻接矩阵版 Bellman-Ford，最多 k+1 条边
    for _ in range(k + 1):  # 让 _ 从 下标 k 加 1 遍历
        prev = dist[:]  # 把 复制 dist 存入 前一个
        for i in range(n):  # 让 下标 i 从 元素个数 遍历
            if prev[i] == INF:  # 若 前一个[下标 i] 等于 INF
                continue  # 跳过本轮，进入下一次
            for j in range(n):  # 让 下标 j 从 元素个数 遍历
                if prev[i] + w[i][j] < dist[j]:  # 若 前一个[下标 i] 加 权重[下标 i][下标 j] 小于 dist[下标 j]
                    dist[j] = prev[i] + w[i][j]  # 把 前一个[下标 i] 加 权重[下标 i][下标 j] 写入 dist[j]
    return -1 if dist[dst] == INF else dist[dst]  # 返回 减 1 if dist[dst] 等于 INF else dist[dst]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(
        findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1)
    )  # 打印输出
