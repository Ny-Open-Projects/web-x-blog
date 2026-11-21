try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    s = pd.Series([1, 2, 3, 4])
    print(s.map(lambda x: x * 10).tolist())          # 逐元素
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    print(df.applymap(lambda x: x + 1).to_dict())    # 全表逐元素
    print(df.apply("sum", axis=0).to_dict())         # 按列
    # 向量化替代方案对比
    big = pd.Series(np.arange(1_000_000))
    import time
    t0 = time.perf_counter()
    big.map(lambda x: x * 2)
    t1 = time.perf_counter()
    big * 2
    t2 = time.perf_counter()
    print(f"map: {t1 - t0:.3f}s  vectorized: {t2 - t1:.4f}s")

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        s = [1, 2, 3, 4]
        print([x * 10 for x in s])                   # 逐元素映射
        print([sum(col) for col in zip(s, s)])       # 按列聚合
