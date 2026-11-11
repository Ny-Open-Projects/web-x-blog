# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145115578
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def twoSum(numbers, target):  # 定义函数 twoSum（参数：numbers, 目标值）
    for i in range(len(numbers)):  # 让 下标 i 从 长度(numbers 遍历
        left, right = i + 1, len(numbers) - 1  # 把 下标 i 加 1, 长度(numbers) 减 1 写入 left, right
        while left <= right:  # 循环，直到不满足「左边界 不超过 右边界」
            mid = (left + right) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 中点
            if numbers[mid] == target - numbers[i]:  # 若 numbers[中点] 等于 目标值 减 numbers[下标 i]
                return [i + 1, mid + 1]  # 返回 [下标 i 加 1, 中点 加 1]
            elif numbers[mid] > target - numbers[i]:  # 否则，若 numbers[中点] 超过 目标值 减 numbers[下标 i]
                right = mid - 1  # 把 中点 减 1 存入 右边界
            else:  # 否则
                left = mid + 1  # 把 中点 加 1 存入 左边界
    return [-1, -1]  # 返回 [ 减 1, 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(twoSum([2, 7, 11, 15], 9))  # 打印输出
