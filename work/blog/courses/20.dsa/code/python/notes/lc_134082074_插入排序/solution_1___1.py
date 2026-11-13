# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def insertionSort(nums):  # 定义函数 insertionSort（参数：数组）
    for i in range(1, len(nums)):  # 让 下标 i 从 1 到 长度(数组 遍历
        key = nums[i]  # 把 数组[下标 i] 存入 key
        j = i - 1  # 把 下标 i 减 1 存入 下标 j
        while j >= 0 and nums[j] > key:  # 循环，直到不满足「下标 j 不低于 0 and 数组[下标 j] 超过 key」
            nums[j + 1] = nums[j]  # 把 数组[下标 j] 写入 nums[j + 1]
            j -= 1  # 下标 j累减 1
        nums[j + 1] = key  # 把 key 写入 nums[j + 1]
    return nums  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(insertionSort([1, 2, 3]))  # 打印输出
