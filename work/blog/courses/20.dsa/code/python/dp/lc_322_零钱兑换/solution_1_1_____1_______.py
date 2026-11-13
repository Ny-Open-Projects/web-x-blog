# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144851123
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def coinChange(coins, amount):  # 定义函数 coinChange（参数：硬币面额, 目标金额）
    import functools  # 引入依赖

    @functools.lru_cache(None)  # @functools.lru_cache(None)
    def dfs(rem):  # 定义函数 dfs（参数：rem）
        if rem == 0:  # 若 rem 等于 0
            return 0  # 返回 0
        if rem < 0:  # 若 rem 小于 0
            return float("inf")  # 返回 float('inf')
        best = float("inf")  # 把 float('inf') 存入 当前最优
        for c in coins:  # 逐个取出 硬币面额 的元素（字符）
            best = min(best, dfs(rem - c) + 1)  # 把 取较小值 当前最优, dfs(rem 减 字符) 加 1) 存入 当前最优
        return best  # 返回 当前最优

    res = dfs(amount)  # 把 dfs(目标金额) 存入 结果
    return res if res != float("inf") else -1  # 返回 结果 if 结果 不等于 float('inf') else 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(coinChange([1, 2, 5], 11))  # 打印输出
