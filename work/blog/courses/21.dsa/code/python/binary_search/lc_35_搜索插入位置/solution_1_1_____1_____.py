# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def searchInsert(nums, target):  # 定义函数 searchInsert（参数：数组, 目标值）
    left, right = 0, len(nums)  # 把 0, 长度(数组) 写入 left, right
    while left < right:  # 循环，直到不满足「左边界 小于 右边界」
        mid = (left + right) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 中点
        if nums[mid] < target:  # 若 数组[中点] 小于 目标值
            left = mid + 1  # 把 中点 加 1 存入 左边界
        else:  # 否则
            right = mid  # 把 中点 存入 右边界
    return left  # 返回 左边界


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(searchInsert([1, 2, 3], 1))  # 打印输出
