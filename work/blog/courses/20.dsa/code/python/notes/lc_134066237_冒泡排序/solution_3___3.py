# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def bubbleSort(nums):  # 定义函数 bubbleSort（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        swapped = False  # 把 False 存入 swapped
        for j in range(0, n - i - 1):  # 让 下标 j 从 0 到 元素个数 减 下标 i 减 1 遍历
            if nums[j] > nums[j + 1]:  # 若 数组[下标 j] 超过 数组[下标 j 加 1]
                nums[j], nums[j + 1] = (
                    nums[j + 1],
                    nums[j],
                )  # 把 数组[下标 j 加 1], 数组[下标 j] 写入 nums[j], nums[j + 1]
                swapped = True  # 把 True 存入 swapped
        if not swapped:  # 若 not swapped
            break  # 跳出循环
    return nums  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(bubbleSort([1, 2, 3]))  # 打印输出
