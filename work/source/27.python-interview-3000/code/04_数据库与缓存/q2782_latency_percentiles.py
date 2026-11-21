"""存储延迟的分位: 均值被长尾稀释, P99 才是真话"""
import random
import statistics

random.seed(5)
samples = []
for _ in range(10000):
    if random.random() < 0.01:
        samples.append(random.uniform(80, 200))    # 1% 的慢请求撑起长尾
    else:
        samples.append(random.uniform(0.5, 2.0))

def pct(data, p):
    s = sorted(data)
    k = max(0, min(len(s) - 1, int(round(p / 100.0 * (len(s) - 1)))))
    return s[k]

print("均值 %.2f ms (大盘上看起来很好)" % statistics.mean(samples))
print("P50 %.2f | P95 %.2f | P99 %.2f | MAX %.1f ms (长尾全在 P99 之外)"
      % (pct(samples, 50), pct(samples, 95), pct(samples, 99), max(samples)))
print("结论: 均值正常 + 投诉不断的组合, 先切 P99 看长尾, 慢路径都藏在那 1% 里")
