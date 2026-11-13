# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059
# Gnome Sort (侏儒排序) + Bubble Sort + 贪心找零
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def gnome_sort(arr):  # 定义函数 gnome_sort（参数：数组）
    i = 0  # 把 0 存入 下标 i
    while i < len(arr):  # 循环，直到不满足「下标 i 小于 长度(数组」
        if i == 0 or arr[i] >= arr[i - 1]:  # 若 下标 i 等于 0 or 数组[下标 i] 不低于 数组[下标 i 减 1]
            i += 1  # 下标 i累加 1
        else:  # 否则
            arr[i - 1], arr[i] = (
                arr[i],
                arr[i - 1],
            )  # 把 数组[下标 i], 数组[下标 i 减 1] 写入 arr[i - 1], arr[i]
            i -= 1  # 下标 i累减 1
    return arr  # 返回 数组


def bubble_sort(arr):  # 定义函数 bubble_sort（参数：数组）
    arr = arr[:]  # 把 复制 数组 存入 数组
    swapped = True  # 把 True 存入 swapped
    while swapped:  # 循环，直到不满足「swapped」
        swapped = False  # 把 False 存入 swapped
        for i in range(len(arr) - 1):  # 让 下标 i 从 长度(数组 遍历
            if arr[i] > arr[i + 1]:  # 若 数组[下标 i] 超过 数组[下标 i 加 1]
                arr[i], arr[i + 1] = (
                    arr[i + 1],
                    arr[i],
                )  # 把 数组[下标 i 加 1], 数组[下标 i] 写入 arr[i], arr[i + 1]
                swapped = True  # 把 True 存入 swapped
    return arr  # 返回 数组


def coin_change(coins, amount):  # 定义函数 coin_change（参数：硬币面额, 目标金额）
    coins = sorted(coins, reverse=True)  # 把 sorted(硬币面额, reverse 赋值为 True) 存入 硬币面额
    remaining = amount  # 把 目标金额 存入 remaining
    count = 0  # 把 0 存入 计数
    for coin in coins:  # 逐个取出 硬币面额 的元素（coin）
        while remaining >= coin:  # 循环，直到不满足「remaining 不低于 coin」
            remaining -= coin  # remaining累减 coin
            count += 1  # 计数累加 1
    return count if remaining == 0 else -1  # 返回 计数 if remaining 等于 0 else 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(gnome_sort([3, 2, 1]))  # [1, 2, 3]
    print(bubble_sort([3, 2, 1]))  # [1, 2, 3]
    print(coin_change([1, 5, 10, 25], 63))  # 6
