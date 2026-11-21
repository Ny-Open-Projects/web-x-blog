"""API 版本双运行: 路由表按版本隔离, 业务内核全局共享(纯标准库)。"""

V1_TABLE = {("GET", "/orders"): "order_v1"}
V2_TABLE = {("GET", "/orders"): "order_v2", ("GET", "/orders/stats"): "stats_v2"}


def order_core(payload):
    """业务内核与版本无关, 版本差异只在出口适配。"""
    return {"id": payload.get("id", "o-100"), "amount_cents": 9900,
            "tax_cents": 900, "state": "paid"}


def order_v1(payload):
    data = order_core(payload)
    return 200, {"id": data["id"], "amount": data["amount_cents"] // 100,
                 "state": data["state"]}


def order_v2(payload):
    data = order_core(payload)
    return 200, {"id": data["id"], "amount_cents": data["amount_cents"],
                 "tax_cents": data["tax_cents"], "state": data["state"]}


def stats_v2(payload):
    return 200, {"total": 42}


HANDLERS = {"order_v1": order_v1, "order_v2": order_v2, "stats_v2": stats_v2}
ROUTES = {"v1": V1_TABLE, "v2": V2_TABLE}


def dispatch(method, path):
    parts = path.lstrip("/").split("/", 1)
    version, rest = parts[0], "/" + (parts[1] if len(parts) > 1 else "")
    table = ROUTES.get(version)
    if table is None:
        return 404, {"error": "unknown_version", "supported": sorted(ROUTES)}
    if (method, rest) not in table:
        return 404, {"error": "no_route", "version": version}
    return HANDLERS[table[(method, rest)]]({"id": "o-100"})


for method, path in [("GET", "/v1/orders"), ("GET", "/v2/orders"),
                     ("GET", "/v2/orders/stats"), ("POST", "/v1/orders"),
                     ("GET", "/v3/orders")]:
    print("{} {:18s} ->".format(method, path), dispatch(method, path))
assert dispatch("GET", "/v2/orders")[1]["amount_cents"] == 9900
print("要点: 双运行的单位是路由表与适配函数, 业务内核只有一份; v1 表存在即服务, 下线只是删表")
