# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def quick_sort_v1(arr):  # 定义函数 quick_sort_v1（参数：数组）
    def qs_fn(arr):  # 定义函数 qs_fn（参数：数组）
        if len(arr) < 1:  # 若 长度(数组) 小于 1
            return arr  # 返回 数组
        pivot_index = len(arr) // 2  # 把 长度(数组) 除以 除以 2 存入 pivot_index
        pivot = arr[pivot_index]  # 把 数组[pivot_index] 存入 pivot
        rest = (
            arr[:pivot_index] + arr[pivot_index + 1 :]
        )  # 把 数组[:pivot_index] 加 数组[pivot_index 加 1:] 存入 rest
        left, right = [], []  # 把 [], [] 写入 left, right
        for item in rest:  # 逐个取出 rest 的元素（item）
            if item < pivot:  # 若 item 小于 pivot
                left.append(item)  # 把 item 追加到列表尾部
            elif item > pivot:  # 否则，若 item 超过 pivot
                right.append(item)  # 把 item 追加到列表尾部
        return qs_fn(left) + [pivot] + qs_fn(right)  # 返回 qs_fn(左边界) 加 [pivot] 加 qs_fn(右边界)

    res = qs_fn(arr)  # 把 qs_fn(数组) 存入 结果
    arr[:] = res  # 把 结果 写入 arr[:]
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [15, 4, 23, 52, 1]  # 把 [15, 4, 23, 52, 1] 存入 数组
    quick_sort_v1(arr)  # quick_sort_v1(数组)
    print(arr)  # 输出: [1, 4, 15, 23, 52]
