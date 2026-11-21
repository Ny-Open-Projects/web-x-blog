try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    n = 100_000
    df = pd.DataFrame({
        "city": np.random.default_rng(0).choice(["BJ", "SH", "SZ"], n),
        "val": np.random.default_rng(1).integers(0, 1000, n),
        "cnt": pd.array([1, None] * (n // 2), dtype="Int64"),  # nullable int
    })
    before = df.memory_usage(deep=True).sum()
    df["city"] = df["city"].astype("category")
    after = df.memory_usage(deep=True).sum()
    print(f"memory {before/1e6:.1f}MB -> {after/1e6:.1f}MB")
    print(df["cnt"].dtype, df["city"].cat.categories.tolist())

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        print("标准库层面:用整数编码枚举值 + 常量表模拟 category 思路")
