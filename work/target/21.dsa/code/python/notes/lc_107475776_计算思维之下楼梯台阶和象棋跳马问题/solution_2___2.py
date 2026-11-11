# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def climb_stairs_count(h):  # 定义函数 climb_stairs_count（参数：h）
    # 下楼梯问题：每步可走 1/2/3 级（方案2，自底向上 DP / 递推计数）
    if h < 0:  # 若 h 小于 0
        return 0  # 返回 0
    if h == 0:  # 若 h 等于 0
        return 1  # 返回 1
    if h == 1:  # 若 h 等于 1
        return 1  # 返回 1
    if h == 2:  # 若 h 等于 2
        return 2  # 返回 2
    dp = [0] * (h + 1)  # 把 [0] 乘 (h 加 1) 存入 DP 表
    dp[0], dp[1], dp[2] = 1, 1, 2  # 把 1, 1, 2 写入 dp[0], dp[1], dp[2]
    for i in range(3, h + 1):  # 让 下标 i 从 3 到 h 加 1 遍历
        dp[i] = (
            dp[i - 1] + dp[i - 2] + dp[i - 3]
        )  # 把 DP 表[下标 i 减 1] 加 DP 表[下标 i 减 2] 加 DP 表[下标 i 减 3] 写入 dp[i]
    return dp[h]  # 返回 DP 表[h]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    for h in (4, 6, 10):  # for h in (4, 6, 10):
        print(f"台阶数 {h}，总方案数: {climb_stairs_count(h)}")  # 打印输出
