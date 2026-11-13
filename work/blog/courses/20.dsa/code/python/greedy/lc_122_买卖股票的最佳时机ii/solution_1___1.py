# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134633617
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    profit = 0  # 把 0 存入 profit
    for i in range(1, len(prices)):  # 让 下标 i 从 1 到 长度(价格序列 遍历
        if prices[i] > prices[i - 1]:  # 若 价格序列[下标 i] 超过 价格序列[下标 i 减 1]
            profit += prices[i] - prices[i - 1]  # profit累加 价格序列[下标 i] 减 价格序列[下标 i 减 1]
    return profit  # 返回 profit


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([1, 2, 3]))  # 打印输出
