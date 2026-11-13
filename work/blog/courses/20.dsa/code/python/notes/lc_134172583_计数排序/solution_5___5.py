# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def count_sort(lst):  # 定义函数 count_sort（参数：lst）
    # 计数排序 - 基础版（要求非负整数，原地排序）
    length = len(lst)  # 把 长度(lst) 存入 长度
    if length < 2:  # 若 长度 小于 2
        return  # return
    max_val = max(lst)  # 把 取较大值 lst) 存入 max_val
    count_list = [0] * (max_val + 1)  # 把 [0] 乘 (max_val 加 1) 存入 count_list
    for num in lst:  # 逐个取出 lst 的元素（num）
        count_list[num] += 1  # count_list[num]累加 1
    i = 0  # 把 0 存入 下标 i
    for j in range(max_val + 1):  # 让 下标 j 从 max_val 加 1 遍历
        for _ in range(count_list[j]):  # 让 _ 从 count_list[下标 j] 遍历
            lst[i] = j  # 把 下标 j 写入 lst[i]
            i += 1  # 下标 i累加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    lst = [2, 3, 8, 7, 1, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2]
    count_sort(lst)  # count_sort(lst)
    print(lst)  # [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 6, 7, 7, 8, 8, 9, 9]
