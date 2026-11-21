try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def reduce_memory(df):
    for col in df.columns:
        t = df[col].dtype
        if pd.api.types.is_integer_dtype(t):
            df[col] = pd.to_numeric(df[col], downcast="integer")
        elif pd.api.types.is_float_dtype(t):
            df[col] = pd.to_numeric(df[col], downcast="float")
        elif pd.api.types.is_object_dtype(t):
            if df[col].nunique() / len(df) < 0.5:
                df[col] = df[col].astype("category")
    return df

if __name__ == "__main__":
    if PANDAS:
        rng = np.random.default_rng(0)
        df = pd.DataFrame({
            "a": rng.integers(0, 100, 50_000),        # int64 -> int8
            "b": rng.random(50_000),                  # float64 -> float32
            "c": rng.choice(["x", "y"], 50_000),      # object -> category
        })
        before = df.memory_usage(deep=True).sum()
        df = reduce_memory(df)
        after = df.memory_usage(deep=True).sum()
        print(f"{before/1e6:.2f}MB -> {after/1e6:.2f}MB")
        print(df.dtypes.to_dict())
    else:
        print("标准库思路:选择最小够用的数值类型,枚举列用整数编码")
