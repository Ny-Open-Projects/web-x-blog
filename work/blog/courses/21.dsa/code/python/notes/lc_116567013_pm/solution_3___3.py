# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def build_next(P):  # 定义函数 build_next（参数：P）
    """构造 KMP 的 next 失效函数（look-up table）。"""
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


def kmp_match(P, T):  # 定义函数 kmp_match（参数：P, T）
    """KMP 模式匹配：借助 next 表在失配时大步跳跃，最坏 O(n)。"""
    N = build_next(P)  # 把 build_next(P) 存入 N
    n, m = len(T), len(P)  # 把 长度(T), 长度(P) 写入 n, m
    i, j = 0, 0  # 把 0, 0 写入 i, j
    while j < m and i < n:  # 循环，直到不满足「下标 j 小于 映射表 and 下标 i 小于 元素个数」
        if j < 0 or T[i] == P[j]:  # 若 下标 j 小于 0 or T[下标 i] 等于 P[下标 j]
            i += 1  # 下标 i累加 1
            j += 1  # 下标 j累加 1
        else:  # 否则
            j = N[j]  # 把 N[下标 j] 存入 下标 j
    return i - j if j == m else -1  # 返回 下标 i 减 下标 j if 下标 j 等于 映射表 else 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    T = "now is the time for all good people to come"  # 把 'now is the time for all good people to come' 存入 T
    print('KMP 匹配 "people":', kmp_match("people", T))  # 打印输出
    print('KMP 匹配 "all":', kmp_match("all", T))  # 打印输出
