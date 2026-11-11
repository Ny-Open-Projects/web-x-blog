# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def bucket_sort(lst, n=2):  # 定义函数 bucket_sort（参数：lst, 元素个数 赋值为 2）
    # 桶排序：按取值范围均匀分桶，桶内各自排序后合并
    if len(lst) < 2:  # 若 长度(lst) 小于 2
        return lst  # 返回 lst
    max_val = max(lst)  # 把 取较大值 lst) 存入 max_val
    min_val = min(lst)  # 把 取较小值 lst) 存入 min_val
    dist = max_val - min_val  # 把 max_val 减 min_val 存入 dist
    if dist == 0:  # 若 dist 等于 0
        return lst  # 返回 lst
    buckets = [[] for _ in range(n)]  # 把 [[] for _ in range(元素个数)] 存入 buckets
    width = (dist + 1) // n  # 每个桶的区间宽度
    for current in lst:  # 逐个取出 lst 的元素（current）
        index = (current - min_val) // width  # 把 (current 减 min_val) 除以 除以 width 存入 index
        if index >= n:  # 若 index 不低于 元素个数
            index = n - 1  # 把 元素个数 减 1 存入 index
        buckets[index].append(current)  # 把 current 追加到列表尾部
    for bucket in buckets:  # 逐个取出 buckets 的元素（bucket）
        bucket.sort()  # 排序
    result = [
        item for sublist in buckets for item in sublist
    ]  # 把 [item for sublist in buckets for item in sublist] 存入 结果
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    test_cases = [
        [102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104, 102, 104, 106, 109, 102],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [],
        [1],
        [-2, 1, 0, -9, 1, 3, 9, 99, 9, -30, -100, 100, 88, 88, 20, 1, 0, 3, 4, 5, -20],
    ]
    for case in test_cases:  # 逐个取出 test_cases 的元素（case）
        print(bucket_sort(case[:], 5))  # 打印输出
