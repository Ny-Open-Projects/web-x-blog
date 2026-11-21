"""错误信息分级: 外部响应最小化, 内部日志保留全量(纯标准库)。"""
import traceback


class ExternalSafeError(Exception):
    """预期内错误: 消息本身可以对外。"""


def handle(handler_name, exc, request_id):
    if isinstance(exc, ExternalSafeError):
        external = {"error": "bad_request", "message": str(exc), "request_id": request_id}
        internal = "{}: {}".format(handler_name, exc)
    else:
        external = {"error": "internal_error", "message": "服务器内部错误, 请稍后重试",
                    "request_id": request_id}
        detail = "".join(traceback.format_exception_only(type(exc), exc)).strip()
        internal = "{}: {}".format(handler_name, detail)
    return external, internal


rid = "req-88f3"
safe = handle("create_order", ExternalSafeError("库存不足"), rid)
print("预期内 -> 外部:", safe[0])
print("预期内 -> 日志:", safe[1])
try:
    1 / 0
except ZeroDivisionError as exc:
    leak = handle("create_order", exc, rid)
print("预期外 -> 外部:", leak[0])
print("预期外 -> 日志:", leak[1])
assert "ZeroDivisionError" not in str(leak[0])
assert "ZeroDivisionError" in leak[1]
print("要点: 外部永不出现堆栈与内部细节, request_id 是外部与内部日志之间唯一的桥")
