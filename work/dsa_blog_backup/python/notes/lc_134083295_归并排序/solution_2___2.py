# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def mergeSort(nums):  # 定义函数 mergeSort（参数：数组）
    if len(nums) <= 1:  # 若 长度(数组) 不超过 1
        return nums  # 返回 数组
    mid = len(nums) // 2  # 把 长度(数组) 除以 除以 2 存入 中点
    left = mergeSort(nums[:mid])  # 把 mergeSort(数组[:中点]) 存入 左边界
    right = mergeSort(nums[mid:])  # 把 mergeSort(数组[中点:]) 存入 右边界
    return merge(left, right)  # 返回 merge(左边界, 右边界)


def merge(left, right):  # 定义函数 merge（参数：左边界, 右边界）
    result = []  # 把 [] 存入 结果
    i = j = 0  # 把 下标 j 赋值为 0 存入 下标 i
    while i < len(left) and j < len(
        right
    ):  # 循环，直到不满足「下标 i 小于 长度(左边界) and 下标 j 小于 长度(右边界」
        if left[i] <= right[j]:  # 若 左边界[下标 i] 不超过 右边界[下标 j]
            result.append(left[i])  # 把 左边界[下标 i] 追加到列表尾部
            i += 1  # 下标 i累加 1
        else:  # 否则
            result.append(right[j])  # 把 右边界[下标 j] 追加到列表尾部
            j += 1  # 下标 j累加 1
    result.extend(left[i:])  # 结果.extend(左边界[下标 i:])
    result.extend(right[j:])  # 结果.extend(右边界[下标 j:])
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(mergeSort([1, 2, 3]))  # 打印输出
