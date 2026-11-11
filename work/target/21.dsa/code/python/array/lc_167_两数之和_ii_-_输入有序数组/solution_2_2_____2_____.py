# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145115578
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def twoSum(numbers, target):  # 定义函数 twoSum（参数：numbers, 目标值）
    left, right = 0, len(numbers) - 1  # 把 0, 长度(numbers) 减 1 写入 left, right
    while left < right:  # 循环，直到不满足「左边界 小于 右边界」
        s = numbers[left] + numbers[right]  # 把 numbers[左边界] 加 numbers[右边界] 存入 字符串
        if s == target:  # 若 字符串 等于 目标值
            return [left + 1, right + 1]  # 返回 [左边界 加 1, 右边界 加 1]
        elif s < target:  # 否则，若 字符串 小于 目标值
            left += 1  # 左边界累加 1
        else:  # 否则
            right -= 1  # 右边界累减 1
    return [-1, -1]  # 返回 [ 减 1, 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(twoSum([2, 7, 11, 15], 9))  # 打印输出
