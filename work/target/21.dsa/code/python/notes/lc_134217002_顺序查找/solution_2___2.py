# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
# 顺序查找 - 返回目标值的下标, 找不到返回 -1
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def seq_search(nums, target):  # 定义函数 seq_search（参数：数组, 目标值）
    for i in range(len(nums)):  # 让 下标 i 从 长度(数组 遍历
        if nums[i] == target:  # 若 数组[下标 i] 等于 目标值
            return i  # 返回 下标 i
    return -1  # 返回 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    lst = [15, 4, 23, 52, 1]  # 把 [15, 4, 23, 52, 1] 存入 lst
    print(seq_search(lst, 23))  # 2
    print(seq_search(lst, 123))  # -1
