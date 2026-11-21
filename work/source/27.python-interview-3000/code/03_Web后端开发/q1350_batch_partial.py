"""批量接口部分成功:逐项结果 + 汇总统计(纯标准库,fastapi 可用时挂路由)。"""
try:
    from fastapi import FastAPI
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    print("[降级] 未安装 fastapi,以下用纯函数演示同一响应结构")


def process_batch(items):
    """逐项独立处理,返回 {results, summary},顺序与请求一致。"""
    results = []
    for item in items:
        try:
            if item["amount"] <= 0:
                raise ValueError("amount 必须为正数")
            results.append({"index": item["index"], "id": item["id"],
                            "status": "success", "data": {"fee": item["amount"] // 100}})
        except (KeyError, ValueError) as exc:
            results.append({"index": item.get("index"), "id": item.get("id"),
                            "status": "failed", "error": {"code": "INVALID_AMOUNT",
                                                          "message": str(exc)}})
    ok = sum(1 for r in results if r["status"] == "success")
    return {"results": results,
            "summary": {"total": len(results), "succeeded": ok, "failed": len(results) - ok}}


if HAS_FASTAPI:
    app = FastAPI()

    @app.post("/v1/fees/batch")
    def batch_route(items: list):
        return process_batch(items)
    print("[fastapi] 已注册 POST /v1/fees/batch 路由示例")

resp = process_batch([
    {"index": 0, "id": "a1", "amount": 250},
    {"index": 1, "id": "a2", "amount": -1},
    {"index": 2, "id": "a3", "amount": 80},
])
print(resp["summary"])
for r in resp["results"]:
    tail = r.get("error", {}).get("message", "ok")
    print(r["index"], r["status"], tail)
