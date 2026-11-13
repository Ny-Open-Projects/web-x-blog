# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def removeElement(nums, val):  # 定义函数 removeElement（参数：数组, 值）
    # Two-pointer from both ends, optimized for few deletions
    left, right = 0, len(nums) - 1  # 把 0, 长度(数组) 减 1 写入 left, right
    while left <= right:  # 循环，直到不满足「左边界 不超过 右边界」
        if nums[left] == val:  # 若 数组[左边界] 等于 值
            nums[left] = nums[right]  # 把 数组[右边界] 写入 nums[left]
            right -= 1  # 右边界累减 1
        else:  # 否则
            left += 1  # 左边界累加 1
    return left  # 返回 左边界


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(removeElement([1, 2, 3], 1))  # 打印输出
