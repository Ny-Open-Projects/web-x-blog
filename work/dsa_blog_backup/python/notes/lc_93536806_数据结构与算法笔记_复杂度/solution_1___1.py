# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def linear_search(arr, target):  # 定义函数 linear_search（参数：数组, 目标值）
    # 顺序查找：最坏时间复杂度 O(n)
    for i in range(len(arr)):  # 让 下标 i 从 长度(数组 遍历
        if arr[i] == target:  # 若 数组[下标 i] 等于 目标值
            return i  # 返回 下标 i
    return -1  # 返回 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [3, 1, 4, 1, 5, 9, 2, 6]  # 把 [3, 1, 4, 1, 5, 9, 2, 6] 存入 数组
    print(linear_search(arr, 5))  # 4
    print(linear_search(arr, 7))  # -1
