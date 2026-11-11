# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minSubArrayLen(target, nums):  # 定义函数 minSubArrayLen（参数：目标值, 数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    ans = float("inf")  # 把 float('inf') 存入 答案
    start = end = 0  # 把 终点 赋值为 0 存入 起点
    total = 0  # 把 0 存入 总和
    while end < n:  # 循环，直到不满足「终点 小于 元素个数」
        total += nums[end]  # 总和累加 数组[终点]
        while total >= target:  # 循环，直到不满足「总和 不低于 目标值」
            ans = min(ans, end - start + 1)  # 把 取较小值 答案, 终点 减 起点 加 1) 存入 答案
            total -= nums[start]  # 总和累减 数组[起点]
            start += 1  # 起点累加 1
        end += 1  # 终点累加 1
    return ans if ans != float("inf") else 0  # 返回 答案 if 答案 不等于 float('inf') else 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minSubArrayLen(1, [1, 2, 3]))  # 打印输出
