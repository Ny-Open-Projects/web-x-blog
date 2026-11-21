try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import Counter
    users = [("u1", "vip"), ("u2", "normal")]
    orders = [("o1", "u1"), ("o2", "u1"), ("o3", "u2")]
    cnt = Counter(uid for _, uid in orders)
    for uid, level in users:
        print(uid, level, "订单数", cnt.get(uid, 0))
    dup = [("u1", "vip"), ("u1", "old")]  # 用户表键不唯一,m:1 校验会失败
    print("用户表键重复:", [k for k, v in Counter(u for u, _ in dup).items() if v > 1])
else:
    users = pd.DataFrame({"user_id": ["u1", "u2"], "level": ["vip", "normal"]})
    orders = pd.DataFrame({"order_id": ["o1", "o2", "o3"], "user_id": ["u1", "u1", "u2"]})
    m = orders.merge(users, on="user_id", validate="m:1")
    print(m, end="\n\n")
    bad_users = pd.DataFrame({"user_id": ["u1", "u1", "u2"], "level": ["vip", "old", "normal"]})
    try:
        orders.merge(bad_users, on="user_id", validate="m:1")
    except pd.errors.MergeError as e:
        print("键膨胀被拦截:", e)
