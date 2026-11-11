# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660487
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def climbStairs(n):  # 定义函数 climbStairs（参数：元素个数）
    # 两个变量（空间优化）
    if n == 1:  # 若 元素个数 等于 1
        return 1  # 返回 1
    dp0 = 1  # 把 1 存入 dp0
    dp1 = 1  # 把 1 存入 dp1
    for i in range(2, n + 1):  # 让 下标 i 从 2 到 元素个数 加 1 遍历
        tmp = dp0  # 把 dp0 存入 临时变量
        dp0 = dp1  # 把 dp1 存入 dp0
        dp1 += tmp  # dp1累加 临时变量
    return dp1  # 返回 dp1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(climbStairs(5))  # 打印输出
