"""访问日志的字段契约设计: 必填项、枚举与基数纪律(纯标准库)。"""
import json
import re

REQUIRED = ["ts", "service", "method", "route_template", "status",
            "duration_ms", "request_id", "client_ip", "user_id", "outcome"]
ENUMS = {"method": {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"},
         "outcome": {"success", "client_error", "server_error", "redirect"}}
ROUTE_TEMPLATE = re.compile(r"^/[^\s]*$")


def validate_log(record):
    """校验一条访问日志是否符合字段契约, 返回问题列表。

    基数纪律: route_template 必须是模板而非原始路径, 否则聚合维度爆炸。
    """
    problems = []
    missing = [f for f in REQUIRED if f not in record]
    if missing:
        problems.append("缺少必填字段: " + ", ".join(missing))
    method = record.get("method")
    if method and method not in ENUMS["method"]:
        problems.append("method 不在枚举内: " + str(method))
    outcome = record.get("outcome")
    if outcome and outcome not in ENUMS["outcome"]:
        problems.append("outcome 不在枚举内: " + str(outcome))
    route = record.get("route_template")
    if route and not ROUTE_TEMPLATE.match(route):
        problems.append("route_template 不是路径模板")
    if route and re.search(r"/\d{4,}|/[0-9a-f-]{16,}", route):
        problems.append("route_template 疑似泄漏了原始 ID, 应换成 {id} 模板")
    if "user_id" in record and record["user_id"] and len(record["user_id"]) > 64:
        problems.append("user_id 过长, 疑似误放了凭证材料")
    return problems


good = {"ts": "2026-11-05T03:14:15.926Z", "service": "order-api",
        "method": "GET", "route_template": "/api/orders/{id}",
        "status": 200, "duration_ms": 34, "request_id": "req-9f3ab",
        "client_ip": "10.2.3.4", "user_id": "u-1024", "outcome": "success"}
print("好样本:", validate_log(good) or "通过")

bad = {"ts": "2026-11-05T03:14:16.000Z", "service": "order-api",
       "method": "FETCH", "route_template": "/api/orders/981273817238",
       "status": 500, "duration_ms": 980,
       "request_id": "req-771", "client_ip": "10.2.3.5",
       "user_id": "eyJhbGciOiJIUzI1NiJ9", "outcome": "timeout"}
problems = validate_log(bad)
for p in problems:
    print("坏样本问题 ->", p)
assert len(problems) >= 3

print(json.dumps(good, ensure_ascii=False, sort_keys=True)[:110], "...")
print("要点: 字段契约先于日志上线, 模板化路径保证聚合维度有限, 枚举字段让告警规则可依赖")
