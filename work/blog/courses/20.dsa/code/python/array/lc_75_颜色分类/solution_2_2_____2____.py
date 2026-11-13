# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370043
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortColors(nums):  # 定义函数 sortColors（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    p0, p1 = 0, 0  # 把 0, 0 写入 p0, p1
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        if nums[i] == 1:  # 若 数组[下标 i] 等于 1
            nums[i], nums[p1] = nums[p1], nums[i]  # 把 数组[p1], 数组[下标 i] 写入 nums[i], nums[p1]
            p1 += 1  # p1累加 1
        elif nums[i] == 0:  # 否则，若 数组[下标 i] 等于 0
            nums[i], nums[p0] = nums[p0], nums[i]  # 把 数组[p0], 数组[下标 i] 写入 nums[i], nums[p0]
            if p0 < p1:  # 若 p0 小于 p1
                nums[i], nums[p1] = nums[p1], nums[i]  # 把 数组[p1], 数组[下标 i] 写入 nums[i], nums[p1]
            p0 += 1  # p0累加 1
            p1 += 1  # p1累加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortColors([1, 2, 3]))  # 打印输出
