---
title: "[Q6221] X-Accel-Redirect 受保护下载：应用鉴权与静态层分工"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6221 · X-Accel-Redirect 受保护下载：应用鉴权与静态层分工

难度：P6 ｜ 标签：X-Accel-Redirect、Nginx、internal、sendfile、签名 URL、文件下载、鉴权

**问**：会员才能下载的 PDF 放在磁盘/对象存储上，为什么不能让应用直接 read 再回给客户端？Nginx 的 X-Accel-Redirect 机制怎么工作——应用返回什么、Nginx 做什么？`internal` 指令挡的是什么攻击？下载链接的鉴权签名该怎么设计？

**答**：
结论：应用直读文件有两条硬伤——**占 worker**（大文件下载把同步 worker 挂住几秒到几分钟）和**占带宽/内存**（文件经应用内存中转，失去静态层的 sendfile 零拷贝）。X-Accel-Redirect 的分工是：①**应用只做鉴权**：校验用户权限/签名，通过后返回一个**空响应体** + `X-Accel-Redirect: /uploads/2026/report.pdf` 头，毫秒级返回；②**Nginx 接力伺服**：看到该头后，在内部 location 上按 alias 取真实文件、sendfile 直发客户端，不占应用资源；③**internal 是关键防线**：`location /uploads/ { internal; }` 保证外网直接 `GET /uploads/...` 得 404——真实路径永远不可绕过鉴权直达；④**应用层不暴露磁盘路径**：X-Accel-Redirect 里的路径是**内部 URI**（Nginx 的 location 前缀），不是 `/data/files/2026/...` 这种磁盘绝对路径，客户端看不到也猜不到真实存储布局；⑤签名设计：过期时间戳 + HMAC(path) 的拼接 token，比对用 `hmac.compare_digest` 防时序侧信道。

取舍：a) 单机无 Nginx：Python 侧 `FileResponse`/`sendfile` 系统调用也能零拷贝，但仍占 worker——鉴权开销小、文件大的场景才可接受；b) 对象存储（S3/OSS）：同样思路换成**预签名 URL**（presigned GET），应用只签发短时效 URL，下载流量走存储域名——云端的标准等价物；c) 签名 URL vs 每次实时鉴权：签名 URL 可缓存可断点续传（Range 请求 Nginx 原生支持），实时鉴权适合权限随时变化的场景，代价是每次下载都打应用；d) 防**路径穿越**：应用拼内部 URI 前必须归一化校验（`posixpath.normpath` 后确认仍在白名单前缀下），X-Accel 头本身也是用户不可控的（应用生成），但如果签名校验逻辑里把用户输入直接拼路径就是漏洞；e) 别忘了 Content-Disposition：文件名由应用带头指定（attachment; filename=），静态层不会替你起名。

实战：事故形态是"知识付费站的课件下载：早期实现是 Flask 视图里 `send_file('/data/files/xxx.pdf')`，大促时 200 个并发下载把 gunicorn worker 全占满，登录接口也排队超时；改造为 JWT 校验 + X-Accel-Redirect，worker 只花 1ms 鉴权，下载流量全部由 Nginx 承担"。下面演示签名设计与鉴权拦截。

```python
# X-Accel-Redirect: 应用层鉴权 + 静态层伺服
import hashlib
import hmac
import os
import time


def authorize(path: str, token: str, secret: bytes) -> str | None:
    """返回内部路径或拒绝原因; 决不把真实磁盘路径暴露给客户端"""
    if not token:
        return "deny: 未登录"
    expected = hmac.new(secret, path.encode(), hashlib.sha256).hexdigest()[:32]
    exp = int(token[:8], 16)
    if time.time() > exp:
        return "deny: 链接过期"
    if not hmac.compare_digest(expected, token[8:40]):
        return "deny: 签名不符"
    return None


secret = b"dev-secret"
path = "/uploads/2026/report.pdf"
exp = int(time.time()) + 600
token = f"{exp:08x}" + hmac.new(secret, path.encode(), hashlib.sha256).hexdigest()[:32]

print("[1] 应用只做鉴权, 不读文件不耗带宽:")
reason = authorize(path, token, secret)
print("    合法请求 ->", "通过" if reason is None else reason)
if reason is None:
    print("    响应体为空, 只有头:")
    print("        X-Accel-Redirect:", path)
    print("        Content-Disposition: attachment; filename=report.pdf")

print("[2] Nginx 收到 X-Accel-Redirect 后, 在内部 location 静态层取文件发回客户端")
print("    nginx 配置: location /uploads/ { internal; alias /data/files/; }")
print("    internal 保证外网直接 GET /uploads/... 拿到 404 -- 路径不可绕过")

print("[3] 防线清单: 签名带过期时间 | compare_digest 防时序 | internal 挡直连 | 路径归一防穿越")
print("[4] 对比 sendfile: sendfile 是应用自己读盘(占 worker), X-Accel 是静态层零拷贝(不占应用)")
bad = authorize(path, f"{exp:08x}{'0' * 32}", secret)
print("    篡改签名 ->", bad)
```

**追问一**：签名的 HMAC 消息为什么用内部路径而不是文件 ID？过期时间戳放在 token 明文里安全吗？—— 用内部路径做 HMAC 消息能把"签名"与"具体资源"绑定：签名只对这一个资源有效，拿去请求别的资源必然校验失败（防横向挪用）；如果只签名用户 ID，签名就能用于该用户的任意资源。过期时间戳明文没问题——它的作用是让校验端能**判断是否过期**，防篡改靠的是后面的 HMAC（HMAC 消息只含路径不含 exp 的话，篡改 exp 就能续期——所以更严格的实现把 exp 也纳入 HMAC 消息：`HMAC(path + exp)`，本例 token 前缀 exp 明文 + 签名，生产版本应把 exp 一起签名）。这体现签名设计的一般原则：**所有需要防篡改的字段都必须进入 HMAC 消息**。

**追问二**：X-Accel-Redirect 响应里应用设置的其他头（Content-Disposition、缓存控制）会传给客户端吗？Range 断点续传呢？—— 应用响应的头会被 **Nginx 合并进最终下载响应**（除非用 `proxy_ignore_headers`/`X-Accel-Expires` 类指令调整），所以 Content-Disposition、Cache-Control、自定义头都能送达客户端；但 Content-Length 会由静态层按真实文件重算，应用不必也无法准确设置。Range 请求由 Nginx 静态层原生处理（应用根本看不到 Range 头，因为请求到达应用时只是鉴权），断点续传、ETag、If-Modified-Since 全部在内部 location 上生效——这正是"鉴权与传输解耦"的红利：应用的鉴权逻辑完全不用理解 HTTP 缓存语义。注意 Authorization 类敏感头别透传到静态层日志，内部 location 记访问日志时要做脱敏。

## 背诵要点
- 应用直读文件 = 占 worker + 失去 sendfile 零拷贝；X-Accel-Redirect：应用毫秒级鉴权，Nginx 内部 location 伺服。
- internal 指令让外网直连真实路径得 404；应用返回的是内部 URI，不暴露磁盘路径。
- 签名 URL：过期时间 + HMAC(所有防篡改字段)，compare_digest 恒定时间比对；对象存储用 presigned URL 等价替换。

## 复盘追问
- 为什么签名里把过期时间也纳入 HMAC？（明文 exp 可被篡改续期；HMAC 消息必须覆盖所有防篡改字段）
- 应用侧要自己处理 Range 断点续传吗？（不用——静态层原生处理；应用只管鉴权与 Content-Disposition）
