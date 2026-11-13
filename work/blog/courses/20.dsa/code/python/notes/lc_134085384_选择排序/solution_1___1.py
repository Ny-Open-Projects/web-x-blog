# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def selectionSort(nums):  # 定义函数 selectionSort（参数：数组）
    for i in range(len(nums)):  # 让 下标 i 从 长度(数组 遍历
        min_idx = i  # 把 下标 i 存入 min_idx
        for j in range(i + 1, len(nums)):  # 让 下标 j 从 下标 i 加 1 到 长度(数组 遍历
            if nums[j] < nums[min_idx]:  # 若 数组[下标 j] 小于 数组[min_idx]
                min_idx = j  # 把 下标 j 存入 min_idx
        nums[i], nums[min_idx] = (
            nums[min_idx],
            nums[i],
        )  # 把 数组[min_idx], 数组[下标 i] 写入 nums[i], nums[min_idx]
    return nums  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(selectionSort([1, 2, 3]))  # 打印输出
