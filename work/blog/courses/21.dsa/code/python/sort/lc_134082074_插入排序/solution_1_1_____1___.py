# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
def insertion_sort(nums: list) -> None:  # 定义函数 insertion_sort（参数：数组: 列表）
    length = len(nums)  # 把 长度(数组) 存入 长度
    for i in range(1, length):  # 让 下标 i 从 1 到 长度 遍历
        tmp = nums[i]  # 把 数组[下标 i] 存入 临时变量
        j = i  # 把 下标 i 存入 下标 j
        while j > 0:  # 循环，直到不满足「下标 j 超过 0」
            if nums[j - 1] > tmp:  # 若 数组[下标 j 减 1] 超过 临时变量
                nums[j] = nums[j - 1]  # 把 数组[下标 j 减 1] 写入 nums[j]
            else:  # 否则
                break  # 跳出循环
            j -= 1  # 下标 j累减 1
        if i != j:  # 若 下标 i 不等于 下标 j
            nums[j] = tmp  # 把 临时变量 写入 nums[j]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    nums = [5, 2, 3, 1, 4]  # 把 [5, 2, 3, 1, 4] 存入 数组
    insertion_sort(nums)  # insertion_sort(数组)
    print(nums)  # 打印输出
