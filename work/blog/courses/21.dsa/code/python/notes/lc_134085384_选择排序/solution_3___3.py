# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def selection_sort(nums):  # 定义函数 selection_sort（参数：数组）
    arr = list(nums)  # 把 列表(数组) 存入 数组
    length = len(arr)  # 把 长度(数组) 存入 长度
    for i in range(length - 1):  # 让 下标 i 从 长度 减 1 遍历
        min_index = i  # 把 下标 i 存入 min_index
        for j in range(i + 1, length):  # 让 下标 j 从 下标 i 加 1 到 长度 遍历
            if arr[j] < arr[min_index]:  # 若 数组[下标 j] 小于 数组[min_index]
                min_index = j  # 把 下标 j 存入 min_index
        if i != min_index:  # 若 下标 i 不等于 min_index
            arr[i], arr[min_index] = (
                arr[min_index],
                arr[i],
            )  # 把 数组[min_index], 数组[下标 i] 写入 arr[i], arr[min_index]
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(selection_sort([5, 4, 3, 2, 1]))  # 打印输出
