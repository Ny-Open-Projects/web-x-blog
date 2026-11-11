# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370043
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortColors(nums):  # 定义函数 sortColors（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    p0, p2 = 0, n - 1  # 把 0, 元素个数 减 1 写入 p0, p2
    i = 0  # 把 0 存入 下标 i
    while i <= p2:  # 循环，直到不满足「下标 i 不超过 p2」
        while i <= p2 and nums[i] == 2:  # 循环，直到不满足「下标 i 不超过 p2 and 数组[下标 i] 等于 2」
            nums[i], nums[p2] = nums[p2], nums[i]  # 把 数组[p2], 数组[下标 i] 写入 nums[i], nums[p2]
            p2 -= 1  # p2累减 1
        if nums[i] == 0:  # 若 数组[下标 i] 等于 0
            nums[i], nums[p0] = nums[p0], nums[i]  # 把 数组[p0], 数组[下标 i] 写入 nums[i], nums[p0]
            p0 += 1  # p0累加 1
        i += 1  # 下标 i累加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortColors([1, 2, 3]))  # 打印输出
