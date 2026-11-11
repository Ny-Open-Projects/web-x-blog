# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145369843
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from functools import cmp_to_key  # from functools import cmp_to_key


def largestNumber(nums):  # 定义函数 largestNumber（参数：数组）
    strs = list(map(str, nums))  # 把 列表(映射表(str, 数组)) 存入 strs

    def cmp(a, b):  # 定义函数 cmp（参数：数组, b）
        if a + b > b + a:  # 若 数组 加 b 超过 b 加 数组
            return -1  # 返回 减 1
        elif a + b < b + a:  # 否则，若 数组 加 b 小于 b 加 数组
            return 1  # 返回 1
        return 0  # 返回 0

    strs.sort(key=cmp_to_key(cmp))  # 排序
    if strs[0] == "0":  # 若 strs[0] 等于 '0'
        return "0"  # 返回 '0'
    return "".join(strs)  # 返回 ''.join(strs)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(largestNumber([10, 2]))  # 打印输出
    print(largestNumber([3, 30, 34, 5, 9]))  # 打印输出
