# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134701204
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def subsets(nums):  # 定义函数 subsets（参数：数组）
    res = [[]]  # 把 [[]] 存入 结果
    for num in nums:  # 逐个取出 数组 的元素（num）
        res += [cur + [num] for cur in res]  # 结果累加 [当前值 加 [num] for 当前值 in 结果]
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(subsets([1, 2, 3]))  # 打印输出
