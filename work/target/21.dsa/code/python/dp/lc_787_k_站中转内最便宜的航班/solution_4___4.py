# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130717572
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findCheapestPrice(
    n, flights, src, dst, k
):  # 定义函数 findCheapestPrice（参数：元素个数, flights, src, dst, 下标 k）
    INF = float("inf")  # 把 float('inf') 存入 INF
    dist = [INF] * n  # 把 [INF] 乘 元素个数 存入 dist
    dist[src] = 0  # 把 0 写入 dist[src]
    # Bellman-Ford：最多经过 k+1 条边
    for _ in range(k + 1):  # 让 _ 从 下标 k 加 1 遍历
        prev = dist[:]  # 把 复制 dist 存入 前一个
        for frm, to, price in flights:  # for frm, to, price in flights:
            if prev[frm] != INF:  # 若 前一个[frm] 不等于 INF
                dist[to] = min(
                    dist[to], prev[frm] + price
                )  # 把 取较小值 dist[to], 前一个[frm] 加 price) 写入 dist[to]
    return dist[dst] if dist[dst] != INF else -1  # 返回 dist[dst] if dist[dst] 不等于 INF else 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(
        findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1)
    )  # 打印输出
