"""冷缓存的爬坡: 回源率随请求序衰减的曲线"""
import random

random.seed(3)
N = 500
weights = [1.0 / (i + 1) for i in range(1, N + 1)]   # Zipf 倾向的热点分布
requests = random.choices(range(N), weights=weights, k=20000)

cache = set()
miss_in_window = 0
WINDOW = 2000
print("窗口   回源率")
for i, k in enumerate(requests, 1):
    if k not in cache:
        cache.add(k)
        miss_in_window += 1
    if i % WINDOW == 0:
        print("%4d   %5.1f%%" % (i // WINDOW, miss_in_window * 100.0 / WINDOW))
        miss_in_window = 0
print("结论: 回源率单调下降后稳定, 稳定值由热点集中度决定; 预热就是把最陡的爬坡段提前走完")
