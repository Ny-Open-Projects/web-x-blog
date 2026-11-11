# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853675
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minCostClimbingStairs(cost):  # 定义函数 minCostClimbingStairs（参数：cost）
    n = len(cost)  # 把 长度(cost) 存入 元素个数
    prev2 = cost[0]  # 把 cost[0] 存入 prev2
    prev1 = cost[1]  # 把 cost[1] 存入 prev1
    for i in range(2, n):  # 让 下标 i 从 2 到 元素个数 遍历
        cur = min(prev1, prev2) + cost[i]  # 把 取较小值 prev1, prev2) 加 cost[下标 i] 存入 当前值
        prev2 = prev1  # 把 prev1 存入 prev2
        prev1 = cur  # 把 当前值 存入 prev1
    return min(prev1, prev2)  # 返回 取较小值 prev1, prev2)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minCostClimbingStairs([10, 15, 20]))  # 打印输出
