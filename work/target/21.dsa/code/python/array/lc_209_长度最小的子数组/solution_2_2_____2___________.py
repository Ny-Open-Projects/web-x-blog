# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minSubArrayLen(target, nums):  # 定义函数 minSubArrayLen（参数：目标值, 数组）
    import bisect  # 引入依赖

    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    ans = float("inf")  # 把 float('inf') 存入 答案
    sums = [0] * (n + 1)  # 把 [0] 乘 (元素个数 加 1) 存入 sums
    for i in range(1, n + 1):  # 让 下标 i 从 1 到 元素个数 加 1 遍历
        sums[i] = sums[i - 1] + nums[i - 1]  # 把 sums[下标 i 减 1] 加 数组[下标 i 减 1] 写入 sums[i]
    for i in range(1, n + 1):  # 让 下标 i 从 1 到 元素个数 加 1 遍历
        t = sums[i - 1] + target  # 把 sums[下标 i 减 1] 加 目标值 存入 另一字符串
        bound = bisect.bisect_left(sums, t)  # 把 bisect.bisect_left(sums, 另一字符串) 存入 bound
        if bound <= n:  # 若 bound 不超过 元素个数
            ans = min(ans, bound - (i - 1))  # 把 取较小值 答案, bound 减 (下标 i 减 1)) 存入 答案
    return ans if ans != float("inf") else 0  # 返回 答案 if 答案 不等于 float('inf') else 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minSubArrayLen(1, [1, 2, 3]))  # 打印输出
