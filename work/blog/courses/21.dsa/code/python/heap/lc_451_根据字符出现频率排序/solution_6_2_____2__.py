# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133564001
# 根据字符出现频率排序 - 方案: 小顶堆 (heapq)
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖
from collections import Counter  # from collections import Counter


def frequency_sort(s):  # 定义函数 frequency_sort（参数：字符串）
    cnt = Counter(s)  # 把 Counter(字符串) 存入 计数
    heap = [(-v, k) for k, v in cnt.items()]  # 把 [( 减 值, 下标 k) for 下标 k, 值 in 计数.items()] 存入 堆
    heapq.heapify(heap)  # heapq.heapify(堆)
    result = ""  # 把 '' 存入 结果
    while heap:  # 循环，直到不满足「堆」
        v, k = heapq.heappop(heap)  # 把 heapq.heappop(堆) 写入 v, k
        result += k * (-v)  # 结果累加 下标 k 乘 ( 减 值)
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(frequency_sort("tree"))  # 'eert' 或 'eetr'
