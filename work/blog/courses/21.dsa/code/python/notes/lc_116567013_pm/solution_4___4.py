# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def build_next(P):  # 定义函数 build_next（参数：P）
    """构造 KMP 的 next 表（单独呈现，对应 C++ buildNext）。"""
    m = len(P)  # 把 长度(P) 存入 映射表
    N = [-1] * m  # 把 [ 减 1] 乘 映射表 存入 N
    j, t = 0, -1  # 把 0, 减 1 写入 j, t
    while j < m - 1:  # 循环，直到不满足「下标 j 小于 映射表 减 1」
        if t < 0 or P[j] == P[t]:  # 若 另一字符串 小于 0 or P[下标 j] 等于 P[另一字符串]
            j += 1  # 下标 j累加 1
            t += 1  # 另一字符串累加 1
            N[j] = t  # 把 另一字符串 写入 N[j]
        else:  # 否则
            t = N[t]  # 把 N[另一字符串] 存入 另一字符串
    return N  # 返回 N


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    P = "ababaca"  # 把 'ababaca' 存入 P
    table = build_next(P)  # 把 build_next(P) 存入 table
    print("模式:", P)  # 打印输出
    print("next 表:", table)  # 打印输出
