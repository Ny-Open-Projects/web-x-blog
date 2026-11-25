---
title: "[Q6180] CSRF_TRUSTED_ORIGINS 方案错配导致全站 POST 403"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6180 · CSRF_TRUSTED_ORIGINS 方案错配导致全站 POST 403

难度：P6 ｜ 标签：Django、CSRF、Origin、SECURE_PROXY_SSL_HEADER、TLS 终止

**问**：Django 服务迁到 ALB 后，所有 GET 正常，但登录/下单等 POST 全部 403，日志写 `Origin checking failed - https://app.example.com does not match any trusted origins`。`CSRF_TRUSTED_ORIGINS` 明明加了域名，为什么还是不过？为什么报错里是 https、Django 却认为不匹配？`SECURE_PROXY_SSL_HEADER` 和 `CSRF_TRUSTED_ORIGINS` 各自该在什么层面解决问题？两者都配会不会互相打架？

**答**：
结论：Django 4 的 CSRF 校验会用 `request.is_secure()` + `Host` 拼出"本站 origin"，再和请求的 `Origin`/`Referer` 比较。TLS 在 ALB 终止时，应用收到的是 HTTP，`request.is_secure()` 为 `False`，于是本站 origin 被拼成 `http://app.example.com`；浏览器发来的是 `https://app.example.com`，不相等；`CSRF_TRUSTED_ORIGINS` 里的条目必须**带 scheme**（`https://app.example.com`），如果只写裸域名 `app.example.com` 或不写协议，Django 不认。两层修复：a) 用 `SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")` 让 `is_secure()` 正确；b) 在 `CSRF_TRUSTED_ORIGINS` 里列出带 scheme 的可信源（支持 `https://*.example.com` 通配子域）。两者不冲突：前者修正"本站是谁"，后者是"额外信任哪些源"。

取舍：最干净的是让 `is_secure()` 正确，这样 CSRF、Secure Cookie、`SECURE_SSL_REDIRECT`、HSTS 全都受益；但前提是只信任来自 LB 的 `X-Forwarded-Proto`，边缘必须剥离客户端伪造的头（Q6174）。`CSRF_TRUSTED_ORIGINS` 是"我确实有多个合法前端域名/协议"时的白名单，不要为了绕过问题把 `https://*.example.com` 开得过宽，更不要加 `http://`（会削弱 CSRF 防护）。

实战：事故形态是"迁移当天所有写操作 403，读操作正常；开发本地 http 复现不了"。下面模拟 Django 的 origin 判定：TLS 终止但 `is_secure=False` 时，`https://` 的 Origin 不匹配 `http://` 的本站；配了代理头后匹配；或者用带 scheme 的 trusted 白名单兜底。注意 trusted 里写裸域名仍然无效。

```python
def django_csrf_origin_ok(origin, host, is_secure, trusted_origins):
    scheme = "https" if is_secure else "http"
    good_origin = f"{scheme}://{host}"
    if origin == good_origin:
        return True
    return origin in trusted_origins


cases = [
    ("TLS 在 LB 终止，未配 SECURE_PROXY_SSL_HEADER", False, set()),
    ("配了 SECURE_PROXY_SSL_HEADER，is_secure=True", True, set()),
    ("is_secure 仍为 False，但 trusted 带 scheme", False, {"https://app.example.com"}),
]

for label, secure, trusted in cases:
    ok = django_csrf_origin_ok("https://app.example.com", "app.example.com", secure, trusted)
    print(f"{label:44} -> {ok}")

print("trusted 写成裸域名也无效:",
      django_csrf_origin_ok("https://app.example.com", "app.example.com", False,
                            {"app.example.com"}))
```

**追问一**：为什么只有 POST/PUT/DELETE 受影响，GET 没事？——CSRF 只对"可能改变状态"的方法做 Origin/Referer 校验，GET/HEAD/OPTIONS/TRACE 被视为安全方法（Django 的 `csrf_protect` 也跳过它们）。所以事故表现是"页面能打开、一提交就 403"，很容易被误判为前端/网关问题。排查时看 Django 日志的 `Origin checking failed` 和 `request.is_secure()` 的实际值。

**追问二**：`USE_X_FORWARDED_HOST` 与 `SECURE_PROXY_SSL_HEADER` 要不要一起开？——`SECURE_PROXY_SSL_HEADER` 只解决" scheme 是 https"，`USE_X_FORWARDED_HOST` 解决"Host 用 X-Forwarded-Host 而不是原始 Host"。如果 LB 改了 Host 或应用在多层代理后，两者可能都需要；但 `USE_X_FORWARDED_HOST` 会信任客户端可伪造的头，必须确保只有可信代理能设置（Q6101 的 Host 注入）。最小配置原则：只开当前架构真正需要的，并在边缘清洗对应头。

## 背诵要点
- Django 4 CSRF 用 `is_secure()` + Host 拼本站 origin；TLS 在 LB 终止未配代理头 → 拼成 http，https Origin 不匹配 → 403。
- `CSRF_TRUSTED_ORIGINS` 条目必须带 scheme（可 `https://*.example.com`），裸域名无效；不要加 http 削弱防护。
- 优先修 `SECURE_PROXY_SSL_HEADER` 让 `is_secure()` 正确；可信代理前提 + 边缘剥离伪造头；`USE_X_FORWARDED_HOST` 按需且防 Host 注入。

## 复盘追问
- 迁移后所有 POST 403、GET 正常，如何用 `is_secure()` 与 Origin 拼接解释并修复？（TLS 终止、代理头、带 scheme 的 trusted）
- 为什么 `CSRF_TRUSTED_ORIGINS` 写裸域名不生效？它和 `SECURE_PROXY_SSL_HEADER` 的职责边界是什么？（scheme 必填；修正本站 vs 额外白名单）
