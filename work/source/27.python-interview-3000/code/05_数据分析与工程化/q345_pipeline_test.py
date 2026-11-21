"""用 pytest 风格编写数据转换测试(可 python 345_pipeline_test.py 直接跑)。"""
try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def transform(df):
    df = df.copy()
    df["total"] = df["price"] * df["qty"]
    return df[df["total"] > 0]

def test_transform_basic():
    df = pd.DataFrame({"price": [2.0, -1.0], "qty": [3, 5]})
    out = transform(df)
    assert len(out) == 1                  # 负金额被过滤
    assert out["total"].iloc[0] == 6.0

def test_transform_empty():
    df = pd.DataFrame({"price": [], "qty": []})
    assert transform(df).empty            # 空输入不抛错

if __name__ == "__main__":
    if PANDAS:
        test_transform_basic()
        test_transform_empty()
        print("all tests passed")
    else:
        print("需 pandas 演示;标准库可用 dict 列表 + 断言函数替代")
