# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solution():  # 定义函数 solution（参数：无）
    nums = [3, 2, 2, 3]  # 把 [3, 2, 2, 3] 存入 数组
    val = 3  # 把 3 存入 值
    k = removeElement(nums, val)  # 把 removeElement(数组, 值) 存入 下标 k
    print(k, nums[:k])  # 打印输出


def removeElement(nums, val):  # 定义函数 removeElement（参数：数组, 值）
    left = 0  # 把 0 存入 左边界
    for right in range(len(nums)):  # 让 右边界 从 长度(数组 遍历
        if nums[right] != val:  # 若 数组[右边界] 不等于 值
            nums[left] = nums[right]  # 把 数组[右边界] 写入 nums[left]
            left += 1  # 左边界累加 1
    return left  # 返回 左边界


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(solution())  # 打印输出
