# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def match_v1(P, T):  # 定义函数 match_v1（参数：P, T）
    """Brute-Force 模式匹配（版本1：主串指针回退）。
    返回模式 P 在文本 T 中首次出现的起始下标，未找到返回 -1。"""
    n, m = len(T), len(P)  # 把 长度(T), 长度(P) 写入 n, m
    i, j = 0, 0  # 把 0, 0 写入 i, j
    while j < m and i < n:  # 循环，直到不满足「下标 j 小于 映射表 and 下标 i 小于 元素个数」
        if T[i] == P[j]:  # 若 T[下标 i] 等于 P[下标 j]
            i += 1  # 下标 i累加 1
            j += 1  # 下标 j累加 1
        else:  # 否则
            i -= j - 1  # 主串回退到本次对齐的下一位置
            j = 0  # 把 0 存入 下标 j
    return i - j if j == m else -1  # 返回 下标 i 减 下标 j if 下标 j 等于 映射表 else 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    T = "now is the time for all good people to come"  # 把 'now is the time for all good people to come' 存入 T
    print('匹配 "people":', match_v1("people", T))  # 打印输出
    print('匹配 "good":', match_v1("good", T))  # 打印输出
    print('匹配 "xyz":', match_v1("xyz", T))  # 打印输出
