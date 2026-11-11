# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853675
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minCostClimbingStairs(cost):  # 定义函数 minCostClimbingStairs（参数：cost）
    minCost0 = 0  # 把 0 存入 minCost0
    minCost1 = min(cost[0], cost[1])  # 把 取较小值 cost[0], cost[1]) 存入 minCost1
    for i in range(2, len(cost)):  # 让 下标 i 从 2 到 长度(cost 遍历
        minCost = min(minCost1 + cost[i], minCost0 + cost[i - 1])
        [minCost0, minCost1] = [minCost1, minCost]  # 把 [minCost1, minCost] 写入 [minCost0, minCost1]
    return minCost1  # 返回 minCost1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minCostClimbingStairs([10, 15, 20]))  # 打印输出
