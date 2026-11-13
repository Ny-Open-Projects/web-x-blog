# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def quickselect(nums, l, r, k):  # 定义函数 quickselect（参数：数组, 左指针, 右指针, 下标 k）
    if l == r:  # 若 左指针 等于 右指针
        return nums[k]  # 返回 数组[下标 k]
    pivot = nums[l]  # 把 数组[左指针] 存入 pivot
    i, j = l - 1, r + 1  # 把 左指针 减 1, 右指针 加 1 写入 i, j
    while i < j:  # 循环，直到不满足「下标 i 小于 下标 j」
        while True:  # 循环，直到不满足「True」
            i += 1  # 下标 i累加 1
            if nums[i] <= pivot:  # 若 数组[下标 i] 不超过 pivot
                continue  # 跳过本轮，进入下一次
            break  # 跳出循环
        while True:  # 循环，直到不满足「True」
            j -= 1  # 下标 j累减 1
            if nums[j] >= pivot:  # 若 数组[下标 j] 不低于 pivot
                continue  # 跳过本轮，进入下一次
            break  # 跳出循环
        if i < j:  # 若 下标 i 小于 下标 j
            nums[i], nums[j] = nums[j], nums[i]  # 把 数组[下标 j], 数组[下标 i] 写入 nums[i], nums[j]
    return quickselect(nums, l, j, k) if k <= j else quickselect(nums, j + 1, r, k)


def findKthLargest(nums, k):  # 定义函数 findKthLargest（参数：数组, 下标 k）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    return quickselect(nums, 0, n - 1, n - k)  # 返回 quickselect(数组, 0, 元素个数 减 1, 元素个数 减 下标 k)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(quickselect([1, 2, 3], None, None, 1))  # 打印输出
