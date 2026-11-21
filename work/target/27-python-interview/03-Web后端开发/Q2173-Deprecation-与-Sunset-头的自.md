---
title: [Q2173] Deprecation 与 Sunset 头的自动注入
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2173 · Deprecation 与 Sunset 头的自动注入

> 难度:★★★☆ | 标签:HTTP, 弃用治理

**问**:弃用一个路由时,Deprecation 和 Sunset 响应头应该怎么规范地发?散落在 handler 里写行吗?

**答**:弃用信息应该由注册表统一驱动、中间件统一注入,路由代码零感知。注册表登记弃用路由的弃用日期、Sunset 日期与替代路径;中间件按路径查表,命中则追加:Deprecation: true(或草稿规范的结构化日期)、Sunset 用 HTTP 日期(机器可读的下线时刻)、Link rel="sunset" 指向替代端点或公告页、可选 Warning 299 给人类看。这样做的收益是可审计——注册表就是弃用清单,直接生成调用方盘点报表与倒计时告警;散落在 handler 里手写会漏、会拼错日期格式,也无法统一监控。Sunset 日期一经对外公布就尽量不要改,改了要提前公告。

```python
# file: code/03_Web后端开发/q2173_deprecation_headers.py
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
```

**追问**:
- 客户端怎么自动感知弃用?——代理层聚合 Sunset 头生成弃用看板,SDK 在响应头出现 Sunset 时打告警日志。
- 弃用头会增加响应体量吗?——四个头约 200 字节,全站弃用路由数量有限,可忽略;缓存层要保证弃用头不被中间缓存剥离。
