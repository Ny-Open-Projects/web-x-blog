try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import Counter
    values = ["beijing", "shanghai"] * 50
    codes = {v: i for i, v in enumerate(sorted(set(values)))}
    print("类别字典:", codes)
    print("存储为 codes 列表长度:", len(values), "类别数:", len(codes))
else:
    big = pd.DataFrame({"city": ["beijing", "shanghai"] * 50_000})
    print("object 内存:", big.memory_usage(deep=True).sum())
    big["city_c"] = big["city"].astype("category")
    print("category 内存:", big["city_c"].memory_usage(deep=True).sum())
    sub = big[big["city"] == "beijing"]
    print("切片残留类别数:", len(sub["city_c"].cat.categories))
    print("清理后类别数:", len(sub["city_c"].cat.remove_unused_categories().cat.categories))
