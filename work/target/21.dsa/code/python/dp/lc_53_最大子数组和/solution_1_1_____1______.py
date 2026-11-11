# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847570
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxSubArray(nums):  # 定义函数 maxSubArray（参数：数组）
    best = cur = nums[0]  # 把 当前值 赋值为 数组[0] 存入 当前最优
    for x in nums[1:]:  # 逐个取出 数组 的元素（x）
        cur = max(x, cur + x)  # 把 取较大值 x, 当前值 加 x) 存入 当前值
        best = max(best, cur)  # 把 取较大值 当前最优, 当前值) 存入 当前最优
    return best  # 返回 当前最优


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 打印输出
