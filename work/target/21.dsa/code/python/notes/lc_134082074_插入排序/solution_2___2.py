# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def insertion_sort(nums):  # 定义函数 insertion_sort（参数：数组）
    """插入排序：从第二个数开始向前比较，比它大就后移，最终插入合适位置。"""
    length = len(nums)  # 把 长度(数组) 存入 长度
    for i in range(1, length):  # 让 下标 i 从 1 到 长度 遍历
        tmp = nums[i]  # 当前要插入的“牌”
        j = i  # 把 下标 i 存入 下标 j
        while j > 0:  # 循环，直到不满足「下标 j 超过 0」
            if nums[j - 1] > tmp:  # 若 数组[下标 j 减 1] 超过 临时变量
                nums[j] = nums[j - 1]  # 后移
            else:  # 否则
                break  # 跳出循环
            j -= 1  # 下标 j累减 1
        if i != j:  # 若 下标 i 不等于 下标 j
            nums[j] = tmp  # 把 临时变量 写入 nums[j]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    list_ = [5, 4, 3, 2, 1]  # 把 [5, 4, 3, 2, 1] 存入 list_
    insertion_sort(list_)  # insertion_sort(list_)
    print(list_)  # [1, 2, 3, 4, 5]
