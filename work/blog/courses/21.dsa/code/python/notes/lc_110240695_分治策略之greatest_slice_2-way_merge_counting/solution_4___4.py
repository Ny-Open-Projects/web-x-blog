# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
# Greatest Slice - 方案4: Linear Scan (Kadane, O(n))
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def max_sub_array(arr):  # 定义函数 max_sub_array（参数：数组）
    if not arr:  # 若 not 数组
        return 0  # 返回 0
    max_sum = arr[0]  # 把 数组[0] 存入 max_sum
    current_sum = arr[0]  # 把 数组[0] 存入 current_sum
    for i in range(1, len(arr)):  # 让 下标 i 从 1 到 长度(数组 遍历
        current_sum = max(
            arr[i], current_sum + arr[i]
        )  # 把 取较大值 数组[下标 i], current_sum 加 数组[下标 i]) 存入 current_sum
        max_sum = max(max_sum, current_sum)  # 把 取较大值 max_sum, current_sum) 存入 max_sum
    return max_sum  # 返回 max_sum


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1]))  # 6
