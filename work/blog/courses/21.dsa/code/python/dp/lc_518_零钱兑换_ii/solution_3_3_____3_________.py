# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def change(amount, coins):  # 定义函数 change（参数：目标金额, 硬币面额）
    n = len(coins)  # 把 长度(硬币面额) 存入 元素个数
    f = [
        [0] * (amount + 1) for _ in range(n + 1)
    ]  # 把 [[0] 乘 (目标金额 加 1) for _ in range(元素个数 加 1)] 存入 f
    f[0][0] = 1  # 把 1 写入 f[0][0]
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for c in range(amount + 1):  # 让 字符 从 目标金额 加 1 遍历
            if c < coins[i]:  # 若 字符 小于 硬币面额[下标 i]
                f[i + 1][c] = f[i][c]  # 把 f[下标 i][字符] 写入 f[i + 1][c]
            else:  # 否则
                f[i + 1][c] = (
                    f[i][c] + f[i + 1][c - coins[i]]
                )  # 把 f[下标 i][字符] 加 f[下标 i 加 1][字符 减 硬币面额[下标 i]] 写入 f[i + 1][c]
    return f[n][amount]  # 返回 f[元素个数][目标金额]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(change(5, [1, 2, 5]))  # 打印输出
