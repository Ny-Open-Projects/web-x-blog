---
title: "[Q6158] HTTP/2 Server Push 废弃与 103 Early Hints 演进"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6158 · HTTP/2 Server Push 废弃与 103 Early Hints 演进

难度：P7 ｜ 标签：HTTP/2、Server Push、Early Hints、103、性能演进

**问**：HTTP/2 Server Push 为什么被 Chrome/边缘生态逐步废弃、它与 103 Early Hints 的机制差在哪？Early Hints 的"预提示不预推"如何解决 Push 的带宽浪费与缓存归属问题？Python 后端（ASGI/uvicorn/nginx 链路）怎么支持 103，收益与注意事项是什么？

**答**：
结论：Server Push（RFC 7540）让服务器在客户端没请求前就把资源推到 HTTP/2 连接流里，失败点有三个：① **推不推得准**——服务器不知道浏览器缓存里有什么，重复推浪费带宽（Chrome 实测 20%+ 推送被重复接收）；② **缓存归属**——推送资源进的是连接级缓存，与应用 HTTP 缓存语义割裂；③ **代理/CDN 多数不转发**。Chrome 2022 起移除支持，nginx 2023 年删除 `http2_push`——Push 被官方放弃。**103 Early Hints**（RFC 8297）是反向思路：不推资源本体，只在最终响应生成前**提前发一个 103 临时响应**携带 `Link: </style.css>; rel=preload` 头，浏览器收到后立刻发起常规请求（走正常缓存/优先级/协商），服务器稍后再发真正的 200。它修掉了 Push 的两大死穴——浏览器自己的缓存与并发预算仍然生效、没有带宽浪费；且对服务器是"无状态提示"，CDN 透传即可。

取舍：103 的收益场景 = 首字节慢（服务端渲染、重定向链后）+ 关键资源固定（CSS/字体/首图）；对动态生成快或资源列表依赖响应内容（个性化）的页面收益小甚至负收益（提前提示错资源）。链路要求：反代必须透传 1xx 信息响应（nginx `proxy_pass` 默认支持，h2c 直连需服务器实现 103 发送——uvicorn/h11 已有信息响应支持但生态参差，需实测），且**浏览器端只是"可能利用"**——103 是建议不是承诺，指标要按"关键资源开始加载时间"对比而非强依赖。

实战：Python 侧落地：ASGI 层面服务器若支持 `http.response.early_hint` 类扩展或直接写原始 1xx（多数要服务器级配置），应用侧用 `Link` 头预生成 preload 列表（模板渲染前已知的那部分），配合 `<link rel=preload>` 双保险；监控看 TTFB 与关键资源 start time 的 P75 分位。

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket, threading, time

# 1) 原始 socket 演示 103 Early Hints 的线格式（RFC 8297）
def send_103(sock, hints):
    lines = ["HTTP/1.1 103 Early Hints"]
    for url, rel in hints:
        lines.append(f'Link: <{url}>; rel={rel}')
    sock.sendall(("\r\n".join(lines) + "\r\n\r\n").encode())

def serve_early_hints(port):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port)); srv.listen(1)
    conn, _ = srv.accept()
    time.sleep(0.2)                       # 模拟服务端渲染慢：先发提示
    send_103(conn, [("/style.css", "preload"), ("/font.woff2", "preload")])
    body = b"<html><body>late render</body></html>"
    conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n"
                 + f"Content-Length: {len(body)}\r\n\r\n".encode() + body)
    conn.close(); srv.close()

import urllib.request
with socket.socket() as s:
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
threading.Thread(target=serve_early_hints, args=(port,), daemon=True).start()

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def http_error_103(self, req, fp, code, msg, headers):   # 标准库默认忽略 1xx
        print("client saw 103 with hints:", headers.get_all("Link") or headers.get("Link"))
        return None

try:
    resp = urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=3)
    print("final:", resp.status, resp.read()[:30])
except Exception as e:
    print("103 响应在 urllib 中表现为信息响应/跳过（标准库不消费 103），浏览器才会利用:", e)

# 2) 应用侧 preload 列表生成（与 Link 头同源）
def preload_links(template_assets):
    return [f"</{a}>; rel=preload; as={t}" for a, t in template_assets]

assets = [("style.css", "style"), ("font.woff2", "font")]
print("Link headers:", preload_links(assets))
```

**追问一**：103 与 `<link rel=preload>` 在 HTML 里的关系？——103 的 Link 头与 HTML 内 preload 提示语义相同（RFC 8297 明确 103 头可以重复/覆盖最终 200 头里的 Link）；实践是"HTML 里放最终版、103 里放已知子集"，浏览器以两者并集工作，重复 preload 有去重。

**追问二**：为什么 CDN 对 103 的支持是落地关键？——CDN 在中间时，上游的 103 若被吞掉（很多老代理直接丢弃 1xx），客户端永远看不到提示，收益归零且无从告警；所以选型要看 CDN 明确声明透传 1xx（Cloudflare/Fastly 已支持），并在压测里验证 103 到达率（抓客户端侧）。

## 背诵要点
- Server Push 三死穴：不知道客户端缓存、连接级缓存语义割裂、代理不转发——Chrome/nginx 已移除，属废弃特性。
- 103 Early Hints 只发 Link 提示不推本体：浏览器缓存/优先级仍生效、无带宽浪费；RFC 8297。
- 落地前提：反代/CDN 透传 1xx，应用预生成已知 preload 列表；指标看关键资源 start time 而非 TTFB 单点。

## 复盘追问
- 首页 TTFB 800ms 优化评审里有人提"上 HTTP/2 Push"，如何给出废弃依据与 103 方案的收益预估？（Push 已弃用；103 在慢 FTTB+固定关键资源下收益，讨论量化口径）
- 为什么 103 是"建议而非承诺"？从信息响应语义与浏览器调度角度分析。（1xx 不改变最终响应状态、浏览器可忽略；讨论与 preload 双保险）
