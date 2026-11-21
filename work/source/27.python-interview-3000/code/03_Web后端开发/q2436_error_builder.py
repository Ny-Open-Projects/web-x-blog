"""统一错误响应构造器与错误码表(纯标准库)。"""
import json
import uuid

ERRORS = {
    "validation_failed": (422, "请求参数校验失败"),
    "not_found": (404, "资源不存在"),
    "conflict": (409, "资源状态冲突"),
    "rate_limited": (429, "请求过于频繁, 请稍后重试"),
    "internal": (500, "服务内部错误"),
}


def build_error(code, details=None, request_id=None):
    """业务侧入口: 已知错误码 -> 稳定结构体, details 只放给客户端看的内容。"""
    status, message = ERRORS[code]
    rid = request_id or "req-" + uuid.uuid4().hex[:12]
    payload = {"error": {"code": code, "message": message, "request_id": rid}}
    if details:
        payload["error"]["details"] = details
    return status, json.dumps(payload, ensure_ascii=False)


def build_internal(exc, request_id=None):
    """兜底入口: 未知异常一律 500, 细节进日志不进响应体。"""
    rid = request_id or "req-" + uuid.uuid4().hex[:12]
    # 生产环境此处应把 repr(exc) 与堆栈写入结构化日志, 这里仅演示
    logged = "would log: {}: {}".format(type(exc).__name__, exc)
    status, body = build_error("internal", request_id=rid)
    return status, body, logged


# 场景一: 参数校验失败, 带字段级明细
status, body = build_error("validation_failed", details=[
    {"field": "email", "message": "格式不合法"},
    {"field": "age", "message": "必须为 0..120 的整数"},
])
print(status, body)
parsed = json.loads(body)
assert status == 422 and parsed["error"]["code"] == "validation_failed"
assert len(parsed["error"]["details"]) == 2

# 场景二: 未预期异常, 响应体不外泄内部信息
try:
    1 / 0
except ZeroDivisionError as exc:
    status, body, logged = build_internal(exc, request_id="req-fixed-01")
print(status, body)
print("日志侧:", logged)
parsed = json.loads(body)
assert status == 500
assert "ZeroDivision" not in body and "division" not in body   # 内部细节不外泄
assert parsed["error"]["request_id"] == "req-fixed-01"

# 场景三: 同一错误码的结构稳定, 客户端可按 code 分支
_, body_a = build_error("not_found", request_id="req-x")
_, body_b = build_error("not_found", request_id="req-y")
assert json.loads(body_a)["error"]["code"] == json.loads(body_b)["error"]["code"]
print("要点: 错误响应三要素 code message request_id, "
      "已知错误带 details, 未知异常只给通用文案加 request_id 让用户可追溯")
