try:
    import numpy as np
except ImportError:
    print("该题演示需要第三方库 numpy:pip install numpy,原理见正文")
    raise SystemExit(0)

def sample_pipeline(seed):
    rng = np.random.default_rng(seed)      # 新 API:独立 Generator
    return {
        "ints": rng.integers(0, 10, 5).tolist(),
        "normal": rng.normal(0, 1, 3).round(3).tolist(),
        "shuffle": rng.permutation(np.arange(5)).tolist(),
    }

if __name__ == "__main__":
    r1 = sample_pipeline(42)
    r2 = sample_pipeline(42)
    r3 = sample_pipeline(7)
    assert r1 == r2, "同种子必须可复现"
    assert r1 != r3, "不同种子应不同"
    print("reproducible:", r1["ints"])
