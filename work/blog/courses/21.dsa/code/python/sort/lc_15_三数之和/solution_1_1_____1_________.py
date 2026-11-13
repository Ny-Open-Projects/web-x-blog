# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233688
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def threeSum(nums):  # 定义函数 threeSum（参数：数组）
    nums.sort()  # 排序
    ans = []  # 把 [] 存入 答案
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    for first in range(n):  # 让 first 从 元素个数 遍历
        if (
            first > 0 and nums[first] == nums[first - 1]
        ):  # 若 first 超过 0 and 数组[first] 等于 数组[first 减 1]
            continue  # 跳过本轮，进入下一次
        third = n - 1  # 把 元素个数 减 1 存入 third
        target = -nums[first]  # 把 减 数组[first] 存入 目标值
        for second in range(first + 1, n):  # 让 second 从 first 加 1 到 元素个数 遍历
            if (
                second > first + 1 and nums[second] == nums[second - 1]
            ):  # 若 second 超过 first 加 1 and 数组[second] 等于 数组[second 减 1]
                continue  # 跳过本轮，进入下一次
            while (
                second < third and nums[second] + nums[third] > target
            ):  # 循环，直到不满足「second 小于 third and 数组[second] 加 数组[third] 超过 目标值」
                third -= 1  # third累减 1
            if second == third:  # 若 second 等于 third
                break  # 跳出循环
            if nums[second] + nums[third] == target:  # 若 数组[second] 加 数组[third] 等于 目标值
                ans.append(
                    [nums[first], nums[second], nums[third]]
                )  # 把 [数组[first], 数组[second], 数组[third]] 追加到列表尾部
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(threeSum([1, 2, 3]))  # 打印输出
