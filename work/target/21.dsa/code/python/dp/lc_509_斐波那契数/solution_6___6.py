# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fib(n):  # 定义函数 fib（参数：元素个数）
    # 数组 DP
    if n <= 1:  # 若 元素个数 不超过 1
        return n  # 返回 元素个数
    dp = [0, 1]  # 把 [0, 1] 存入 DP 表
    for i in range(2, n + 1):  # 让 下标 i 从 2 到 元素个数 加 1 遍历
        dp.append(dp[i - 1] + dp[i - 2])  # 把 DP 表[下标 i 减 1] 加 DP 表[下标 i 减 2] 追加到列表尾部
    return dp[n]  # 返回 DP 表[元素个数]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fib(5))  # 打印输出
