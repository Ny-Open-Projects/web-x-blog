# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344295
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def containsDuplicate(nums):  # 定义函数 containsDuplicate（参数：数组）
    return len(nums) != len(set(nums))  # 返回 长度(数组) 不等于 长度(set(数组))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(containsDuplicate([1, 2, 3]))  # 打印输出
