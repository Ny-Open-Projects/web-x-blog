# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831489
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minFlipsMonoIncr(s):  # 定义函数 minFlipsMonoIncr（参数：字符串）
    one = 0  # 把 0 存入 one
    dp = 0  # 把 0 存入 DP 表
    for c in s:  # 逐个取出 字符串 的元素（字符）
        if c == "0":  # 若 字符 等于 '0'
            dp = min(one, dp + 1)  # 把 取较小值 one, DP 表 加 1) 存入 DP 表
        else:  # 否则
            one += 1  # one累加 1
    return dp  # 返回 DP 表


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minFlipsMonoIncr("00110"))  # 打印输出
