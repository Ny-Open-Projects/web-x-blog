try:
    import numpy as np
    rng = np.random.default_rng(0)
    x = rng.lognormal(0, 1.5, 500)  # 重尾样本
    z = (x - x.mean()) / x.std()
    print("z>3 占比:", round(float((np.abs(z) > 3).mean()), 4), "正态假设下应约 0.0027")
    print("99 分位:", round(float(np.quantile(x, 0.99)), 1), "3σ 上界:", round(float(x.mean() + 3 * x.std()), 1))
    lz = (np.log(x) - np.log(x).mean()) / np.log(x).std()
    print("log 变换后 z>3 占比:", round(float((np.abs(lz) > 3).mean()), 4))
except ImportError:
    import random, statistics
    random.seed(0)
    x = [random.lognormvariate(0, 1.5) for _ in range(500)]
    m, sd = statistics.mean(x), statistics.pstdev(x)
    z = [(v - m) / sd for v in x]
    print("z>3 占比:", round(sum(1 for t in z if abs(t) > 3) / len(z), 4))
    lx = [ __import__("math").log(v) for v in x ]
    lm, lsd = statistics.mean(lx), statistics.pstdev(lx)
    lz = [(v - lm) / lsd for v in lx]
    print("log 变换后 z>3 占比:", round(sum(1 for t in lz if abs(t) > 3) / len(lz), 4))
