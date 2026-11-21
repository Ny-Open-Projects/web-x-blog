try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    wide = pd.DataFrame({
        "month": ["2026-01", "2026-02"],
        "gmv": [100, 120],
        "uv": [30, 35],
    })
    long = wide.melt(id_vars="month", var_name="metric", value_name="val")
    print(long)                              # 宽转长
    back = long.pivot(index="month", columns="metric", values="val")
    back.columns.name = None
    print(back)                              # 长转宽
    # 长表带重复键时用 pivot_table 聚合
    pt = long.pivot_table(index="metric", values="val", aggfunc="sum")
    print(pt)

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        wide = [{"month": "2026-01", "gmv": 100, "uv": 30},
                {"month": "2026-02", "gmv": 120, "uv": 35}]
        long = [{"month": r["month"], "metric": k, "val": v}
                for r in wide for k, v in r.items() if k != "month"]
        for row in long:
            print(row)
