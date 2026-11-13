# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def change(amount, coins):  # 定义函数 change（参数：目标金额, 硬币面额）
    import functools  # 引入依赖

    n = len(coins)  # 把 长度(硬币面额) 存入 元素个数

    @functools.lru_cache(None)  # @functools.lru_cache(None)
    def dfs(i, c):  # 定义函数 dfs（参数：下标 i, 字符）
        if i < 0:  # 若 下标 i 小于 0
            return 1 if c == 0 else 0  # 返回 1 if 字符 等于 0 else 0
        if c < coins[i]:  # 若 字符 小于 硬币面额[下标 i]
            return dfs(i - 1, c)  # 返回 dfs(下标 i 减 1, 字符)
        return dfs(i - 1, c) + dfs(
            i, c - coins[i]
        )  # 返回 dfs(下标 i 减 1, 字符) 加 dfs(下标 i, 字符 减 硬币面额[下标 i])

    return dfs(n - 1, amount)  # 返回 dfs(元素个数 减 1, 目标金额)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(change(5, [1, 2, 5]))  # 打印输出
