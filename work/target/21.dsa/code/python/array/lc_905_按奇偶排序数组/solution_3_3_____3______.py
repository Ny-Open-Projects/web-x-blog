# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145588341
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortArrayByParity(nums):  # 定义函数 sortArrayByParity（参数：数组）
    left, right = 0, len(nums) - 1  # 把 0, 长度(数组) 减 1 写入 left, right
    while left < right:  # 循环，直到不满足「左边界 小于 右边界」
        while (
            left < right and nums[left] % 2 == 0
        ):  # 循环，直到不满足「左边界 小于 右边界 and 数组[左边界] 对…取模 2 等于 0」
            left += 1  # 左边界累加 1
        while (
            left < right and nums[right] % 2 == 1
        ):  # 循环，直到不满足「左边界 小于 右边界 and 数组[右边界] 对…取模 2 等于 1」
            right -= 1  # 右边界累减 1
        if left < right:  # 若 左边界 小于 右边界
            nums[left], nums[right] = (
                nums[right],
                nums[left],
            )  # 把 数组[右边界], 数组[左边界] 写入 nums[left], nums[right]
            left += 1  # 左边界累加 1
            right -= 1  # 右边界累减 1
    return nums  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortArrayByParity([1, 2, 3]))  # 打印输出
