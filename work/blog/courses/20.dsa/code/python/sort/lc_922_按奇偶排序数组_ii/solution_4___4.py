# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortArrayByParityII(nums):  # 定义函数 sortArrayByParityII（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    j = 1  # 把 1 存入 下标 j
    for i in range(0, n, 2):  # 让 下标 i 从 0 到 元素个数 到 2 遍历
        if nums[i] & 1:  # 若 数组[下标 i] 按位与 1
            while nums[j] & 1:  # 循环，直到不满足「数组[下标 j] 按位与 1」
                j += 2  # 下标 j累加 2
            nums[i], nums[j] = nums[j], nums[i]  # 把 数组[下标 j], 数组[下标 i] 写入 nums[i], nums[j]
    return nums  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortArrayByParityII([4, 2, 5, 7]))  # 打印输出
    print(sortArrayByParityII([2, 3]))  # 打印输出
