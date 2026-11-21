"""夹具工厂进阶:默认值覆盖、嵌套构造与序列计数器,测试数据一行造好"""

COUNTERS = {}


def seq(name):
    COUNTERS[name] = COUNTERS.get(name, 0) + 1
    return COUNTERS[name]


def make_user(**overrides):
    user = {"uid": f"u{seq('user'):04d}", "city": "华东", "vip": False, "age": 25}
    user.update(overrides)
    return user


def make_order(user=None, **overrides):
    """嵌套构造:订单工厂自动带出一个用户工厂,可用参数替换"""
    u = user or make_user()
    order = {"order_id": f"o{seq('order'):05d}", "uid": u["uid"],
             "amount": 100, "status": "paid"}
    order.update(overrides)
    order["_user"] = u
    return order


def make_orders(n, **common):
    """批量场景:共享特征,键唯一"""
    return [make_order(**common) for _ in range(n)]


if __name__ == "__main__":
    u = make_user(city="华北", vip=True)
    o = make_order(user=u, amount=250)
    batch = make_orders(3, status="created")
    print("定制用户:", u)
    print("嵌套订单:", {k: v for k, v in o.items() if k != "_user"})
    for b in batch:
        print("  批量:", b["order_id"], b["uid"], b["status"])
    print("要点:工厂=默认值+覆盖+序列号,嵌套工厂控制对象图;工厂造数据,pytest fixture 管生命周期,两者分工不混")
