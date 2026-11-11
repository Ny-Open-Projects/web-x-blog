# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134633617
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    # 动态规划：cash 表示不持股时的最大利润，hold 表示持股时的最大利润
    cash = 0  # 把 0 存入 cash
    hold = -prices[0] if prices else 0  # 把 减 价格序列[0] if 价格序列 else 0 存入 hold
    for price in prices:  # 逐个取出 价格序列 的元素（price）
        cash = max(cash, hold + price)  # 把 取较大值 cash, hold 加 price) 存入 cash
        hold = max(hold, cash - price)  # 把 取较大值 hold, cash 减 price) 存入 hold
    return cash  # 返回 cash


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # 打印输出
