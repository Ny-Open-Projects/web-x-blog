"""超时与重试的客户端契约: 预算、幂等与 Retry-After(纯标准库)。"""

CONTRACT = {
    "GET /items": {"timeout": 2.0, "retries": 2, "idempotent": True},
    "POST /orders": {"timeout": 3.0, "retries": 1, "idempotent": False, "requires_key": True},
    "POST /pay": {"timeout": 5.0, "retries": 0, "idempotent": False, "requires_key": True},
}


def validate_client(op, timeout, retries, has_key):
    """客户端配置对照契约, 返回违规列表。

    非幂等操作的重试必须携带幂等键, 否则第一次失败后的重试就是双倍下单。
    """
    c = CONTRACT[op]
    bad = []
    if timeout > c["timeout"]:
        bad.append("timeout %.1fs 超出预算 %.1fs" % (timeout, c["timeout"]))
    if retries > c["retries"]:
        bad.append("retries=%d 超出上限 %d" % (retries, c["retries"]))
    if not c["idempotent"] and retries > 0 and not (c.get("requires_key") and has_key):
        bad.append("非幂等操作重试必须携带幂等键")
    return bad


def deadline_ok(op, attempts, deadline):
    """总预算: attempts 次超时 + 重试间隔之和不得突破 deadline。"""
    return attempts * CONTRACT[op]["timeout"] <= deadline


def next_retry_after(retry_after_header, elapsed):
    """服务端给了 Retry-After 就必须等够, 客户端自己的退避只能取更长者。"""
    return max(float(retry_after_header or 0), elapsed)


assert validate_client("GET /items", 2.0, 2, False) == []
assert validate_client("GET /items", 5.0, 2, False) == ["timeout 5.0s 超出预算 2.0s"]
assert validate_client("GET /items", 2.0, 5, False) == ["retries=5 超出上限 2"]
v = validate_client("POST /orders", 3.0, 1, False)
assert v == ["非幂等操作重试必须携带幂等键"], v
assert validate_client("POST /orders", 3.0, 1, True) == []
assert validate_client("POST /pay", 5.0, 3, True) == ["retries=3 超出上限 0"], "支付不重试, 靠查询补单"
assert deadline_ok("POST /orders", 2, 6.0) and not deadline_ok("POST /orders", 3, 6.0)
assert next_retry_after("30", 10) == 30.0 and next_retry_after(None, 10) == 10
print("契约四条: 超时预算 / 重试上限 / 幂等键门槛 / Retry-After 优先")
