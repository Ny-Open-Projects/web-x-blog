# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def quick_select(arr, k):  # 定义函数 quick_select（参数：数组, 下标 k）
    # 快速选择：返回 arr 中第 k 小元素（k 为 0-based 索引），平均 O(n)
    a = arr[:]  # 把 复制 数组 存入 数组

    def select(lo, hi, k):  # 定义函数 select（参数：左边界, 右边界, 下标 k）
        if lo == hi:  # 若 左边界 等于 右边界
            return a[lo]  # 返回 数组[左边界]
        pivot = a[hi]  # 把 数组[右边界] 存入 pivot
        i = lo  # 把 左边界 存入 下标 i
        for j in range(lo, hi):  # 让 下标 j 从 左边界 到 右边界 遍历
            if a[j] <= pivot:  # 若 数组[下标 j] 不超过 pivot
                a[i], a[j] = a[j], a[i]  # 把 数组[下标 j], 数组[下标 i] 写入 a[i], a[j]
                i += 1  # 下标 i累加 1
        a[i], a[hi] = a[hi], a[i]  # 把 数组[右边界], 数组[下标 i] 写入 a[i], a[hi]
        if i == k:  # 若 下标 i 等于 下标 k
            return a[i]  # 返回 数组[下标 i]
        elif i > k:  # 否则，若 下标 i 超过 下标 k
            return select(lo, i - 1, k)  # 返回 select(左边界, 下标 i 减 1, 下标 k)
        else:  # 否则
            return select(i + 1, hi, k)  # 返回 select(下标 i 加 1, 右边界, 下标 k)

    return select(0, len(a) - 1, k)  # 返回 select(0, 长度(数组) 减 1, 下标 k)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [3, 1, 4, 1, 5, 9, 2, 6]  # 把 [3, 1, 4, 1, 5, 9, 2, 6] 存入 数组
    print("第3小元素:", quick_select(arr, 2))  # 2
    print("中位数(第4小):", quick_select(arr, 3))  # 3
    s = sorted(arr)  # 把 sorted(数组) 存入 字符串
    print("校验:", s)  # 打印输出
