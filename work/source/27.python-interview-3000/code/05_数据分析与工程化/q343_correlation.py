try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    rng = np.random.default_rng(0)
    x = np.linspace(0, 10, 100)
    y_curve = (x - 5) ** 2 + rng.normal(0, 2, 100)   # U 形关系
    df = pd.DataFrame({"x": x, "y": y_curve})
    print("pearson:", round(df["x"].corr(df["y"]), 3),
          "| spearman:", round(df["x"].corr(df["y"], method="spearman"), 3))
    # 异常值敏感性
    a = rng.normal(0, 1, 100)
    b = rng.normal(0, 1, 100)
    b[0] += 50                                        # 一个离群点
    print("with outlier:", round(np.corrcoef(a, b)[0, 1], 3))
    b[0] -= 50
    print("without:", round(np.corrcoef(a, b)[0, 1], 3))

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        print("标准库思路:手写 Pearson 公式;Spearman 先转秩再做 Pearson")
