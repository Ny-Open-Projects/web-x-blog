try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    print("标准库演示:滞后特征只用过去,标准化只用训练段统计")
    ys = [10, 11, 12, 13, 14, 100]
    train = ys[:4]
    mu = sum(train) / len(train)
    for i, y in enumerate(ys):
        lag1 = ys[i - 1] if i > 0 else None
        z = (y - mu) / (sum((t - mu) ** 2 for t in train) / len(train)) ** 0.5
        print(f"t{i} y={y} lag1={lag1} z_train_std={z:.2f}")
else:
    df = pd.DataFrame({"t": range(6), "y": [10, 11, 12, 13, 14, 100]})
    # 正确:滞后特征,只用过去
    df["lag1"] = df["y"].shift(1)
    train = df.iloc[:4]
    # 错误:全量标准化把验证期 100 算进均值方差
    df["z_bad"] = (df["y"] - df["y"].mean()) / df["y"].std()
    # 正确:统计量只用训练段
    df["z_good"] = (df["y"] - train["y"].mean()) / train["y"].std()
    print(df.round(2))
    assert df["z_bad"].round(6).tolist() != df["z_good"].round(6).tolist(), "两种口径应有差异"
    print("两种口径数值不同,说明全量统计确实泄露了验证期信息")
