# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def binarySearch(arr, target):  # 定义函数 binarySearch（参数：数组, 目标值）
    """二分查找（减治策略）：在有序数组 arr 中查找 target，返回下标，未找到返回 -1。"""
    left, right = 0, len(arr) - 1  # 把 0, 长度(数组) 减 1 写入 left, right
    while left <= right:  # 循环，直到不满足「左边界 不超过 右边界」
        mid = (left + right) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 中点
        if arr[mid] == target:  # 若 数组[中点] 等于 目标值
            return mid  # 返回 中点
        if arr[mid] < target:  # 若 数组[中点] 小于 目标值
            left = mid + 1  # 把 中点 加 1 存入 左边界
        else:  # 否则
            right = mid - 1  # 把 中点 减 1 存入 右边界
    return -1  # 返回 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(binarySearch([1, 3, 5, 7, 9], 5))  # 打印输出
    print(binarySearch([1, 3, 5, 7, 9], 4))  # 打印输出
