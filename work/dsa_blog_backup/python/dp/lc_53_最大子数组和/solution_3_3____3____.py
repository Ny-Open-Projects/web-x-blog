# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847570
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxSubArray(nums):  # 定义函数 maxSubArray（参数：数组）
    def dc(left, right):  # 定义函数 dc（参数：左边界, 右边界）
        if left == right:  # 若 左边界 等于 右边界
            return nums[left]  # 返回 数组[左边界]
        mid = (left + right) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 中点
        left_sum = dc(left, mid)  # 把 dc(左边界, 中点) 存入 left_sum
        right_sum = dc(mid + 1, right)  # 把 dc(中点 加 1, 右边界) 存入 right_sum
        cross = nums[mid]  # 把 数组[中点] 存入 cross
        cur = nums[mid]  # 把 数组[中点] 存入 当前值
        for i in range(mid - 1, left - 1, -1):  # 让 下标 i 从 中点 减 1 到 左边界 减 1 到 减 1 遍历
            cur += nums[i]  # 当前值累加 数组[下标 i]
            cross = max(cross, cur)  # 把 取较大值 cross, 当前值) 存入 cross
        cur = cross  # 把 cross 存入 当前值
        for i in range(mid + 1, right + 1):  # 让 下标 i 从 中点 加 1 到 右边界 加 1 遍历
            cur += nums[i]  # 当前值累加 数组[下标 i]
            cross = max(cross, cur)  # 把 取较大值 cross, 当前值) 存入 cross
        return max(left_sum, right_sum, cross)  # 返回 取较大值 left_sum, right_sum, cross)

    return dc(0, len(nums) - 1)  # 返回 dc(0, 长度(数组) 减 1)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 打印输出
