# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
def bubble_sort_v3(nums: list) -> None:  # 定义函数 bubble_sort_v3（参数：数组: 列表）
    length = len(nums)  # 把 长度(数组) 存入 长度
    sorted_ = False  # 把 False 存入 sorted_
    while not sorted_:  # 循环，直到不满足「not sorted_」
        sorted_ = True  # 把 True 存入 sorted_
        for i in range(length - 1):  # 让 下标 i 从 长度 减 1 遍历
            if nums[i] > nums[i + 1]:  # 若 数组[下标 i] 超过 数组[下标 i 加 1]
                nums[i], nums[i + 1] = (
                    nums[i + 1],
                    nums[i],
                )  # 把 数组[下标 i 加 1], 数组[下标 i] 写入 nums[i], nums[i + 1]
                sorted_ = False  # 把 False 存入 sorted_
        length -= 1  # 长度累减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    nums = [5, 2, 3, 1, 4]  # 把 [5, 2, 3, 1, 4] 存入 数组
    bubble_sort_v3(nums)  # bubble_sort_v3(数组)
    print(nums)  # 打印输出
