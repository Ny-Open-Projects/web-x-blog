try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    fact = pd.DataFrame({                       # 事实表:度量 + 外键
        "order_id": [1, 2, 3],
        "user_key": [10, 11, 10],
        "item_key": [100, 101, 100],
        "amount": [100.0, 50.0, 30.0],
    })
    dim_user = pd.DataFrame({"user_key": [10, 11],
                             "city": ["BJ", "SH"]})   # 维度表
    dim_item = pd.DataFrame({"item_key": [100, 101],
                             "category": ["book", "toy"]})
    # 星型模型典型查询:度量沿维度汇聚
    out = (fact.merge(dim_user, on="user_key")
               .merge(dim_item, on="item_key")
               .groupby("city")["amount"].sum())
    print(out)

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        fact = [(1, 10, 100, 100.0), (2, 11, 101, 50.0), (3, 10, 100, 30.0)]
        dim_user = {10: "BJ", 11: "SH"}
        dim_item = {100: "book", 101: "toy"}
        agg = {}
        for _, u, i, amt in fact:
            agg[dim_user[u]] = agg.get(dim_user[u], 0) + amt
        print(agg)
