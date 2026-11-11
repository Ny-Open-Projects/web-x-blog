# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116601
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def moveZeroes(nums):  # 定义函数 moveZeroes（参数：数组）
    left = 0  # 把 0 存入 左边界
    for right in range(len(nums)):  # 让 右边界 从 长度(数组 遍历
        if nums[right] != 0:  # 若 数组[右边界] 不等于 0
            nums[left], nums[right] = (
                nums[right],
                nums[left],
            )  # 把 数组[右边界], 数组[左边界] 写入 nums[left], nums[right]
            left += 1  # 左边界累加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(moveZeroes([1, 2, 3]))  # 打印输出
