# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
# 数组中的第 K 个最大元素 - 方案: 快速选择 (Hoare 分区, 随机 pivot)
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import random  # 引入依赖


def find_kth_largest(nums, k):  # 定义函数 find_kth_largest（参数：数组, 下标 k）
    a = list(nums)  # 把 列表(数组) 存入 数组
    return _quickselect(
        a, 0, len(a) - 1, len(a) - k
    )  # 返回 _quickselect(数组, 0, 长度(数组) 减 1, 长度(数组) 减 下标 k)


def _quickselect(nums, l, r, k):  # 定义函数 _quickselect（参数：数组, 左指针, 右指针, 下标 k）
    if l == r:  # 若 左指针 等于 右指针
        return nums[l]  # 返回 数组[左指针]
    pidx = random.randint(l, r)  # 把 random.randint(左指针, 右指针) 存入 pidx
    nums[l], nums[pidx] = nums[pidx], nums[l]  # 把 数组[pidx], 数组[左指针] 写入 nums[l], nums[pidx]
    pivot = nums[l]  # 把 数组[左指针] 存入 pivot
    i = l - 1  # 把 左指针 减 1 存入 下标 i
    j = r + 1  # 把 右指针 加 1 存入 下标 j
    while i < j:  # 循环，直到不满足「下标 i 小于 下标 j」
        i += 1  # 下标 i累加 1
        while nums[i] < pivot:  # 循环，直到不满足「数组[下标 i] 小于 pivot」
            i += 1  # 下标 i累加 1
        j -= 1  # 下标 j累减 1
        while nums[j] > pivot:  # 循环，直到不满足「数组[下标 j] 超过 pivot」
            j -= 1  # 下标 j累减 1
        if i < j:  # 若 下标 i 小于 下标 j
            nums[i], nums[j] = nums[j], nums[i]  # 把 数组[下标 j], 数组[下标 i] 写入 nums[i], nums[j]
    if k <= j:  # 若 下标 k 不超过 下标 j
        return _quickselect(nums, l, j, k)  # 返回 _quickselect(数组, 左指针, 下标 j, 下标 k)
    else:  # 否则
        return _quickselect(nums, j + 1, r, k)  # 返回 _quickselect(数组, 下标 j 加 1, 右指针, 下标 k)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
