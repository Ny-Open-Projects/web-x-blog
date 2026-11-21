"""查询参数的多值解析: 重复键聚合与逗号两种约定(FastAPI + 标准库对照)。"""
import sys

try:
    from fastapi import FastAPI, Query, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("未安装 fastapi/httpx, 降级用标准库演示核心语义:")
    from urllib.parse import parse_qs
    print("重复键 ->", parse_qs("tag=py&tag=web&tag=py"))  # 自动聚合为列表
    print("逗号式 ->", parse_qs("tag=py,web"))             # 仍是单字符串, 需业务层自行 split
    sys.exit(0)

app = FastAPI()


@app.get("/search")
def search(tags: list = Query(default=[]), page: int = Query(default=1, ge=1)):
    """参数声明成 list, FastAPI 会把同名重复键聚合成列表, 缺省为空列表。"""
    return {"tags": tags, "page": page}


@app.get("/raw")
async def raw(request: Request):
    """绕开声明式绑定: getlist 拿全量保序, get 只拿最后一个重复值, 混用会静默丢数据。"""
    return {
        "all": request.query_params.getlist("tag"),
        "last": request.query_params.get("tag"),
    }


client = TestClient(app)
r1 = client.get("/search", params=[("tags", "py"), ("tags", "web")])
assert r1.json() == {"tags": ["py", "web"], "page": 1}, r1.json()
r2 = client.get("/search", params={"tags": "py,web"})
assert r2.json()["tags"] == ["py,web"], "逗号约定到框架这层还是一个值, 切分是业务契约"
r3 = client.get("/raw", params=[("tag", "a"), ("tag", "b")])
assert r3.json() == {"all": ["a", "b"], "last": "b"}
print("重复键聚合:", r1.json()["tags"])
print("逗号约定不自动切分:", r2.json()["tags"])
print("getlist 保序拿全量, get 只剩最后一个:", r3.json())
