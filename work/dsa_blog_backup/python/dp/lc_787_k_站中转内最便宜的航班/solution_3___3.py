# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130717572
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findCheapestPrice(
    n, flights, src, dst, k
):  # 定义函数 findCheapestPrice（参数：元素个数, flights, src, dst, 下标 k）
    from collections import defaultdict  # from collections import defaultdict
    import functools  # 引入依赖

    graph = defaultdict(list)  # 把 defaultdict(列表) 存入 graph
    for frm, to, price in flights:  # for frm, to, price in flights:
        graph[frm].append((to, price))  # 把 (to, price 追加到列表尾部

    @functools.lru_cache(None)  # @functools.lru_cache(None)
    def dfs(city, rem):  # 定义函数 dfs（参数：city, rem）
        # rem: 还能乘坐的航班（边数）数量
        if city == dst:  # 若 city 等于 dst
            return 0  # 返回 0
        if rem == 0:  # 若 rem 等于 0
            return float("inf")  # 返回 float('inf')
        best = float("inf")  # 把 float('inf') 存入 当前最优
        for to, price in graph[city]:  # for to, price in graph[city]:
            nxt = dfs(to, rem - 1)  # 把 dfs(to, rem 减 1) 存入 nxt
            if nxt != float("inf"):  # 若 nxt 不等于 float('inf'
                best = min(best, price + nxt)  # 把 取较小值 当前最优, price 加 nxt) 存入 当前最优
        return best  # 返回 当前最优

    res = dfs(src, k + 1)  # 把 dfs(src, 下标 k 加 1) 存入 结果
    return -1 if res == float("inf") else res  # 返回 减 1 if 结果 等于 float('inf') else 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(
        findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1)
    )  # 打印输出
