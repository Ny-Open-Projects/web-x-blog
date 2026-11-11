# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
# Greatest Slice - 方案2: Incremental (递增求和, O(n^2))
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def max_sub_array_ic(arr):  # 定义函数 max_sub_array_ic（参数：数组）
    n = len(arr)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    gs = arr[0]  # 把 数组[0] 存入 gs
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        s = 0  # 把 0 存入 字符串
        for j in range(i, n):  # 让 下标 j 从 下标 i 到 元素个数 遍历
            s += arr[j]  # 递增得到当前区间总和: O(1)
            if gs < s:  # 若 gs 小于 字符串
                gs = s  # 把 字符串 存入 gs
    return gs  # 返回 gs


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(max_sub_array_ic([-2, 1, -3, 4, -1, 2, 1]))  # 6
