"""访问日志的完整字段: 从请求与响应中提取一行结构化 JSON(纯标准库)。"""
import json
import time
import uuid

TRUSTED_PROXIES = {"10.0.0.2"}  # 只有直连方是可信代理时, 才采信 XFF 链
UA_KEY = "user-agent"


def client_ip(headers, remote_addr):
    """真实客户端 IP: 可信代理链内才采信 XFF 最左值, 否则用直连地址防伪造。"""
    xff = headers.get("x-forwarded-for")
    if xff and remote_addr in TRUSTED_PROXIES:
        return xff.split(",")[0].strip()
    return remote_addr


def log_line(request, response, started_wall, started_mono, user=None):
    """一行访问日志的完整字段; 字段有但值可缺, 键名永远稳定。"""
    duration_ms = int((time.monotonic() - started_mono) * 1000)
    path, _, query = request["path"].partition("?")
    headers = request.get("headers", {})
    record = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started_wall)),
        "request_id": request.get("request_id") or uuid.uuid4().hex,
        "method": request["method"],
        "route": request.get("route", path),      # 低基数路由模板, 便于聚合
        "path": path,
        "query_bytes": len(query),                # 不落原文, 查询串可能带令牌
        "status": response["status"],
        "bytes_out": response.get("bytes_out", 0),
        "duration_ms": duration_ms,
        "client_ip": client_ip(headers, request.get("remote_addr", "-")),
        "scheme": headers.get("x-forwarded-proto", "http"),
        "user": user or request.get("user", "anonymous"),
        "ua": headers.get(UA_KEY, "-"),
        "error": response.get("error"),
    }
    return json.dumps(record, ensure_ascii=False, separators=(",", ":"))


# 请求一: 正常 200, 经过可信代理, XFF 指向真实客户端
started_wall = time.time() - 0.12
started_mono = time.monotonic() - 0.12
req1 = {
    "request_id": "req-0001", "method": "GET",
    "path": "/api/users/42", "route": "GET /api/users/{id}",
    "remote_addr": "10.0.0.2", "user": "alice",
    "headers": {"x-forwarded-for": "203.0.113.7, 10.0.0.2",
                "x-forwarded-proto": "https", "user-agent": "demo-agent/1.0"},
}
line1 = log_line(req1, {"status": 200, "bytes_out": 358}, started_wall, started_mono)
rec1 = json.loads(line1)
print("日志一:", line1)
assert rec1["client_ip"] == "203.0.113.7", "可信链内取 XFF 最左"
assert rec1["scheme"] == "https" and rec1["route"].endswith("{id}")
assert rec1["status"] == 200 and rec1["error"] is None

# 请求二: 直连且伪造 XFF -> 必须落直连地址
req2 = {"method": "POST", "path": "/api/orders?token=secret-value",
        "remote_addr": "198.51.100.9",
        "headers": {"x-forwarded-for": "1.2.3.4", "user-agent": "curl/8"}}
line2 = log_line(req2, {"status": 201, "bytes_out": 64}, time.time(), time.monotonic())
rec2 = json.loads(line2)
print("日志二:", line2)
assert rec2["client_ip"] == "198.51.100.9", "不可信直连不采信 XFF"
assert "secret-value" not in line2, "查询串原文不落日志"

# 请求三: 5xx 带 error 字段, 便于按 error 聚合告警
req3 = {"method": "POST", "path": "/api/orders", "remote_addr": "10.0.0.3",
        "request_id": "req-0003", "headers": {}}
line3 = log_line(req3, {"status": 500, "bytes_out": 120, "error": "ValueError"},
                 time.time(), time.monotonic())
rec3 = json.loads(line3)
print("日志三:", line3)
assert rec3["error"] == "ValueError" and rec3["user"] == "anonymous"

# 字段完整性: 三条日志键集合一致, 采集端才能按列解析
k1, k2, k3 = set(rec1), set(rec2), set(rec3)
assert k1 == k2 == k3
print("字段集:", ",".join(sorted(k1)))
print("访问日志字段演示通过")
