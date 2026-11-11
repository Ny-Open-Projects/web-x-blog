# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
def bubble_sort_v5(nums: list) -> None:  # 定义函数 bubble_sort_v5（参数：数组: 列表）
    length = len(nums)  # 把 长度(数组) 存入 长度
    k = length - 1  # 把 长度 减 1 存入 下标 k
    last = 0  # 把 0 存入 last
    i = 0  # 把 0 存入 下标 i
    sorted_ = False  # 把 False 存入 sorted_
    while i < length - 1 and not sorted_:  # 循环，直到不满足「下标 i 小于 长度 减 1 and not sorted_」
        sorted_ = True  # 把 True 存入 sorted_
        for j in range(k):  # 让 下标 j 从 下标 k 遍历
            if nums[j] > nums[j + 1]:  # 若 数组[下标 j] 超过 数组[下标 j 加 1]
                nums[j], nums[j + 1] = (
                    nums[j + 1],
                    nums[j],
                )  # 把 数组[下标 j 加 1], 数组[下标 j] 写入 nums[j], nums[j + 1]
                last = j  # 把 下标 j 存入 last
                sorted_ = False  # 把 False 存入 sorted_
        k = last  # 把 last 存入 下标 k
        i += 1  # 下标 i累加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    nums = [5, 2, 3, 1, 4]  # 把 [5, 2, 3, 1, 4] 存入 数组
    bubble_sort_v5(nums)  # bubble_sort_v5(数组)
    print(nums)  # 打印输出
