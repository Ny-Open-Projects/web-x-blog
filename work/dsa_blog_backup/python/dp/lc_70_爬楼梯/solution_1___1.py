# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660487
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def climbStairs(n):  # 定义函数 climbStairs（参数：元素个数）
    # 递归 + 记忆化
    from functools import lru_cache  # from functools import lru_cache

    @lru_cache(None)  # @lru_cache(None)
    def f(k):  # 定义函数 f（参数：下标 k）
        if k <= 1:  # 若 下标 k 不超过 1
            return 1  # 返回 1
        return f(k - 1) + f(k - 2)  # 返回 f(下标 k 减 1) 加 f(下标 k 减 2)

    return f(n)  # 返回 f(元素个数)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(climbStairs(5))  # 打印输出
