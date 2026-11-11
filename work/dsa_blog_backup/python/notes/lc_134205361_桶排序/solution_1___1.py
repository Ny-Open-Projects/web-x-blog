# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def getIndex(arr, k):  # 定义函数 getIndex（参数：数组, 下标 k）
    if not arr:  # 若 not 数组
        return -1  # 返回 减 1
    min_val, max_val = min(arr), max(arr)  # 把 取较小值 数组), 取较大值 数组) 写入 min_val, max_val
    bucket_size = max(1, (max_val - min_val) // len(arr) + 1)
    bucket_count = (
        max_val - min_val
    ) // bucket_size + 1  # 把 (max_val 减 min_val) 除以 除以 bucket_size 加 1 存入 bucket_count
    buckets = [[] for _ in range(bucket_count)]  # 把 [[] for _ in range(bucket_count)] 存入 buckets
    for num in arr:  # 逐个取出 数组 的元素（num）
        idx = (num - min_val) // bucket_size  # 把 (num 减 min_val) 除以 除以 bucket_size 存入 idx
        buckets[idx].append(num)  # 把 num 追加到列表尾部
    for bucket in buckets:  # 逐个取出 buckets 的元素（bucket）
        bucket.sort()  # 排序
    for i, bucket in enumerate(buckets):  # 同时取 下标 i 与 bucket 遍历
        for num in bucket:  # 逐个取出 bucket 的元素（num）
            k -= 1  # 下标 k累减 1
            if k == 0:  # 若 下标 k 等于 0
                return num  # 返回 num
    return -1  # 返回 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(getIndex([1, 2, 3], 1))  # 打印输出
