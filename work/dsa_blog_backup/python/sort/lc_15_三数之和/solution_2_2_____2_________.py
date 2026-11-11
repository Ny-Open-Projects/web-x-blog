# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233688
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def threeSum(nums):  # 定义函数 threeSum（参数：数组）
    nums.sort()  # 排序
    result = []  # 把 [] 存入 结果
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    for i in range(n - 2):  # 让 下标 i 从 元素个数 减 2 遍历
        if i > 0 and nums[i] == nums[i - 1]:  # 若 下标 i 超过 0 and 数组[下标 i] 等于 数组[下标 i 减 1]
            continue  # 跳过本轮，进入下一次
        left, right = i + 1, n - 1  # 把 下标 i 加 1, 元素个数 减 1 写入 left, right
        while left < right:  # 循环，直到不满足「左边界 小于 右边界」
            total = (
                nums[i] + nums[left] + nums[right]
            )  # 把 数组[下标 i] 加 数组[左边界] 加 数组[右边界] 存入 总和
            if total < 0:  # 若 总和 小于 0
                left += 1  # 左边界累加 1
            elif total > 0:  # 否则，若 总和 超过 0
                right -= 1  # 右边界累减 1
            else:  # 否则
                result.append(
                    [nums[i], nums[left], nums[right]]
                )  # 把 [数组[下标 i], 数组[左边界], 数组[右边界]] 追加到列表尾部
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
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(threeSum([1, 2, 3]))  # 打印输出
