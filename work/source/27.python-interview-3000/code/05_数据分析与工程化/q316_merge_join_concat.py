try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    orders = pd.DataFrame({"uid": [1, 2, 2, 3], "amt": [10, 20, 30, 40]})
    users = pd.DataFrame({"uid": [1, 2, 2], "name": ["a", "b", "b2"]})
    # 陷阱演示:users 的 uid 重复,join 后行数膨胀
    m = orders.merge(users, on="uid", how="left")
    assert len(m) > len(orders), "键不唯一导致笛卡尔积"
    print(len(orders), "->", len(m))
    # 生产守则:先验证唯一性再 merge
    assert users["uid"].is_unique, "users.uid 存在重复"
    concat_df = pd.concat([orders, orders], ignore_index=True)
    print(concat_df.shape)

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        orders = [(1, 10), (2, 20), (2, 30), (3, 40)]
        users = {1: "a", 2: "b"}  # 唯一键字典,天然防重复
        for uid, amt in orders:
            print(uid, amt, users.get(uid))
