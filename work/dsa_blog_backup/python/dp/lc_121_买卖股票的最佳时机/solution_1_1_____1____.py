# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849130
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    # 暴力法
    n = len(prices)  # 把 长度(价格序列) 存入 元素个数
    maxprofit = 0  # 把 0 存入 maxprofit
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for j in range(i + 1, n):  # 让 下标 j 从 下标 i 加 1 到 元素个数 遍历
            profit = prices[j] - prices[i]  # 把 价格序列[下标 j] 减 价格序列[下标 i] 存入 profit
            if profit > maxprofit:  # 若 profit 超过 maxprofit
                maxprofit = profit  # 把 profit 存入 maxprofit
    return maxprofit  # 返回 maxprofit


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # 打印输出
