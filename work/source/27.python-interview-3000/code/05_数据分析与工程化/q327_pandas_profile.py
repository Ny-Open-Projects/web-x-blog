import time

try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def timed(fn, *args, **kwargs):
    t0 = time.perf_counter()
    result = fn(*args, **kwargs)
    return result, time.perf_counter() - t0

if __name__ == "__main__":
    if PANDAS:
        rng = np.random.default_rng(0)
        n = 500_000
        df = pd.DataFrame({"k": rng.integers(0, 100, n),
                           "v": rng.random(n)})
        # 热点对比:逐行 apply vs 向量化
        _, slow = timed(lambda: df.apply(lambda r: r["v"] * 2, axis=1))
        _, fast = timed(lambda: df["v"] * 2)
        print(f"apply(axis=1): {slow:.3f}s  vectorized: {fast:.4f}s")
        print(f"speedup ~{slow / max(fast, 1e-9):.0f}x")
        print(df.memory_usage(deep=True).to_dict())
    else:
        print("标准库:用 time.perf_counter 分段计时定位热点")
