# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def change(amount, coins):  # 定义函数 change（参数：目标金额, 硬币面额）
    f = [0] * (amount + 1)  # 把 [0] 乘 (目标金额 加 1) 存入 f
    f[0] = 1  # 把 1 写入 f[0]
    for x in coins:  # 逐个取出 硬币面额 的元素（x）
        for c in range(x, amount + 1):  # 让 字符 从 x 到 目标金额 加 1 遍历
            f[c] += f[c - x]  # f[c]累加 f[字符 减 x]
    return f[amount]  # 返回 f[目标金额]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(change(5, [1, 2, 5]))  # 打印输出
