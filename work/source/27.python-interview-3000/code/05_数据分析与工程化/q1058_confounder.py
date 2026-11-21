import random
import statistics

random.seed(5)
z = [random.uniform(1, 10) for _ in range(500)]                  # 门店规模,混淆变量
x = [zi * 10 + random.gauss(0, 20) for zi in z]                  # 销售额
y = [zi * 5 + random.gauss(0, 20) + 0.1 * xi for zi, xi in zip(z, x)]  # 利润,x 真实效应很小

def corr(a, b):
    ma, mb = statistics.mean(a), statistics.mean(b)
    cov = sum((p - ma) * (q - mb) for p, q in zip(a, b))
    va = sum((p - ma) ** 2 for p in a) ** 0.5
    vb = sum((q - mb) ** 2 for q in b) ** 0.5
    return cov / (va * vb)

def partial_corr(x_, y_, z_):
    rxz, ryz, rxy = corr(x_, z_), corr(y_, z_), corr(x_, y_)
    return (rxy - rxz * ryz) / ((1 - rxz ** 2) ** 0.5 * (1 - ryz ** 2) ** 0.5)

print("原始相关:", round(corr(x, y), 3))
print("控制门店规模后的偏相关:", round(partial_corr(x, y, z), 3))
print("相关大幅下降,说明大部分相关来自混淆变量")
