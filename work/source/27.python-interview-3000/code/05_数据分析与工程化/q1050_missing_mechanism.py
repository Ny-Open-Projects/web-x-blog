import random
import statistics

random.seed(3)
n = 2000
age = [random.gauss(35, 8) for _ in range(n)]
income = [a * 300 + random.gauss(0, 2000) for a in age]  # 收入与年龄相关

# MAR:收入缺失概率随年龄增大
income_mar = [inc if random.random() > 0.02 * max(0, a - 40) else None for a, inc in zip(age, income)]
# MNAR:高收入者更不愿填,缺失依赖自身
income_mnar = [inc if random.random() > inc / 300000 else None for inc in income]

def report(tag, xs):
    obs = [x for x in xs if x is not None]
    miss = 1 - len(obs) / len(xs)
    print(f"{tag}: 缺失率 {miss:.1%} 观测均值 {statistics.mean(obs):.0f} 真实均值 {statistics.mean(income):.0f}")

report("MAR  按年龄缺失  ", income_mar)
report("MNAR 按收入缺失  ", income_mnar)
# MAR 的均值下滑可用分组填充纠偏,MNAR 无论怎么填都系统偏低
