try:
    import numpy as np
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({"x": np.arange(-5, 5), "y": np.arange(10) * 1.5})
    # 反例:for idx, row in df.iterrows(): 手写 if-else
    # 向量化:多分支用 np.select
    conditions = [df["x"] > 0, df["x"] < 0]
    choices = ["pos", "neg"]
    df["sign"] = np.select(conditions, choices, default="zero")
    # 条件赋值用 np.where
    df["clip_y"] = np.where(df["y"] > 10, 10, df["y"])
    print(df.head())

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        xs = list(range(-5, 5))
        out = ["zero" if x == 0 else ("pos" if x > 0 else "neg") for x in xs]
        print(list(zip(xs, out)))
