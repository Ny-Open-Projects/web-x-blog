# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def nextGreaterElement(n):  # 定义函数 nextGreaterElement（参数：元素个数）
    MAX = 2147483647  # 把 2147483647 存入 MAX
    nums = list(str(n))  # 把 列表(str(元素个数)) 存入 数组

    # Find first decreasing position from right
    i = len(nums) - 2  # 把 长度(数组) 减 2 存入 下标 i
    while (
        i >= 0 and nums[i] >= nums[i + 1]
    ):  # 循环，直到不满足「下标 i 不低于 0 and 数组[下标 i] 不低于 数组[下标 i 加 1]」
        i -= 1  # 下标 i累减 1

    if i < 0:  # 若 下标 i 小于 0
        return -1  # 返回 减 1

    # Find smallest digit larger than nums[i] to the right
    j = len(nums) - 1  # 把 长度(数组) 减 1 存入 下标 j
    while nums[j] <= nums[i]:  # 循环，直到不满足「数组[下标 j] 不超过 数组[下标 i]」
        j -= 1  # 下标 j累减 1

    # Swap
    nums[i], nums[j] = nums[j], nums[i]  # 把 数组[下标 j], 数组[下标 i] 写入 nums[i], nums[j]

    # Reverse the suffix
    nums[i + 1 :] = nums[i + 1 :][::-1]  # 把 数组[下标 i 加 1:][:: 减 1] 写入 nums[i + 1:]

    # Check overflow
    ans = int("".join(nums))  # 把 int(''.join(数组)) 存入 答案
    return ans if ans <= MAX else -1  # 返回 答案 if 答案 不超过 MAX else 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(nextGreaterElement(1))  # 打印输出
