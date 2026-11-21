---
title: [Q2930] 错误码到 HTTP 状态的映射器: 注册表与一元出口
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2930 · 错误码到 HTTP 状态的映射器: 注册表与一元出口

> 难度:★★☆☆ | 标签:错误码, HTTP 状态

**问**:业务错误码和 HTTP 状态码是两套体系, 你怎么把它们组织起来? 未注册的码和意外异常怎么兜底?

**答**:注册表一张: 错误码映射到 HTTP 状态与对外文案, 业务代码只抛 BizError(code), 状态码与文案永远从表里来, 不在业务代码里散落 set_status。映射器做三层兜底: 注册过的码按表映射, 可以附 detail; 未注册的码按 500 兜底给通用文案, 错误码名可以回显方便开发者发现漏注册, 但绝不编一个状态码出去; 非业务异常一律 500, 内部细节只进日志不进响应体, 响应带 trace_id 让用户报障时能串起服务端日志。注册表自身要自检: 业务错误应映射到 4xx 段, 状态码不重复使用, 这两条在测试里断言。

```python
# file: code/03_Web后端开发/q2930_error_mapper.py
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
```

**追问**:
- 响应里为什么要带 trace_id?——用户报障时只有状态码没法查, trace_id 能直接串起服务端日志定位那一次请求。
- 注册表漏注册的码会发生什么?——按 500 兜底返回通用文案, 宁可暴露为服务端错误提醒补表, 也不能编一个状态码出去。
