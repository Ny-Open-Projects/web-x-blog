# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116938
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortedSquares(nums):  # 定义函数 sortedSquares（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    ans = [0] * n  # 把 [0] 乘 元素个数 存入 答案
    i, j, pos = 0, n - 1, n - 1  # 把 0, 元素个数 减 1, 元素个数 减 1 写入 i, j, pos
    while i <= j:  # 循环，直到不满足「下标 i 不超过 下标 j」
        if (
            nums[i] * nums[i] > nums[j] * nums[j]
        ):  # 若 数组[下标 i] 乘 数组[下标 i] 超过 数组[下标 j] 乘 数组[下标 j]
            ans[pos] = nums[i] * nums[i]  # 把 数组[下标 i] 乘 数组[下标 i] 写入 ans[pos]
            i += 1  # 下标 i累加 1
        else:  # 否则
            ans[pos] = nums[j] * nums[j]  # 把 数组[下标 j] 乘 数组[下标 j] 写入 ans[pos]
            j -= 1  # 下标 j累减 1
        pos -= 1  # pos累减 1
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortedSquares([1, 2, 3]))  # 打印输出
