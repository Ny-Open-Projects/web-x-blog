# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minSubArrayLen(target, nums):  # 定义函数 minSubArrayLen（参数：目标值, 数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    ans = float("inf")  # 把 float('inf') 存入 答案
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        s = 0  # 把 0 存入 字符串
        for j in range(i, n):  # 让 下标 j 从 下标 i 到 元素个数 遍历
            s += nums[j]  # 字符串累加 数组[下标 j]
            if s >= target:  # 若 字符串 不低于 目标值
                ans = min(ans, j - i + 1)  # 把 取较小值 答案, 下标 j 减 下标 i 加 1) 存入 答案
                break  # 跳出循环
    return ans if ans != float("inf") else 0  # 返回 答案 if 答案 不等于 float('inf') else 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minSubArrayLen(1, [1, 2, 3]))  # 打印输出
