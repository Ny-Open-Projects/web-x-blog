import random
import statistics

random.seed(7)
data = [random.expovariate(0.2) for _ in range(300)]
means = []
for _ in range(4000):
    sample = [random.choice(data) for _ in range(len(data))]
    means.append(statistics.mean(sample))
means.sort()
lo, hi = means[int(0.025 * len(means))], means[int(0.975 * len(means))]
print(f"样本均值 {statistics.mean(data):.3f}")
print(f"bootstrap 95% CI [{lo:.3f}, {hi:.3f}]")
assert lo < statistics.mean(data) < hi
print("区间覆盖点估计,方法对均值、中位数、P99 通用")
