# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849130
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    if len(prices) == 0:
        return 0  # 若 长度(价格序列) 等于 0: return 0
    pre = prices[0]  # 把 价格序列[0] 存入 前缀和
    ans = 0  # 把 0 存入 答案
    for i in range(0, len(prices)):  # 让 下标 i 从 0 到 长度(价格序列 遍历
        ans = max(ans, prices[i] - pre)  # 把 取较大值 答案, 价格序列[下标 i] 减 前缀和) 存入 答案
        pre = min(pre, prices[i])  # 把 取较小值 前缀和, 价格序列[下标 i]) 存入 前缀和
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([1, 2, 3]))  # 打印输出
