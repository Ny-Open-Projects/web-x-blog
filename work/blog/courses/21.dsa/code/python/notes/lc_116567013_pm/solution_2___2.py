# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def match_v2(P, T):  # 定义函数 match_v2（参数：P, T）
    """Brute-Force 模式匹配（版本2：双循环对齐）。每次对齐后用内层循环逐字符比较。"""
    n, m = len(T), len(P)  # 把 长度(T), 长度(P) 写入 n, m
    for i in range(n - m + 1):  # 让 下标 i 从 元素个数 减 映射表 加 1 遍历
        j = 0  # 把 0 存入 下标 j
        while (
            j < m and T[i + j] == P[j]
        ):  # 循环，直到不满足「下标 j 小于 映射表 and T[下标 i 加 下标 j] 等于 P[下标 j]」
            j += 1  # 下标 j累加 1
        if j == m:  # 若 下标 j 等于 映射表
            return i  # 返回 下标 i
    return -1  # 返回 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    T = "now is the time for all good people to come"  # 把 'now is the time for all good people to come' 存入 T
    print('匹配 "people":', match_v2("people", T))  # 打印输出
    print('匹配 "time":', match_v2("time", T))  # 打印输出
