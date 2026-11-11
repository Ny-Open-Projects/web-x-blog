# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def count_sort(list):  # 定义函数 count_sort（参数：列表）
    length = len(list)  # 把 长度(列表) 存入 长度
    if length < 2:  # 若 长度 小于 2
        return  # return
    max_val = max(list)  # 把 取较大值 列表) 存入 max_val
    min_val = min(list)  # 把 取较小值 列表) 存入 min_val
    count_list = [0] * (max_val - min_val + 1)  # 把 [0] 乘 (max_val 减 min_val 加 1) 存入 count_list
    result = [0] * length  # 把 [0] 乘 长度 存入 结果
    for num in list:  # 逐个取出 列表 的元素（num）
        count_list[num - min_val] += 1  # 把 1 写入 count_list[num - min_val] +
    for j in range(1, len(count_list)):  # 让 下标 j 从 1 到 长度(count_list 遍历
        count_list[j] += count_list[j - 1]  # count_list[j]累加 count_list[下标 j 减 1]
    for k in range(length - 1, -1, -1):  # 让 下标 k 从 长度 减 1 倒数回去（每步减 1）
        current_index = (
            count_list[list[k] - min_val] - 1
        )  # 把 count_list[列表[下标 k] 减 min_val] 减 1 存入 current_index
        result[current_index] = list[k]  # 把 列表[下标 k] 写入 result[current_index]
        count_list[list[k] - min_val] -= 1  # 把 1 写入 count_list[list[k] - min_val] -
    list[:] = result  # 把 结果 写入 list[:]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [4, 2, 2, 8, 3, 3, 1]  # 把 [4, 2, 2, 8, 3, 3, 1] 存入 数组
    count_sort(arr)  # count_sort(数组)
    print(arr)  # 打印输出
