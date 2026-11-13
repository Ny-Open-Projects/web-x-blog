# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def bucket_sort(lst, n=2):  # 定义函数 bucket_sort（参数：lst, 元素个数 赋值为 2）
    if len(lst) < 2:  # 若 长度(lst) 小于 2
        return lst  # 返回 lst
    max_val = max(lst)  # 把 取较大值 lst) 存入 max_val
    min_val = min(lst)  # 把 取较小值 lst) 存入 min_val
    dist = max_val - min_val  # 把 max_val 减 min_val 存入 dist
    if dist == 0:  # 若 dist 等于 0
        return lst  # 返回 lst
    buckets = [[] for _ in range(n)]  # 把 [[] for _ in range(元素个数)] 存入 buckets
    for current in lst:  # 逐个取出 lst 的元素（current）
        index = int(
            (current - min_val) / dist * n
        )  # 把 int((current 减 min_val) 除以 dist 乘 元素个数) 存入 index
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
    print(bucket_sort([4, 2, 7, 1, 9, 3, 6, 5, 8]))  # 打印输出
    print(bucket_sort([0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]))  # 打印输出
