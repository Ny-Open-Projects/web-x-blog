"""上卷与下钻的口径一致性: 可加度量与不可加度量"""

# 事实明细: 区域, 城市, 用户, 金额
FACT = [
    ("华北", "北京", "u1", 120), ("华北", "北京", "u2", 80),
    ("华北", "天津", "u2", 60), ("华北", "天津", "u3", 40),
    ("华东", "上海", "u1", 200), ("华东", "上海", "u4", 150),
    ("华东", "杭州", "u4", 90), ("华东", "杭州", "u5", 70),
]
CITY_REGION = {"北京": "华北", "天津": "华北", "上海": "华东", "杭州": "华东"}


def rollup(rows, level):
    """按粒度重算: 金额求和, 用户数去重计数, 全部从明细出发"""
    agg = {}
    for region, city, user, amount in rows:
        key = city if level == "city" else CITY_REGION[city]
        cell = agg.setdefault(key, {"amount": 0, "users": set()})
        cell["amount"] += amount
        cell["users"].add(user)
    return {k: {"amount": v["amount"], "users": len(v["users"])} for k, v in agg.items()}


if __name__ == "__main__":
    by_city = rollup(FACT, "city")
    by_region = rollup(FACT, "region")
    print("城市粒度:", {k: v for k, v in sorted(by_city.items())})
    print("区域粒度:", {k: v for k, v in sorted(by_region.items())})
    # 可加度量: 金额上卷 = 子层求和, 守恒成立
    for region in ["华北", "华东"]:
        cities = [c for c in by_city if CITY_REGION[c] == region]
        sum_city = sum(by_city[c]["amount"] for c in cities)
        ok = sum_city == by_region[region]["amount"]
        print(f"{region}: 城市金额求和 {sum_city} = 区域重算 {by_region[region]['amount']} -> {'一致' if ok else '不一致'}")
        assert ok, "金额是可加度量, 上卷必须守恒"
    # 不可加度量: 用户数不能把子层数字相加
    for region in ["华北", "华东"]:
        cities = [c for c in by_city if CITY_REGION[c] == region]
        naive = sum(by_city[c]["users"] for c in cities)
        true_n = by_region[region]["users"]
        print(f"{region}: 城市用户数直加 {naive} vs 区域去重重算 {true_n} -> {'虚高' if naive > true_n else '一致'}")
        assert naive > true_n, "跨城市重复用户应导致直加虚高"
    print("要点: 可加度量才能逐层求和, distinct 类度量每层必须回明细重算, 口径字典要逐条标注可加性")
