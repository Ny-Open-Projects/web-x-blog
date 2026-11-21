"""弃用治理: Deprecation 与 Sunset 头按注册表自动注入(纯标准库)。"""
from datetime import datetime, timezone
from email.utils import format_datetime

DEPRECATIONS = {
    "/v1/orders": {"sunset": datetime(2027, 3, 1, tzinfo=timezone.utc),
                   "successor": "/v2/orders"},
}


def apply_deprecation(path, headers):
    """命中弃用注册表则注入弃用响应头; 返回新头与是否命中。"""
    info = DEPRECATIONS.get(path)
    if info is None:
        return headers, False
    headers = dict(headers)
    headers["Deprecation"] = "true"
    headers["Sunset"] = format_datetime(info["sunset"], usegmt=True)
    headers["Link"] = '<{}>; rel="sunset"'.format(info["successor"])
    headers["Warning"] = '299 - "route deprecated, migrate to {}"'.format(info["successor"])
    return headers, True


def proxy(path):
    headers, flagged = apply_deprecation(path, {"Content-Type": "application/json"})
    return {"status": 200, "headers": headers, "deprecated": flagged}


for path in ["/v2/orders", "/v1/orders"]:
    resp = proxy(path)
    print("==", path, "status", resp["status"], "(弃用)" if resp["deprecated"] else "")
    if resp["deprecated"]:
        for key in ["Deprecation", "Sunset", "Link", "Warning"]:
            print("   {}: {}".format(key, resp["headers"][key]))
now = datetime(2026, 11, 5, tzinfo=timezone.utc)
remain = (DEPRECATIONS["/v1/orders"]["sunset"] - now).days
print("距 Sunset 还有 {} 天, 监控按弃用路由统计调用量与调用方分布".format(remain))
print("要点: 注册表即弃用清单, 中间件注入保证头一致且可审计; Sunset 用 HTTP 日期保证机器可读")
