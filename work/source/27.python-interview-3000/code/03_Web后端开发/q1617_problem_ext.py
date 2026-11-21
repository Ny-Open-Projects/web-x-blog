"""RFC 7807 的 type 目录注册与扩展成员演进(纯标准库)。"""
import json

# 错误目录: type URI 是机器可读的"错误种类", 一旦发布语义就要稳定
CATALOG = {
    "insufficient-funds": "https://api.example.com/problems/insufficient-funds",
    "invalid-param": "https://api.example.com/problems/invalid-param",
}


def problem(kind, status, title, detail=None, **ext):
    uri = CATALOG.get(kind)
    if uri is None:
        raise ValueError(f"未注册的错误类型: {kind}")     # 由调用处捕获
    body = {"type": uri, "title": title, "status": status}
    if detail:
        body["detail"] = detail
    body.update(ext)
    return body


# 扩展成员只能增不能删不能改语义: 老客户端按字段名读, 新增字段对它们不可见
v1 = problem("insufficient-funds", 422, "余额不足", detail="需要 120 元", balance=80.0)
v2 = problem("insufficient-funds", 422, "余额不足", detail="需要 120 元",
             balance=80.0, required=120.0, currency="CNY")
print("v1:", json.dumps(v1, ensure_ascii=False))
print("v2:", json.dumps(v2, ensure_ascii=False))
old_clients = {k: v2[k] for k in v1 if k in v2}
print("老客户端可见字段不变:", old_clients == v1)

try:
    problem("unknown-kind", 500, "x")
except ValueError as e:
    print("未注册类型被拦下:", e)
