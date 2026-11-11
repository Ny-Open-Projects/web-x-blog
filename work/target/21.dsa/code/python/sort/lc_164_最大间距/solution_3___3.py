# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maximumGap(nums):  # 定义函数 maximumGap（参数：数组）
    if len(nums) < 2:  # 若 长度(数组) 小于 2
        return 0  # 返回 0
    mn = min(nums)  # 把 取较小值 数组) 存入 mn
    mx = max(nums)  # 把 取较大值 数组) 存入 mx
    if mn == mx:  # 若 mn 等于 mx
        return 0  # 返回 0
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    bucket_size = max(
        1, (mx - mn) // (n - 1)
    )  # 把 取较大值 1, (mx 减 mn) 除以 除以 (元素个数 减 1)) 存入 bucket_size
    bucket_count = (mx - mn) // bucket_size + 1  # 把 (mx 减 mn) 除以 除以 bucket_size 加 1 存入 bucket_count
    buckets = [
        [None, None] for _ in range(bucket_count)
    ]  # 把 [[None, None] for _ in range(bucket_count)] 存入 buckets
    for num in nums:  # 逐个取出 数组 的元素（num）
        idx = (num - mn) // bucket_size  # 把 (num 减 mn) 除以 除以 bucket_size 存入 idx
        if buckets[idx][0] is None:  # 若 buckets[idx][0] is None
            buckets[idx][0] = buckets[idx][1] = num  # 把 buckets[idx][1] 赋值为 num 写入 buckets[idx][0]
        else:  # 否则
            buckets[idx][0] = min(
                buckets[idx][0], num
            )  # 把 取较小值 buckets[idx][0], num) 写入 buckets[idx][0]
            buckets[idx][1] = max(
                buckets[idx][1], num
            )  # 把 取较大值 buckets[idx][1], num) 写入 buckets[idx][1]
    max_gap = 0  # 把 0 存入 max_gap
    prev = None  # 把 None 存入 前一个
    for b in buckets:  # 逐个取出 buckets 的元素（b）
        if b[0] is None:  # 若 b[0] is None
            continue  # 跳过本轮，进入下一次
        if prev is not None:  # 若 前一个 is not None
            max_gap = max(max_gap, b[0] - prev)  # 把 取较大值 max_gap, b[0] 减 前一个) 存入 max_gap
        prev = b[1]  # 把 b[1] 存入 前一个
    return max_gap  # 返回 max_gap


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maximumGap([3, 6, 9, 1]))  # 打印输出
