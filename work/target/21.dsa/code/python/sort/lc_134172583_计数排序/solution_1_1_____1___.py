# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def count_sort(list):  # 定义函数 count_sort（参数：列表）
    length = len(list)  # 把 长度(列表) 存入 长度
    if length < 2:  # 若 长度 小于 2
        return  # return
    max_val = max(list)  # 把 取较大值 列表) 存入 max_val
    count_list = [0] * (max_val + 1)  # 把 [0] 乘 (max_val 加 1) 存入 count_list
    for num in list:  # 逐个取出 列表 的元素（num）
        count_list[num] += 1  # count_list[num]累加 1
    i = 0  # 把 0 存入 下标 i
    for j in range(max_val + 1):  # 让 下标 j 从 max_val 加 1 遍历
        for _ in range(count_list[j]):  # 让 _ 从 count_list[下标 j] 遍历
            list[i] = j  # 把 下标 j 写入 list[i]
            i += 1  # 下标 i累加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [4, 2, 2, 8, 3, 3, 1]  # 把 [4, 2, 2, 8, 3, 3, 1] 存入 数组
    count_sort(arr)  # count_sort(数组)
    print(arr)  # 打印输出
