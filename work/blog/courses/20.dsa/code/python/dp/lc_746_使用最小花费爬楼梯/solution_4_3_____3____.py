# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853675
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minCostClimbingStairs(cost):  # 定义函数 minCostClimbingStairs（参数：cost）
    size = len(cost)  # 把 长度(cost) 存入 大小
    if size == 0:
        return 0  # 若 大小 等于 0: return 0
    if size == 1:
        return cost[0]  # 若 大小 等于 1: return cost[0]
    minCost = [0] * size  # 把 [0] 乘 大小 存入 minCost
    minCost[0] = cost[0]  # 把 cost[0] 写入 minCost[0]
    minCost[1] = cost[1]  # 把 cost[1] 写入 minCost[1]
    for i in range(2, size):  # 让 下标 i 从 2 到 大小 遍历
        minCost[i] = min(minCost[i - 1], minCost[i - 2]) + cost[i]
    return min(minCost[size - 1], minCost[size - 2])  # 返回 取较小值 minCost[大小 减 1], minCost[大小 减 2])


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minCostClimbingStairs([10, 15, 20]))  # 打印输出
