# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116938
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortedSquares(nums):  # 定义函数 sortedSquares（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    ans = []  # 把 [] 存入 答案
    negative = -1  # 把 减 1 存入 negative
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        if nums[i] < 0:  # 若 数组[下标 i] 小于 0
            negative = i  # 把 下标 i 存入 negative
    i, j = negative, negative + 1  # 把 negative, negative 加 1 写入 i, j
    while i >= 0 or j < n:  # 循环，直到不满足「下标 i 不低于 0 or 下标 j 小于 元素个数」
        if i < 0:  # 若 下标 i 小于 0
            ans.append(nums[j] * nums[j])  # 把 数组[下标 j] 乘 数组[下标 j] 追加到列表尾部
            j += 1  # 下标 j累加 1
        elif j == n:  # 否则，若 下标 j 等于 元素个数
            ans.append(nums[i] * nums[i])  # 把 数组[下标 i] 乘 数组[下标 i] 追加到列表尾部
            i -= 1  # 下标 i累减 1
        elif (
            nums[i] * nums[i] < nums[j] * nums[j]
        ):  # 否则，若 数组[下标 i] 乘 数组[下标 i] 小于 数组[下标 j] 乘 数组[下标 j]
            ans.append(nums[i] * nums[i])  # 把 数组[下标 i] 乘 数组[下标 i] 追加到列表尾部
            i -= 1  # 下标 i累减 1
        else:  # 否则
            ans.append(nums[j] * nums[j])  # 把 数组[下标 j] 乘 数组[下标 j] 追加到列表尾部
            j += 1  # 下标 j累加 1
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortedSquares([1, 2, 3]))  # 打印输出
