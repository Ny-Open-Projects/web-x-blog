"""错误码到 HTTP 状态的映射器: 注册表 + 兜底 + 异常一元出口(纯标准库)。"""

ERROR_REGISTRY = {
    "USER_NOT_FOUND": (404, "用户不存在"),
    "USER_LOCKED": (423, "账号已锁定"),
    "QUOTA_EXCEEDED": (429, "配额不足"),
    "PAYMENT_DECLINED": (402, "支付被拒绝"),
    "VALIDATION_FAILED": (422, "请求参数不合法"),
}


class BizError(Exception):
    """业务异常只带错误码; HTTP 状态与对外文案一律从注册表来。"""

    def __init__(self, code, detail=None):
        self.code = code
        self.detail = detail
        entry = ERROR_REGISTRY.get(code)
        if entry:
            self.http_status, self.user_message = entry
        else:
            self.http_status, self.user_message = 500, "服务内部错误"


def to_response(err, trace_id=""):
    body = {"code": err.code, "message": err.user_message}
    if err.detail:
        body["detail"] = err.detail
    if trace_id:
        body["trace_id"] = trace_id
    return err.http_status, body


def handle(fn, *args, **kwargs):
    """一元出口: 业务异常按表映射, 其余异常一律 500 且不外泄内部细节。"""
    try:
        return 200, fn(*args, **kwargs)
    except BizError as e:
        return to_response(e, trace_id="trace-demo-01")
    except Exception:
        return 500, {"code": "INTERNAL", "message": "服务内部错误", "trace_id": "trace-demo-01"}


def get_user(uid):
    if uid == 404:
        raise BizError("USER_NOT_FOUND", "uid=%d" % uid)
    if uid == 423:
        raise BizError("USER_LOCKED")
    if uid == 999:
        raise BizError("CODE_TYPO_NOT_REGISTERED")
    if uid == 500:
        raise RuntimeError("connection refused")  # 内部故障细节只进日志
    return {"uid": uid, "name": "alice"}


status, body = handle(get_user, 1)
print("正常路径:", status, body)
assert status == 200

status, body = handle(get_user, 404)
print("注册码映射:", status, body)
assert (status, body["code"]) == (404, "USER_NOT_FOUND")

status, body = handle(get_user, 423)
assert (status, body["message"]) == (423, "账号已锁定")

status, body = handle(get_user, 999)
print("未注册码兜底 -> 500 通用文案, 错误码名可回显但细节不外泄:", body)
assert status == 500 and body["message"] == "服务内部错误" and "detail" not in body

status, body = handle(get_user, 500)
print("未知异常兜底:", status, body)
assert status == 500 and "connection refused" not in str(body), "内部细节不进响应体"

# 注册表自检: 状态码段位要跟语义一致, 4xx 业务错 5xx 系统错
for code, (http_status, _) in ERROR_REGISTRY.items():
    assert 400 <= http_status < 500, "%s 应映射到 4xx 段" % code
assert len({v[0] for v in ERROR_REGISTRY.values()}) == len(ERROR_REGISTRY), "状态码不重复使用"
print("错误码映射器演示通过")
