---
title: "[Q6160] HTTP 方法幂等与缓存语义矩阵"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6160 · HTTP 方法幂等与缓存语义矩阵

难度：P7 ｜ 标签：HTTP 方法、幂等性、可缓存性、RFC 9110、条件请求

**问**：RFC 9110 里"安全、幂等、可缓存"三个属性分别约束什么、哪些组合是允许的（如 PUT 可缓存吗、DELETE 为什么不可缓存）？GET 与 HEAD 的关系在缓存层怎么工作？为什么"POST 幂等接口"要用 Idempotency-Key 而不是改语义，缓存对非 GET 的响应在什么条件下可复用？

**答**：
结论：三个属性是**正交的协议承诺**：安全（不改服务器状态，只读）、幂等（N 次执行与 1 次效果相同，允许改状态）、可缓存（响应可被复用于后续请求）。矩阵：GET/HEAD 安全+幂等+默认可缓存；PUT/DELETE 幂等**但默认不可缓存**（PUT 的成功响应可缓存必须显式带新鲜度头且极少这样做；DELETE 200 响应不可复用——删除效果的"缓存"没有意义）；POST 既不幂等也默认不可缓存（除非显式缓存头 + 客户端配合，实际禁用）。GET 与 HEAD 在缓存层是**同一资源的两种视图**：缓存可用 HEAD 刷新对 GET 的缓存条目（Content-Length 变化即失效），反之 GET 缓存也可回答 HEAD（去掉 body）。条件请求（If-None-Match/ETag）只对幂等方法有意义——它要求"重放同一请求效果不变"，POST 上用条件头无定义。

取舍："POST 幂等"的正确工程化是**幂等键协议**而非改方法：客户端生成 Idempotency-Key，服务端按 (key) 记录首次响应，重放返回缓存响应（RFC 9110 也确认重放 POST 时服务端可通过幂等键保证安全）——把"效果幂等"从传输层语义移到应用层契约，这也是 Q6060 幂等实现的协议基础。为什么不用 PUT 替代 POST：PUT 语义是"替换目标资源状态"，创建订单的资源 URI 通常是服务端分配的，强行用 PUT 会扭曲资源模型。

实战：网关/客户端重试策略必须与矩阵对齐——幂等方法自动重试，POST 只在带幂等键时重试；缓存配置里 HEAD 必须与 GET 共享缓存键（多数代理默认如此），否则 HEAD 预热会把 GET 缓存打歪。

```python
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client

class ApiHandler(BaseHTTPRequestHandler):
    store = {"etag": "v1", "data": "resource-body"}
    def do_GET(self):
        data, etag = self.store["data"], self.store["etag"]
        if self.headers.get("If-None-Match") == etag:
            self.send_response(304)                    # 条件命中：无 body
            self.send_header("ETag", etag); self.end_headers()
            return
        self.send_response(200)
        self.send_header("ETag", etag)
        self.send_header("Cache-Control", "max-age=60")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers(); self.wfile.write(data.encode())
    def do_HEAD(self):
        data = self.store["data"]
        self.send_response(200)                        # 与 GET 同键：同 ETag 同缓存
        self.send_header("ETag", self.store["etag"])
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()                             # 无 body
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0)); self.rfile.read(n)
        key = self.headers.get("Idempotency-Key")
        sent = getattr(self, "_posted", set())
        if key in sent:                                # 幂等重放：返回首次响应
            self.send_response(200); self.send_header("Idempotency-Replayed", "true")
            self.send_header("Content-Length", "0"); self.end_headers(); return
        sent.add(key)
        self.send_response(201); self.send_header("Content-Length", "0"); self.end_headers()
    def log_message(self, *a): pass

srv = HTTPServer(("127.0.0.1", 0), ApiHandler)
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()

# GET + 条件请求：ETag 协商
c = http.client.HTTPConnection("127.0.0.1", port)
c.request("GET", "/"); r = c.getresponse(); etag = r.getheader("ETag"); r.read()
c.request("GET", "/", headers={"If-None-Match": etag})
r = c.getresponse()
print("conditional GET ->", r.status, "body:", r.read())   # 304 无 body
c.request("HEAD", "/"); r = c.getresponse()
print("HEAD ->", r.status, "len:", r.getheader("Content-Length"), "same etag:", r.getheader("ETag") == etag)

# POST + Idempotency-Key 重放
def post(key):
    c2 = http.client.HTTPConnection("127.0.0.1", port)
    c2.request("POST", "/", body=b"payload", headers={"Idempotency-Key": key})
    r = c2.getresponse(); out = (r.status, r.getheader("Idempotency-Replayed")); r.read(); c2.close()
    return out

print("POST first:", post("k1"), " replay:", post("k1"))

# 语义矩阵（面试背诵）
for m, attrs in {"GET": "安全+幂等+可缓存", "HEAD": "安全+幂等+可缓存(与GET同键)",
                 "PUT": "幂等, 默认不可缓存", "DELETE": "幂等, 默认不可缓存",
                 "POST": "非幂等, 默认不可缓存(幂等键协议补位)"}.items():
    print(f"{m:8}: {attrs}")
c.close(); srv.shutdown()
```

**追问一**：为什么"可缓存"是方法属性 + 响应头属性的合取？——方法决定**默认可缓存性**（GET/HEAD 才有默认），响应头（Cache-Control/Expires）决定**新鲜度与覆写**；显式缓存头不能让 POST 变得可缓存到"任意代理都会存"——RFC 9110 允许 POST 响应被缓存并用于后续 GET 仅在明确指示时，工程上视为不可用，避免依赖角落语义。

**追问二**：304 响应里允许带哪些头、为什么 ETag 弱校验器不能用于范围请求？——304 可带缓存相关头（Cache-Control/ETag/Vary/Link 等）用于更新缓存元数据；弱 ETag（W/ 前缀）只保证"语义等价"不保证字节一致，Range 分片需要字节级稳定，故 If-Range 只认强 ETag——这是文件断点续传（Q6109）必须用强校验器的原因。

## 背诵要点
- 三属性正交：安全（只读）、幂等（N 次=1 次）、可缓存（默认仅 GET/HEAD）；PUT/DELETE 幂等但默认不可缓存。
- 条件请求只对幂等方法有定义；HEAD 与 GET 共享缓存键，304 用于刷新缓存元数据。
- POST 幂等靠 Idempotency-Key 协议（首响应缓存+重放返回），不改方法语义；重试策略按矩阵对齐。

## 复盘追问
- 支付回调接口被网关按"POST 不可重试"配置导致丢单，如何设计幂等键协议并校正网关重试策略？（键生成/存储/重放响应、讨论键的 TTL 与并发去重）
- 为什么给 PUT 响应配 Cache-Control 让缓存"记住删除后的空状态"是危险设计？从语义与失效链角度分析。（PUT/DELETE 缓存语义脆弱、失效广播成本，讨论以版本化资源替代）
