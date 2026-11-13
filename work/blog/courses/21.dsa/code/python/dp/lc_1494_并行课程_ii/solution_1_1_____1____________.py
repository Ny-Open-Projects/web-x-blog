# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145380711
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minNumberOfSemesters(
    n, relations, k
):  # 定义函数 minNumberOfSemesters（参数：元素个数, relations, 下标 k）
    from functools import lru_cache  # from functools import lru_cache
    from itertools import combinations  # from itertools import combinations

    pre = [0] * n  # 把 [0] 乘 元素个数 存入 前缀和
    for u, v in relations:  # for 节点 u, 值 in relations:
        pre[v - 1] |= 1 << (u - 1)  # 把 1 小于 小于 (节点 u 减 1) 写入 pre[v - 1] |
    target = (1 << n) - 1  # 把 (1 小于 小于 元素个数) 减 1 存入 目标值

    @lru_cache(None)  # @lru_cache(None)
    def dfs(mask):  # 定义函数 dfs（参数：mask）
        if mask == target:  # 若 mask 等于 目标值
            return 0  # 返回 0
        cand = [
            i
            for i in range(n)  # 把 [下标 i for 下标 i in range(元素个数) 存入 cand
            if ((mask >> i) & 1) == 0 and (pre[i] & mask) == pre[i]
        ]
        best = n + 1  # 把 元素个数 加 1 存入 当前最优
        sz = min(k, len(cand))  # 把 取较小值 下标 k, 长度(cand)) 存入 sz
        for r in range(1, sz + 1):  # 让 右指针 从 1 到 sz 加 1 遍历
            for combo in combinations(cand, r):  # 逐个取出 combinations 的元素（combo）
                nmask = mask  # 把 mask 存入 nmask
                for c in combo:  # 逐个取出 combo 的元素（字符）
                    nmask |= 1 << c  # 把 (1 小于 小于 字符) 写入 nmask |
                best = min(best, 1 + dfs(nmask))  # 把 取较小值 当前最优, 1 加 dfs(nmask)) 存入 当前最优
        return best  # 返回 当前最优

    return dfs(0)  # 返回 dfs(0)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minNumberOfSemesters(4, [[2, 1], [3, 1], [1, 4]], 2))  # 打印输出
