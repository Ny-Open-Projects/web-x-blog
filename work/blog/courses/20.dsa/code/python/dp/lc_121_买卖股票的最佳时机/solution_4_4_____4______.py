# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849130
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    # 双指针（滑动窗口）
    left = 0  # 把 0 存入 左边界
    right = 0  # 把 0 存入 右边界
    maxProfit = 0  # 把 0 存入 maxProfit
    n = len(prices)  # 把 长度(价格序列) 存入 元素个数
    while right < n:  # 循环，直到不满足「右边界 小于 元素个数」
        if prices[right] < prices[left]:  # 若 价格序列[右边界] 小于 价格序列[左边界]
            left = right  # 把 右边界 存入 左边界
        else:  # 否则
            maxProfit = max(
                maxProfit, prices[right] - prices[left]
            )  # 把 取较大值 maxProfit, 价格序列[右边界] 减 价格序列[左边界]) 存入 maxProfit
        right += 1  # 右边界累加 1
    return maxProfit  # 返回 maxProfit


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # 打印输出
