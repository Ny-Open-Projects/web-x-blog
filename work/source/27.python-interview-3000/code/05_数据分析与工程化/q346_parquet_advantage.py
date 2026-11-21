import json
import os

def write_csv_like(rows, path):
    """模拟 CSV:全文本、无类型。"""
    with open(path, "w") as f:
        for r in rows:
            f.write(",".join(str(v) for v in r.values()) + "\n")

if __name__ == "__main__":
    try:
        import pandas as pd
        df = pd.DataFrame({"id": [1, 2, 3],
                           "ts": pd.to_datetime(["2026-01-01"] * 3),
                           "amt": [1.5, 2.5, 3.5]})
        df.to_parquet("demo.parquet")          # 需 pyarrow
        back = pd.read_parquet("demo.parquet", columns=["id", "amt"])  # 列裁剪
        print(back.dtypes.to_dict(), back.shape)   # 类型无损
        os.remove("demo.parquet")
    except ImportError:
        rows = [{"id": 1, "ts": "2026-01-01", "amt": 1.5}]
        write_csv_like(rows, "demo.csv")
        print("CSV 无类型:读到的都是字符串,需要重新解析")
        print(open("demo.csv").read())
        os.remove("demo.csv")
