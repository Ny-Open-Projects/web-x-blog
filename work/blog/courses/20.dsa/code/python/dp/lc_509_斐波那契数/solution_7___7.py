# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fib(n):  # 定义函数 fib（参数：元素个数）
    from functools import lru_cache  # from functools import lru_cache

    @lru_cache(None)  # @lru_cache(None)
    def dfs(x):  # 定义函数 dfs（参数：x）
        if x == 0:  # 若 x 等于 0
            return 0  # 返回 0
        if x == 1:  # 若 x 等于 1
            return 1  # 返回 1
        return dfs(x - 1) + dfs(x - 2)  # 返回 dfs(x 减 1) 加 dfs(x 减 2)

    return dfs(n)  # 返回 dfs(元素个数)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fib(10))  # 打印输出
