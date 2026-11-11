# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def merge_sort(nums):  # 定义函数 merge_sort（参数：数组）
    def ms_fn(arr):  # 定义函数 ms_fn（参数：数组）
        arr_len = len(arr)  # 把 长度(数组) 存入 arr_len
        if arr_len < 2:  # 若 arr_len 小于 2
            return arr  # 返回 数组
        mid = arr_len // 2  # 把 arr_len 除以 除以 2 存入 中点
        left = arr[:mid]  # 把 数组[:中点] 存入 左边界
        right = arr[mid:]  # 把 数组[中点:] 存入 右边界
        ordered_left = ms_fn(left)  # 把 ms_fn(左边界) 存入 ordered_left
        ordered_right = ms_fn(right)  # 把 ms_fn(右边界) 存入 ordered_right
        res = []  # 把 [] 存入 结果
        while ordered_left and ordered_right:  # 循环，直到不满足「ordered_left and ordered_right」
            if ordered_left[0] <= ordered_right[0]:  # 若 ordered_left[0] 不超过 ordered_right[0]
                res.append(ordered_left.pop(0))  # 把 ordered_left 弹出 0 追加到列表尾部
            else:  # 否则
                res.append(ordered_right.pop(0))  # 把 ordered_right 弹出 0 追加到列表尾部
        res.extend(ordered_left)  # 结果.extend(ordered_left)
        res.extend(ordered_right)  # 结果.extend(ordered_right)
        return res  # 返回 结果

    nums[:] = ms_fn(nums)  # 把 ms_fn(数组) 写入 nums[:]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(merge_sort([1, 2, 3]))  # 打印输出
