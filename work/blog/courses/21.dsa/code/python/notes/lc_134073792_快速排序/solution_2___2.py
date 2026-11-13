# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def partition(nums, low, high):  # 定义函数 partition（参数：数组, low, high）
    pivot = nums[high]  # 把 数组[high] 存入 pivot
    i = low - 1  # 把 low 减 1 存入 下标 i
    for j in range(low, high):  # 让 下标 j 从 low 到 high 遍历
        if nums[j] <= pivot:  # 若 数组[下标 j] 不超过 pivot
            i += 1  # 下标 i累加 1
            nums[i], nums[j] = nums[j], nums[i]  # 把 数组[下标 j], 数组[下标 i] 写入 nums[i], nums[j]
    nums[i + 1], nums[high] = (
        nums[high],
        nums[i + 1],
    )  # 把 数组[high], 数组[下标 i 加 1] 写入 nums[i + 1], nums[high]
    return i + 1  # 返回 下标 i 加 1


def quickSort(nums, low=0, high=None):  # 定义函数 quickSort（参数：数组, low 赋值为 0, high 赋值为 None）
    if high is None:  # 若 high is None
        high = len(nums) - 1  # 把 长度(数组) 减 1 存入 high
    if low < high:  # 若 low 小于 high
        pi = partition(nums, low, high)  # 把 partition(数组, low, high) 存入 pi
        quickSort(nums, low, pi - 1)  # quickSort(数组, low, pi 减 1)
        quickSort(nums, pi + 1, high)  # quickSort(数组, pi 加 1, high)
    return nums  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(quickSort([3, 1, 2, 5, 4]))  # 打印输出
