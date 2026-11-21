"""LIMIT 与排序: 全排序 vs top-N 优先队列的比较次数"""
import heapq
import math
import random

random.seed(3)
n, k = 100000, 5
data = [random.random() for _ in range(n)]

def topn_comparisons():
    heap, cmp = [], 0
    for x in data:
        if len(heap) < k:
            heapq.heappush(heap, x)
            cmp += math.log2(len(heap))
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
            cmp += 2 * math.log2(k)
    return cmp, sorted(heap, reverse=True)

c_full = n * math.log2(n)
c_top, top5 = topn_comparisons()
print(f"全排序: 约 {c_full:.0f} 次比较, 缓冲需容纳全部 n 行")
print(f"top-N 堆: 约 {c_top:.0f} 次比较, 缓冲只留 k={k} 行")
print("top5:", [round(x, 4) for x in top5])
