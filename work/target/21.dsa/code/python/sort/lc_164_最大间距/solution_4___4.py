# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maximumGap(nums):  # 定义函数 maximumGap（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n < 2:  # 若 元素个数 小于 2
        return 0  # 返回 0
    min_val = min(nums)  # 把 取较小值 数组) 存入 min_val
    max_val = max(nums)  # 把 取较大值 数组) 存入 max_val
    d = max(
        1, (max_val - min_val) // (n - 1)
    )  # 把 取较大值 1, (max_val 减 min_val) 除以 除以 (元素个数 减 1)) 存入 d
    bucket_size = (
        (max_val - min_val) // d
    ) + 1  # 把 ((max_val 减 min_val) 除以 除以 d) 加 1 存入 bucket_size
    bucket = [
        [-1, -1] for _ in range(bucket_size)
    ]  # 把 [[ 减 1, 减 1] for _ in range(bucket_size)] 存入 bucket
    for num in nums:  # 逐个取出 数组 的元素（num）
        idx = (num - min_val) // d  # 把 (num 减 min_val) 除以 除以 d 存入 idx
        if bucket[idx][0] == -1:  # 若 bucket[idx][0] 等于 减 1
            bucket[idx][0] = bucket[idx][1] = num  # 把 bucket[idx][1] 赋值为 num 写入 bucket[idx][0]
        else:  # 否则
            bucket[idx][0] = min(bucket[idx][0], num)  # 把 取较小值 bucket[idx][0], num) 写入 bucket[idx][0]
            bucket[idx][1] = max(bucket[idx][1], num)  # 把 取较大值 bucket[idx][1], num) 写入 bucket[idx][1]
    max_gap = 0  # 把 0 存入 max_gap
    prev = -1  # 把 减 1 存入 前一个
    for i in range(bucket_size):  # 让 下标 i 从 bucket_size 遍历
        if bucket[i][0] == -1:  # 若 bucket[下标 i][0] 等于 减 1
            continue  # 跳过本轮，进入下一次
        if prev != -1:  # 若 前一个 不等于 减 1
            max_gap = max(
                max_gap, bucket[i][0] - bucket[prev][1]
            )  # 把 取较大值 max_gap, bucket[下标 i][0] 减 bucket[前一个][1]) 存入 max_gap
        prev = i  # 把 下标 i 存入 前一个
    return max_gap  # 返回 max_gap


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maximumGap([1, 2, 3]))  # 打印输出
