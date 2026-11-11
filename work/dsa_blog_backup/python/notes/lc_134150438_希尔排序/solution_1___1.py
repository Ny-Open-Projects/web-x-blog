# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def shellSort(nums):  # 定义函数 shellSort（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    gap = n // 2  # 把 元素个数 除以 除以 2 存入 gap
    while gap > 0:  # 循环，直到不满足「gap 超过 0」
        for i in range(gap, n):  # 让 下标 i 从 gap 到 元素个数 遍历
            temp = nums[i]  # 把 数组[下标 i] 存入 临时变量
            j = i  # 把 下标 i 存入 下标 j
            while (
                j >= gap and nums[j - gap] > temp
            ):  # 循环，直到不满足「下标 j 不低于 gap and 数组[下标 j 减 gap] 超过 临时变量」
                nums[j] = nums[j - gap]  # 把 数组[下标 j 减 gap] 写入 nums[j]
                j -= gap  # 下标 j累减 gap
            nums[j] = temp  # 把 临时变量 写入 nums[j]
        gap //= 2  # 把 2 写入 gap //
    return nums  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(shellSort([1, 2, 3]))  # 打印输出
