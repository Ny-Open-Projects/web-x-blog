import csv
import os
import tempfile

path = os.path.join(tempfile.gettempdir(), "q1069_sales.csv")
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["user_id", "city", "amount"])
    for i in range(5000):
        w.writerow([i % 500, f"c{i % 3}", i % 97])

try:
    import pandas as pd
    total, n = 0.0, 0
    for chunk in pd.read_csv(path, usecols=["user_id", "amount"], dtype={"user_id": "int32"}, chunksize=1000):
        total += chunk["amount"].sum()
        n += len(chunk)
    print(f"分块读完 {n} 行,amount 合计 {total:.0f}")
except ImportError:
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"标准库读完 {len(rows)} 行,amount 合计 {sum(int(r['amount']) for r in rows)}")
print("Parquet 进阶:pyarrow.parquet.read_table(path, filters=[('city','=','c1')]) 谓词下推只读命中行组")
