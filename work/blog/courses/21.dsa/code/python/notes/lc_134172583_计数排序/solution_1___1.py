# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def countSort(nums):  # 定义函数 countSort（参数：数组）
    if not nums:  # 若 not 数组
        return nums  # 返回 数组
    max_val = max(nums)  # 把 取较大值 数组) 存入 max_val
    min_val = min(nums)  # 把 取较小值 数组) 存入 min_val
    range_val = max_val - min_val + 1  # 把 max_val 减 min_val 加 1 存入 range_val
    count = [0] * range_val  # 把 [0] 乘 range_val 存入 计数
    output = [0] * len(nums)  # 把 [0] 乘 长度(数组) 存入 输出
    for num in nums:  # 逐个取出 数组 的元素（num）
        count[num - min_val] += 1  # 把 1 写入 count[num - min_val] +
    for i in range(1, range_val):  # 让 下标 i 从 1 到 range_val 遍历
        count[i] += count[i - 1]  # count[i]累加 计数[下标 i 减 1]
    for i in range(len(nums) - 1, -1, -1):  # 让 下标 i 从 长度(数组) 减 1 倒数回去（每步减 1）
        output[count[nums[i] - min_val] - 1] = nums[
            i
        ]  # 把 数组[下标 i] 写入 output[count[nums[i] - min_val] - 1]
        count[nums[i] - min_val] -= 1  # 把 1 写入 count[nums[i] - min_val] -
    return output  # 返回 输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(countSort([1, 2, 3]))  # 打印输出
