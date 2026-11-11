# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def rob(nums):  # 定义函数 rob（参数：数组）
    length = len(nums)  # 把 长度(数组) 存入 长度
    if length == 1:  # 若 长度 等于 1
        return nums[0]  # 返回 数组[0]
    elif length == 2:  # 否则，若 长度 等于 2
        return max(nums[0], nums[1])  # 返回 取较大值 数组[0], 数组[1])

    def robRange(start, end):  # 定义函数 robRange（参数：起点, 终点）
        first = nums[start]  # 把 数组[起点] 存入 first
        second = max(nums[start], nums[start + 1])  # 把 取较大值 数组[起点], 数组[起点 加 1]) 存入 second
        for i in range(start + 2, end + 1):  # 让 下标 i 从 起点 加 2 到 终点 加 1 遍历
            temp = second  # 把 second 存入 临时变量
            second = max(first + nums[i], second)  # 把 取较大值 first 加 数组[下标 i], second) 存入 second
            first = temp  # 把 临时变量 存入 first
        return second  # 返回 second

    return max(
        robRange(0, length - 2), robRange(1, length - 1)
    )  # 返回 取较大值 robRange(0, 长度 减 2), robRange(1, 长度 减 1))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(rob([2, 3, 2]))  # 打印输出
