# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def removeDuplicates(nums):  # 定义函数 removeDuplicates（参数：数组）
    if not nums:  # 若 not 数组
        return 0  # 返回 0
    slow = 0  # 把 0 存入 慢指针
    for fast in range(1, len(nums)):  # 让 快指针 从 1 到 长度(数组 遍历
        if nums[fast] != nums[slow]:  # 若 数组[快指针] 不等于 数组[慢指针]
            slow += 1  # 慢指针累加 1
            nums[slow] = nums[fast]  # 把 数组[快指针] 写入 nums[slow]
    return slow + 1  # 返回 慢指针 加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(removeDuplicates([1, 2, 3]))  # 打印输出
