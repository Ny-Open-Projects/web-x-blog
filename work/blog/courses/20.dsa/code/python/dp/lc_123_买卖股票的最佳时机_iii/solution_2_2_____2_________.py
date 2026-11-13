# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849793
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    if not prices:  # 若 not 价格序列
        return 0  # 返回 0
    buy1 = -prices[0]  # 把 减 价格序列[0] 存入 buy1
    sell1 = 0  # 把 0 存入 sell1
    buy2 = -prices[0]  # 把 减 价格序列[0] 存入 buy2
    sell2 = 0  # 把 0 存入 sell2
    for p in prices[1:]:  # 逐个取出 价格序列 的元素（节点）
        buy1 = max(buy1, -p)  # 把 取较大值 buy1, 减 节点) 存入 buy1
        sell1 = max(sell1, buy1 + p)  # 把 取较大值 sell1, buy1 加 节点) 存入 sell1
        buy2 = max(buy2, sell1 - p)  # 把 取较大值 buy2, sell1 减 节点) 存入 buy2
        sell2 = max(sell2, buy2 + p)  # 把 取较大值 sell2, buy2 加 节点) 存入 sell2
    return sell2  # 返回 sell2


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))  # 打印输出
