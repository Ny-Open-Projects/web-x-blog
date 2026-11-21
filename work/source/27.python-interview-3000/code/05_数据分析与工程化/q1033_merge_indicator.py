try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    a = {"k1", "k2", "k3"}
    b = {"k2", "k3", "k4"}
    print("仅左表:", a - b, "仅右表:", b - a, "两侧都有:", a & b)
else:
    orders = pd.DataFrame({"order_id": ["o1", "o2", "o3"], "user_id": ["u1", "u2", "u9"]})
    users = pd.DataFrame({"user_id": ["u1", "u2", "u7"], "level": ["vip", "normal", "vip"]})
    m = orders.merge(users, on="user_id", how="outer", indicator=True)
    print(m, end="\n\n")
    print(m["_merge"].value_counts())
    orphans = m.loc[m["_merge"] == "left_only", "user_id"]
    print("孤儿订单的用户:", orphans.tolist())
