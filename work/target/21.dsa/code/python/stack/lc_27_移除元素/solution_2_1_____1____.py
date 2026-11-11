# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def removeElement(nums, val):  # 定义函数 removeElement（参数：数组, 值）
    left = 0  # 把 0 存入 左边界
    right = len(nums)  # 把 长度(数组) 存入 右边界
    while left < right:  # 循环，直到不满足「左边界 小于 右边界」
        if nums[left] == val:  # 若 数组[左边界] 等于 值
            nums[left] = nums[right - 1]  # 把 数组[右边界 减 1] 写入 nums[left]
            right -= 1  # 右边界累减 1
        else:  # 否则
            left += 1  # 左边界累加 1
    return left  # 返回 左边界


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(removeElement([1, 2, 3], 1))  # 打印输出
