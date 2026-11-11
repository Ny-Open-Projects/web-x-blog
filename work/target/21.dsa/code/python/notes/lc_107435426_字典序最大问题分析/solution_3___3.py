# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def range_max(ele, i):  # 定义函数 range_max（参数：ele, 下标 i）
    """返回 ele[i:] 中的最大值（蛮力版中的核心查找步骤，方案 3）。"""
    mx = ele[i]  # 把 ele[下标 i] 存入 mx
    for j in range(i + 1, len(ele)):  # 让 下标 j 从 下标 i 加 1 到 长度(ele 遍历
        if ele[j] > mx:  # 若 ele[下标 j] 超过 mx
            mx = ele[j]  # 把 ele[下标 j] 存入 mx
    return mx  # 返回 mx


def suffix_max(ele):  # 定义函数 suffix_max（参数：ele）
    """返回后缀最大值数组 maxElement[i] = max(ele[i:])（线性预处理）。"""
    n = len(ele)  # 把 长度(ele) 存入 元素个数
    res = [0] * n  # 把 [0] 乘 元素个数 存入 结果
    res[n - 1] = ele[n - 1]  # 把 ele[元素个数 减 1] 写入 res[n - 1]
    for i in range(n - 2, -1, -1):  # 让 下标 i 从 元素个数 减 2 倒数回去（每步减 1）
        res[i] = max(res[i + 1], ele[i])  # 把 取较大值 结果[下标 i 加 1], ele[下标 i]) 写入 res[i]
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    ele = [4, 1, 3, 5, 2]  # 把 [4, 1, 3, 5, 2] 存入 ele
    print("range_max(ele, 0) =", range_max(ele, 0))  # 5
    print("suffix_max(ele)    =", suffix_max(ele))  # [5, 5, 5, 5, 2]
