# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def numDistinct(s, t):  # 定义函数 numDistinct（参数：字符串, 另一字符串）
    # 递归（自顶向下，记忆化以保证可用）
    from functools import lru_cache  # from functools import lru_cache

    sLen = len(s)  # 把 长度(字符串) 存入 sLen
    tLen = len(t)  # 把 长度(另一字符串) 存入 tLen

    @lru_cache(None)  # @lru_cache(None)
    def helper(i, j):  # 定义函数 helper（参数：下标 i, 下标 j）
        if j < 0:  # 若 下标 j 小于 0
            return 1  # 返回 1
        if i < 0:  # 若 下标 i 小于 0
            return 0  # 返回 0
        if s[i] == t[j]:  # 若 字符串[下标 i] 等于 另一字符串[下标 j]
            return helper(i - 1, j) + helper(
                i - 1, j - 1
            )  # 返回 helper(下标 i 减 1, 下标 j) 加 helper(下标 i 减 1, 下标 j 减 1)
        return helper(i - 1, j)  # 返回 helper(下标 i 减 1, 下标 j)

    return helper(sLen - 1, tLen - 1)  # 返回 helper(sLen 减 1, tLen 减 1)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(numDistinct("rabbbit", "rabbit"))  # 打印输出
