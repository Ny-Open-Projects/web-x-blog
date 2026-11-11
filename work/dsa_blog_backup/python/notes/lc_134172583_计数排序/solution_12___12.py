# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def count_sort(lst):  # 定义函数 count_sort（参数：lst）
    # 计数排序 - 稳定版（计数数组转累加数组，从后向前回填，原地替换）
    length = len(lst)  # 把 长度(lst) 存入 长度
    if length < 2:  # 若 长度 小于 2
        return  # return
    max_val = max(lst)  # 把 取较大值 lst) 存入 max_val
    min_val = min(lst)  # 把 取较小值 lst) 存入 min_val
    count_list = [0] * (max_val - min_val + 1)  # 把 [0] 乘 (max_val 减 min_val 加 1) 存入 count_list
    result = [0] * length  # 把 [0] 乘 长度 存入 结果
    for num in lst:  # 逐个取出 lst 的元素（num）
        count_list[num - min_val] += 1  # 把 1 写入 count_list[num - min_val] +
    for j in range(1, len(count_list)):  # 让 下标 j 从 1 到 长度(count_list 遍历
        count_list[j] += count_list[j - 1]  # count_list[j]累加 count_list[下标 j 减 1]
    for k in range(length - 1, -1, -1):  # 让 下标 k 从 长度 减 1 倒数回去（每步减 1）
        current_index = (
            count_list[lst[k] - min_val] - 1
        )  # 把 count_list[lst[下标 k] 减 min_val] 减 1 存入 current_index
        result[current_index] = lst[k]  # 把 lst[下标 k] 写入 result[current_index]
        count_list[lst[k] - min_val] -= 1  # 把 1 写入 count_list[lst[k] - min_val] -
    lst[:] = result  # 把 结果 写入 lst[:]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    lst = [102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104, 102, 104, 106, 109, 102]
    count_sort(lst)  # count_sort(lst)
    print(lst)  # [101, 101, 102, ... , 109, 109]
