# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maximumGap(nums):  # 定义函数 maximumGap（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n < 2:  # 若 元素个数 小于 2
        return 0  # 返回 0
    min_val = min(nums)  # 把 取较小值 数组) 存入 min_val
    max_val = max(nums)  # 把 取较大值 数组) 存入 max_val
    if min_val == max_val:  # 若 min_val 等于 max_val
        return 0  # 返回 0
    d = max(
        1, (max_val - min_val) // (n - 1)
    )  # 把 取较大值 1, (max_val 减 min_val) 除以 除以 (元素个数 减 1)) 存入 d
    bucket_size = (max_val - min_val) // d + 1  # 把 (max_val 减 min_val) 除以 除以 d 加 1 存入 bucket_size
    buckets = [
        [-1, -1] for _ in range(bucket_size)
    ]  # 把 [[ 减 1, 减 1] for _ in range(bucket_size)] 存入 buckets
    for x in nums:  # 逐个取出 数组 的元素（x）
        idx = (x - min_val) // d  # 把 (x 减 min_val) 除以 除以 d 存入 idx
        if buckets[idx][0] == -1:  # 若 buckets[idx][0] 等于 减 1
            buckets[idx][0] = buckets[idx][1] = x  # 把 buckets[idx][1] 赋值为 x 写入 buckets[idx][0]
        else:  # 否则
            buckets[idx][0] = min(buckets[idx][0], x)  # 把 取较小值 buckets[idx][0], x) 写入 buckets[idx][0]
            buckets[idx][1] = max(buckets[idx][1], x)  # 把 取较大值 buckets[idx][1], x) 写入 buckets[idx][1]
    max_gap = 0  # 把 0 存入 max_gap
    prev = -1  # 把 减 1 存入 前一个
    for i in range(bucket_size):  # 让 下标 i 从 bucket_size 遍历
        if buckets[i][0] == -1:  # 若 buckets[下标 i][0] 等于 减 1
            continue  # 跳过本轮，进入下一次
        if prev != -1:  # 若 前一个 不等于 减 1
            max_gap = max(max_gap, buckets[i][0] - buckets[prev][1])
        prev = i  # 把 下标 i 存入 前一个
    return max_gap  # 返回 max_gap


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maximumGap([3, 6, 9, 1]))  # 打印输出
    print(maximumGap([10]))  # 打印输出
