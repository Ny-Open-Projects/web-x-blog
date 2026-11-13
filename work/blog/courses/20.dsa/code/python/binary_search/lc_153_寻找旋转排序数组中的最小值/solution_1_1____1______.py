# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findMin(nums):  # 定义函数 findMin（参数：数组）
    low = 0  # 把 0 存入 low
    high = len(nums) - 1  # 把 长度(数组) 减 1 存入 high
    while low < high:  # 循环，直到不满足「low 小于 high」
        pivot = low + int((high - low) / 2)  # 把 low 加 int((high 减 low) 除以 2) 存入 pivot
        if nums[pivot] < nums[high]:  # 若 数组[pivot] 小于 数组[high]
            high = pivot  # 把 pivot 存入 high
        else:  # 否则
            low = pivot + 1  # 把 pivot 加 1 存入 low
    return nums[low]  # 返回 数组[low]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findMin([1, 2, 3]))  # 打印输出
