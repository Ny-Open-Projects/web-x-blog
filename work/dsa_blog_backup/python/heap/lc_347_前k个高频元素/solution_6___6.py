# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
# 前 K 个高频元素 - 方案: 桶排序
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import Counter  # from collections import Counter


def top_k_frequent(nums, k):  # 定义函数 top_k_frequent（参数：数组, 下标 k）
    cnt = Counter(nums)  # 把 Counter(数组) 存入 计数
    max_freq = max(cnt.values())  # 把 取较大值 计数.values()) 存入 max_freq
    buckets = [[] for _ in range(max_freq + 1)]  # 把 [[] for _ in range(max_freq 加 1)] 存入 buckets
    for num, f in cnt.items():  # for num, f in 计数.items():
        buckets[f].append(num)  # 把 num 追加到列表尾部
    result = []  # 把 [] 存入 结果
    for f in range(max_freq, 0, -1):  # 让 f 从 max_freq 倒数回去（每步减 1）
        for num in buckets[f]:  # 逐个取出 buckets 的元素（num）
            result.append(num)  # 把 num 追加到列表尾部
            if len(result) == k:  # 若 长度(结果) 等于 下标 k
                return result  # 返回 结果
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
