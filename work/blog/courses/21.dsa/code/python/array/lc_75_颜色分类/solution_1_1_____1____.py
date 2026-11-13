# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370043
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortColors(nums):  # 定义函数 sortColors（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    ptr = 0  # 把 0 存入 ptr
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        if nums[i] == 0:  # 若 数组[下标 i] 等于 0
            nums[i], nums[ptr] = nums[ptr], nums[i]  # 把 数组[ptr], 数组[下标 i] 写入 nums[i], nums[ptr]
            ptr += 1  # ptr累加 1
    for i in range(ptr, n):  # 让 下标 i 从 ptr 到 元素个数 遍历
        if nums[i] == 1:  # 若 数组[下标 i] 等于 1
            nums[i], nums[ptr] = nums[ptr], nums[i]  # 把 数组[ptr], 数组[下标 i] 写入 nums[i], nums[ptr]
            ptr += 1  # ptr累加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortColors([1, 2, 3]))  # 打印输出
