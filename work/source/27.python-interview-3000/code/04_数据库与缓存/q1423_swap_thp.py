"""系统层延迟毛刺: swap 换页的访问延迟模型"""
import random

random.seed(11)
total_keys = 100000
swapped_threshold = 95000            # 编号 95000 以上的冷页被换出到 swap

def access(k):
    if k >= swapped_threshold:
        return 8.0                   # swap in: 毫秒级惩罚
    return 0.1                       # 常驻内存: 亚毫秒

lat = sorted(access(random.randrange(total_keys)) for _ in range(2000))
p50 = lat[len(lat) // 2]
p999 = lat[int(len(lat) * 0.999)]
print(f"5% 冷页落盘: p50={p50}ms, p99.9={p999}ms <- 尾延迟放大 80 倍")
print("核查: free 看 si/so, vm.swappiness 调低, THP 设为 never")
