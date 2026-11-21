import random

random.seed(11)
pop = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("b", 5), ("c", 6)]
groups = {}
for g, v in pop:
    groups.setdefault(g, []).append(v)

print("简单随机:", random.sample(pop, 3))
stratified = [random.choice(groups[g]) for g in groups for _ in range(1)]  # 每层保底 1 条
print("分层保底:", stratified)
systematic = pop[::3]
print("系统采样 k=3:", systematic)
weighted = random.choices(pop, weights=[10, 10, 1, 1, 1, 1], k=3)
print("加权采样 大层权重 10:", weighted)
