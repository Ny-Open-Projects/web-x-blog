# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134633617
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    # 峰谷法：在连续下降段结束后于谷底买入，连续上升段结束后于峰顶卖出
    n = len(prices)  # 把 长度(价格序列) 存入 元素个数
    if n < 2:  # 若 元素个数 小于 2
        return 0  # 返回 0
    i = 0  # 把 0 存入 下标 i
    profit = 0  # 把 0 存入 profit
    while i < n - 1:  # 循环，直到不满足「下标 i 小于 元素个数 减 1」
        while (
            i < n - 1 and prices[i] >= prices[i + 1]
        ):  # 循环，直到不满足「下标 i 小于 元素个数 减 1 and 价格序列[下标 i] 不低于 价格序列[下标 i 加 1]」
            i += 1  # 下标 i累加 1
        valley = prices[i]  # 把 价格序列[下标 i] 存入 valley
        while (
            i < n - 1 and prices[i] <= prices[i + 1]
        ):  # 循环，直到不满足「下标 i 小于 元素个数 减 1 and 价格序列[下标 i] 不超过 价格序列[下标 i 加 1]」
            i += 1  # 下标 i累加 1
        peak = prices[i]  # 把 价格序列[下标 i] 存入 peak
        profit += peak - valley  # profit累加 peak 减 valley
    return profit  # 返回 profit


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # 打印输出
