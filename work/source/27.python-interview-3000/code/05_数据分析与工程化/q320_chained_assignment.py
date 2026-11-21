try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({"a": [1, -2, 3], "b": [0, 0, 0]})
    # 反例:df[df.a > 0]["b"] = 1  -> SettingWithCopyWarning 且可能不生效
    df.loc[df["a"] > 0, "b"] = 1       # 正解:单次 loc 赋值
    assert (df.loc[df["a"] > 0, "b"] == 1).all()
    # 需要子表操作时显式 copy
    sub = df[df["a"] > 0].copy()
    sub["b"] = 99
    print(df, "\n---\n", sub)

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        rows = [{"a": 1, "b": 0}, {"a": -2, "b": 0}, {"a": 3, "b": 0}]
        for r in rows:               # 单次遍历完成定位与赋值
            if r["a"] > 0:
                r["b"] = 1
        print(rows)
