# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245574
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fourSum(nums, target):  # 定义函数 fourSum（参数：数组, 目标值）
    nums.sort()  # 排序
    quadruplets = []  # 把 [] 存入 quadruplets
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    for i in range(n - 3):  # 让 下标 i 从 元素个数 减 3 遍历
        if i > 0 and nums[i] == nums[i - 1]:  # 若 下标 i 超过 0 and 数组[下标 i] 等于 数组[下标 i 减 1]
            continue  # 跳过本轮，进入下一次
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break  # 跳出循环
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue  # 跳过本轮，进入下一次
        for j in range(i + 1, n - 2):  # 让 下标 j 从 下标 i 加 1 到 元素个数 减 2 遍历
            if (
                j > i + 1 and nums[j] == nums[j - 1]
            ):  # 若 下标 j 超过 下标 i 加 1 and 数组[下标 j] 等于 数组[下标 j 减 1]
                continue  # 跳过本轮，进入下一次
            if (
                nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target
            ):  # 若 数组[下标 i] 加 数组[下标 j] 加 数组[下标 j 加 1] 加 数组[下标 j 加 2] 超过 目标值
                break  # 跳出循环
            if (
                nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target
            ):  # 若 数组[下标 i] 加 数组[下标 j] 加 数组[元素个数 减 2] 加 数组[元素个数 减 1] 小于 目标值
                continue  # 跳过本轮，进入下一次
            left, right = j + 1, n - 1  # 把 下标 j 加 1, 元素个数 减 1 写入 left, right
            while left < right:  # 循环，直到不满足「左边界 小于 右边界」
                s = (
                    nums[i] + nums[j] + nums[left] + nums[right]
                )  # 把 数组[下标 i] 加 数组[下标 j] 加 数组[左边界] 加 数组[右边界] 存入 字符串
                if s == target:  # 若 字符串 等于 目标值
                    quadruplets.append(
                        [nums[i], nums[j], nums[left], nums[right]]
                    )  # 把 [数组[下标 i], 数组[下标 j], 数组[左边界], 数组[右边界]] 追加到列表尾部
                    while (
                        left < right and nums[left] == nums[left + 1]
                    ):  # 循环，直到不满足「左边界 小于 右边界 and 数组[左边界] 等于 数组[左边界 加 1]」
                        left += 1  # 左边界累加 1
                    while (
                        left < right and nums[right] == nums[right - 1]
                    ):  # 循环，直到不满足「左边界 小于 右边界 and 数组[右边界] 等于 数组[右边界 减 1]」
                        right -= 1  # 右边界累减 1
                    left += 1  # 左边界累加 1
                    right -= 1  # 右边界累减 1
                elif s < target:  # 否则，若 字符串 小于 目标值
                    left += 1  # 左边界累加 1
                else:  # 否则
                    right -= 1  # 右边界累减 1
    return quadruplets  # 返回 quadruplets


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fourSum([1, 2, 3], 1))  # 打印输出
