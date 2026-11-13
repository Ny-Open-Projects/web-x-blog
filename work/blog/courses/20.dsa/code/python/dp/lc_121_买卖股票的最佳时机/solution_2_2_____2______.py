# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849130
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    # 一次遍历
    minprice = float("inf")  # 把 float('inf') 存入 minprice
    maxprofit = 0  # 把 0 存入 maxprofit
    for price in prices:  # 逐个取出 价格序列 的元素（price）
        if price < minprice:  # 若 price 小于 minprice
            minprice = price  # 把 price 存入 minprice
        else:  # 否则
            maxprofit = max(
                maxprofit, price - minprice
            )  # 把 取较大值 maxprofit, price 减 minprice) 存入 maxprofit
    return maxprofit  # 返回 maxprofit


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # 打印输出
