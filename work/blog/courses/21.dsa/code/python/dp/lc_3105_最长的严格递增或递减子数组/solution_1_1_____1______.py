# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829935
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def longestMonotonicSubarray(nums):  # 定义函数 longestMonotonicSubarray（参数：数组）
    if not nums:  # 若 not 数组
        return 0  # 返回 0
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    ans = 1  # 把 1 存入 答案
    inc = 1  # 把 1 存入 inc
    dec = 1  # 把 1 存入 dec
    for i in range(1, n):  # 让 下标 i 从 1 到 元素个数 遍历
        if nums[i] > nums[i - 1]:  # 若 数组[下标 i] 超过 数组[下标 i 减 1]
            inc += 1  # inc累加 1
            dec = 1  # 把 1 存入 dec
        elif nums[i] < nums[i - 1]:  # 否则，若 数组[下标 i] 小于 数组[下标 i 减 1]
            dec += 1  # dec累加 1
            inc = 1  # 把 1 存入 inc
        else:  # 否则
            inc = 1  # 把 1 存入 inc
            dec = 1  # 把 1 存入 dec
        ans = max(ans, inc, dec)  # 把 取较大值 答案, inc, dec) 存入 答案
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(longestMonotonicSubarray([1, 4, 3, 3, 2]))  # 打印输出
