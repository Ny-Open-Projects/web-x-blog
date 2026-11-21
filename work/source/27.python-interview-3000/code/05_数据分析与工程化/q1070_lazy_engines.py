import csv
import os
import tempfile

path = os.path.join(tempfile.gettempdir(), "q1070_events.csv")
if not os.path.exists(path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["city", "amount"])
        for i in range(20000):
            w.writerow([f"c{i % 4}", i % 100])

used = "stdlib"
try:
    import polars as pl
    used = "polars"
    res = (
        pl.scan_csv(path)
        .group_by("city")
        .agg(pl.col("amount").sum().alias("total"))
        .sort("city")
        .collect()
    )
    print(res)
except ImportError:
    try:
        import duckdb
        used = "duckdb"
        print(duckdb.sql(f"SELECT city, sum(amount) AS total FROM read_csv_auto('{path}') GROUP BY city ORDER BY city"))
    except ImportError:
        from collections import defaultdict
        agg = defaultdict(int)
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                agg[row["city"]] += int(row["amount"])
        for k in sorted(agg):
            print(k, agg[k])
print("引擎:", used, "- lazy 计划把过滤与投影下推到数据源,避免全量进内存")
