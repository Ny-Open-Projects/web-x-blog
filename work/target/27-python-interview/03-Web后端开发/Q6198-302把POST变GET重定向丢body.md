---
title: "[Q6198] 302 把 POST 变成 GET：重定向后请求体丢失"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6198 · 302 把 POST 变成 GET：重定向后请求体丢失

难度：P6 ｜ 标签：HTTP、302、307、308、重定向、方法保持

**问**：登录后 `redirect("/dashboard")` 用 302，POST 表单提交到 `/orders` 后被重定向，请求体没了、方法变成 GET，订单没创建。302 不是"临时重定向"吗，为什么会改方法？307/308 又是什么？什么时候必须用 307？

**答**：
结论：302（Found）在历史上被浏览器实现成"把 POST 改成 GET 再跳"，虽然 RFC 7231 说"不应该改变方法"，但为了兼容，主流客户端都这么做，最终 RFC 9110 把这一行为写进了现实语义。303（See Other）明确要求"用 GET 访问新位置"，适合 POST-Redirect-GET；307（Temporary Redirect）和 308（Permanent Redirect）明确要求**保持原方法和请求体**重放。所以"提交后跳转"要用 303（想变 GET）或 307（想保方法），不能用 302 揣测。

取舍：a) 表单提交成功后跳结果页：303 + Location，语义最清晰，避免用户刷新重复提交；b) API 层"资源临时迁移/维护"且必须保留方法与 body：307；c) 永久迁移且保方法：308（会被缓存，慎用）；d) 301 同样是"永久"，但历史上也会把 POST 变 GET，且浏览器会**永久缓存**，配置错了无法回滚——生产上做重定向优先 302/307，301 只用于确定不变的静态资源。注意 307 重放 body 要求 body 可重放（流式上传不可重放，客户端会失败）。

实战：事故形态是"支付回调地址配了 302，POST 到网关后被改成 GET 跳到结果页，签名校验拿不到 body 直接失败；同时 301 被浏览器缓存，修好配置后老用户仍然跳到旧地址"。下面用本地 HTTP 服务演示 302 与 307 在客户端的行为差异。

```python
import http.client
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def _redirect(self, code):
        self.send_response(code)
        self.send_header("Location", "/new")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        if self.path == "/old":
            self._redirect(302)
        elif self.path == "/new":
            payload = b"GET:"
            self.send_response(200)
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        else:
            self.send_response(404)
            self.send_header("Content-Length", "0")
            self.end_headers()

    def do_POST(self):
        if self.path == "/old":
            self._redirect(302)
        elif self.path == "/keep":
            self._redirect(307)
        elif self.path == "/new":
            n = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(n)
            payload = self.command.encode() + b":" + body
            self.send_response(200)
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *args):
        pass


server = HTTPServer(("127.0.0.1", 0), Handler)
port = server.server_address[1]
threading.Thread(target=server.serve_forever, daemon=True).start()


def submit(path, body=b"amount=100"):
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2)
    conn.request("POST", path, body=body)
    resp = conn.getresponse()
    location = resp.getheader("Location")
    data = resp.read()
    conn.close()
    return resp.status, location, data


def follow_like_browser(path, body=b"amount=100"):
    status, location, _ = submit(path, body)
    if status == 302:                      # 浏览器：改成 GET，丢弃 body
        conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2)
        conn.request("GET", location)
    elif status == 307:                    # 规范：保持 POST 与 body
        conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2)
        conn.request("POST", location, body=body)
    resp = conn.getresponse()
    data = resp.read()
    conn.close()
    return status, data


print("[1] 302 后按浏览器语义跟随:", follow_like_browser("/old"))
print("[2] 307 后保持方法跟随:", follow_like_browser("/keep"))

# 直接验证 307 透传了 body
status, location, _ = submit("/keep")
print("[3] 307 响应:", status, location)

server.shutdown()
```

**追问一**：307 与 308 的区别只有"临时/永久"吗？—— 语义上是，但"永久"意味着**可缓存**：308 会被浏览器/CDN 缓存，改错地址后客户端可能长期不再问你；307 不会被永久缓存。另外 301/308 的"永久"对搜索引擎也生效，做域名迁移时是优点，做灰度时是灾难。生产上"不确定要不要长期保留"的重定向一律临时（302/307）。

**追问二**：为什么流式上传遇到 307 会失败？—— 307 要求把原请求**重新发送**到新地址，而流式 body（`Transfer-Encoding: chunked` 或一次性文件流）在第一次发送时已被消费，客户端无法重放；即使客户端有重试逻辑，也可能因为 `Content-Length` 未知而拒绝。所以"大文件上传 + 重定向"要在网关层解决（直接打到最终地址、或先 307 到对象存储的预签名 URL 并用 PUT 幂等重放）。

## 背诵要点
- 302 在浏览器里普遍把 POST 变 GET；303 明确用 GET；307/308 明确保持方法与 body。
- 301/308 会被永久缓存，改错难回滚；生产重定向优先 302/307。
- 307 重放 body 要求 body 可重放，流式上传需在网关/预签名 URL 层解决。

## 复盘追问
- 支付回调 POST 后 body 丢失，如何从 302 的历史语义解释？（浏览器改写为 GET）
- 什么时候该用 303、307、308？（PRG、保方法临时、保方法永久）
