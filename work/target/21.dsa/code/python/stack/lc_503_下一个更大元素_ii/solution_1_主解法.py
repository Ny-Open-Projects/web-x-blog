# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347297
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solve():  # 定义函数 solve（参数：无）
    """
    LeetCode 503. 下一个更大元素 II
    单调栈解法框架（环形数组）
    """

    pass  # pass


def nextGreaterElements(nums):  # 定义函数 nextGreaterElements（参数：数组）
    """
    找到环形数组中每个元素的下一个更大元素
    """
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    result = [-1] * n  # 把 [ 减 1] 乘 元素个数 存入 结果
    stack = []  # 把 [] 存入 栈

    # 遍历两圈（模拟环形）
    for i in range(2 * n):  # 让 下标 i 从 2 乘 元素个数 遍历
        num = nums[i % n]  # 把 数组[下标 i 对…取模 元素个数] 存入 num
        while stack and nums[stack[-1]] < num:  # 循环，直到不满足「栈 and 数组[栈[ 减 1]] 小于 num」
            idx = stack.pop()  # 把 栈 弹出 ) 存入 idx
            result[idx] = num  # 把 num 写入 result[idx]
        if i < n:  # 若 下标 i 小于 元素个数
            stack.append(i)  # 把 下标 i 追加到列表尾部

    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    nums = [1, 2, 1]  # 把 [1, 2, 1] 存入 数组
    print(nextGreaterElements(nums))  # 打印输出
