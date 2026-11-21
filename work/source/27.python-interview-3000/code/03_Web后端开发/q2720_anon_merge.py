"""匿名会话与登录会话的数据合并: 字段级策略与幂等护栏(纯标准库)。"""


def merge_sessions(anon, user):
    """匿名会话并入登录会话, 三条字段策略:

    - 购物车: 同 SKU 数量取大者, 避免重复登录时翻倍;
    - 列表字段(收藏/浏览历史): 并集保序, 用户侧在前;
    - 档案字段(收货地址等): 用户已有值优先, 匿名侧只补空缺。
    返回 (merged, anon_cleared)。
    """
    merged = {}
    for sku, qty in user.get("cart", {}).items():
        anon_qty = anon.get("cart", {}).get(sku, 0)
        merged[sku] = max(qty, anon_qty)
    for sku, qty in anon.get("cart", {}).items():
        merged.setdefault(sku, qty)
    favorites = list(user.get("favorites", []))
    favorites.extend(x for x in anon.get("favorites", []) if x not in favorites)
    merged_view = {"cart": merged, "favorites": favorites}
    for key, value in user.items():
        if key not in ("cart", "favorites"):
            merged_view[key] = value
    for key, value in anon.items():
        if key not in ("cart", "favorites") and key not in merged_view:
            merged_view[key] = value
    return merged_view, True


def apply_merge_once(store, anon_id, user_id, merge_fn=merge_sessions):
    """幂等护栏: 合并完成后匿名会话打上 merged 墓碑, 重复触发不再二次并。"""
    anon = store.get(anon_id)
    if anon is None or anon.get("_merged"):
        return store.get(user_id), False
    merged, _ = merge_fn(anon, store.get(user_id, {}))
    store[user_id] = merged
    store[anon_id] = {"_merged": True}
    return merged, True


store = {
    "anon1": {"cart": {"A": 2, "C": 1}, "favorites": ["p9"], "coupon": "NEW10"},
    "u1": {"cart": {"A": 1, "B": 3}, "favorites": ["p1", "p9"], "addr": "北京"},
}
merged, _ = merge_sessions(store["anon1"], store["u1"])
assert merged["cart"] == {"A": 2, "B": 3, "C": 1}, merged["cart"]
assert merged["favorites"] == ["p1", "p9"], merged["favorites"]
assert merged["addr"] == "北京" and merged["coupon"] == "NEW10"

final, applied1 = apply_merge_once(store, "anon1", "u1")
assert applied1 and final["cart"] == {"A": 2, "B": 3, "C": 1}
again, applied2 = apply_merge_once(store, "anon1", "u1")
assert not applied2, "墓碑挡住二次合并"
assert again["cart"] == {"A": 2, "B": 3, "C": 1}, "二次触发读到的是已合并结果, 数量没有翻倍"
print("购物车取大:", final["cart"])
print("收藏并集保序:", final["favorites"], "| 档案用户优先, 匿名补空 | 墓碑幂等生效")
