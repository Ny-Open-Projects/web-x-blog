# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853482
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices, fee):  # 定义函数 maxProfit（参数：价格序列, fee）
    cash = 0  # 把 0 存入 cash
    hold = -prices[0]  # 把 减 价格序列[0] 存入 hold
    for i in range(1, len(prices)):  # 让 下标 i 从 1 到 长度(价格序列 遍历
        cash = max(
            cash, hold + prices[i] - fee
        )  # 把 取较大值 cash, hold 加 价格序列[下标 i] 减 fee) 存入 cash
        hold = max(hold, cash - prices[i])  # 把 取较大值 hold, cash 减 价格序列[下标 i]) 存入 hold
    return cash  # 返回 cash


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([1, 3, 2, 8, 4, 9], 2))  # 打印输出
