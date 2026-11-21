"""接口弃用:Deprecation/Sunset 头与调用方盘点(纯标准库,fastapi 可用时挂路由)。"""
from datetime import date

try:
    from fastapi import FastAPI
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    print("[降级] 未安装 fastapi,以下用纯函数演示同一逻辑")

ROUTES = {
    "GET /v1/orders": {"sunset": date(2026, 12, 31)},
    "GET /v2/orders": {"sunset": None},
}
audit = {}   # path -> {caller: count}


def handle(method_path, today, caller="api-key-unknown"):
    meta = ROUTES[method_path]
    headers = {}
    if meta["sunset"]:
        headers["Deprecation"] = "true"
        headers["Sunset"] = meta["sunset"].strftime("%a, %d %b %Y") + " 00:00:00 GMT"
        headers["Link"] = '<https://docs.example.com/migrate>; rel="sunset"'
        audit.setdefault(method_path, {})
        audit[method_path][caller] = audit[method_path].get(caller, 0) + 1
        if today > meta["sunset"]:
            return 410, headers
    return 200, headers


if HAS_FASTAPI:
    app = FastAPI()

    @app.get("/v1/orders")
    def orders_v1():
        status, headers = handle("GET /v1/orders", date.today())
        return status, headers
    print("[fastapi] 已注册带 Sunset 逻辑的 /v1/orders 示例路由")

print(handle("GET /v1/orders", date(2026, 11, 2)))
print(handle("GET /v1/orders", date(2027, 1, 5)))
handle("GET /v1/orders", date(2027, 1, 5), caller="partner-x")
handle("GET /v1/orders", date(2027, 1, 5), caller="partner-x")
handle("GET /v1/orders", date(2027, 1, 5), caller="mobile-app")
print("待迁移调用方排行:", sorted(audit["GET /v1/orders"].items(), key=lambda kv: -kv[1]))
