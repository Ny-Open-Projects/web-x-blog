try:
    from fastapi import FastAPI
    from fastapi.openapi.utils import get_openapi
except ImportError:
    print("pip install fastapi 后再运行")
    raise SystemExit(0)

app = FastAPI(
    title="订单服务",
    version="2.1.0",
    description="内部订单 API",
    openapi_tags=[{"name": "orders", "description": "订单相关"}],
)

@app.get("/orders", tags=["orders"])
def list_orders():
    return []

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(title=app.title, version=app.version,
                         description=app.description, routes=app.routes)
    schema["info"]["x-contact"] = "team-orders@example.com"
    app.openapi_schema = schema
    return app.openapi_schema

app.openapi = custom_openapi
spec = app.openapi()
print(spec["info"]["title"], spec["info"].get("x-contact"))
