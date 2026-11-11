# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def gnome_sort_v2(arr):  # 定义函数 gnome_sort_v2（参数：数组）
    length = len(arr)  # 把 长度(数组) 存入 长度
    for k in range(1, length):  # 让 下标 k 从 1 到 长度 遍历
        i = k  # 把 下标 k 存入 下标 i
        while (
            i > 0 and arr[i - 1] > arr[i]
        ):  # 循环，直到不满足「下标 i 超过 0 and 数组[下标 i 减 1] 超过 数组[下标 i]」
            arr[i - 1], arr[i] = (
                arr[i],
                arr[i - 1],
            )  # 把 数组[下标 i], 数组[下标 i 减 1] 写入 arr[i - 1], arr[i]
            i -= 1  # 下标 i累减 1
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    arr = [5, 4, 3, 2, 1]  # 把 [5, 4, 3, 2, 1] 存入 数组
    gnome_sort_v2(arr)  # gnome_sort_v2(数组)
    print(arr)  # 打印输出
