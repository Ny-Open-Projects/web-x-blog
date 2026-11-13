# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133279737
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def intersection(nums1, nums2):  # 定义函数 intersection（参数：数组1, 数组2）
    return list(set(nums1) & set(nums2))  # 返回 列表(set(数组1) 按位与 set(数组2))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(intersection([1, 2, 2, 1], [2, 2]))  # 打印输出
