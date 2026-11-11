# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381295
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortByBits(arr):  # 定义函数 sortByBits（参数：数组）
    bit = [0] * 10001  # 把 [0] 乘 10001 存入 bit
    for i in range(1, 10001):  # 让 下标 i 从 1 到 10001 遍历
        bit[i] = bit[i >> 1] + (i & 1)  # 把 bit[下标 i 超过 超过 1] 加 (下标 i 按位与 1) 写入 bit[i]
    sorted_arr = arr[:]  # 把 复制 数组 存入 sorted_arr
    sorted_arr.sort(key=lambda x: (bit[x], x))  # 排序
    return sorted_arr  # 返回 sorted_arr


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortByBits([1, 2, 3]))  # 打印输出
