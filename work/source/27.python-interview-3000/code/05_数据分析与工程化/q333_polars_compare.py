try:
    import polars as pl
    HAS_POLARS = True
except ImportError:
    HAS_POLARS = False

def demo_polars():
    df = pl.DataFrame({"city": ["BJ", "SH", "BJ"], "amt": [10, 20, 30]})
    out = (
        df.lazy()
          .filter(pl.col("amt") > 5)            # 谓词下推
          .group_by("city")
          .agg(pl.col("amt").sum().alias("total"))
          .collect()                             # 此时才执行优化后的 plan
    )
    print(out)

if __name__ == "__main__":
    if HAS_POLARS:
        demo_polars()
    else:
        # 标准库演示同语义:filter -> group -> agg
        rows = [("BJ", 10), ("SH", 20), ("BJ", 30)]
        groups = {}
        for city, amt in rows:
            if amt > 5:
                groups[city] = groups.get(city, 0) + amt
        print(groups)
