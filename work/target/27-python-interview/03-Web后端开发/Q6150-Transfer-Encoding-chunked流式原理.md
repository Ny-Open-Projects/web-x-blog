---
title: "[Q6150] Transfer-Encoding chunked 流式原理与实现"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6150 · Transfer-Encoding: chunked 流式原理与实现

难度：P6 ｜ 标签：HTTP、chunked、流式响应、协议原理

**问**：导出大报表时接口内存爆了，改成分块流式响应后峰值降为常量。chunked 编码的线上协议格式是什么？为什么它让"不知道 Content-Length 也能流式发送"？Python 侧手写 chunked 编解码要注意什么（与请求走私 Q6122 的关系）？

**答**：
结论：HTTP/1.1 的响应必须在发送前知道 `Content-Length` 才能声明——但生成式响应（DB 流式导出、LLM 逐 token）无法预知总长。`Transfer-Encoding: chunked` 解决这个矛盾：把响应切成若干"块"，**每块前用十六进制声明自己的长度**，以 `0\r\n\r\n`（终止块）收尾，接收方按块累积即等价于一个无限长响应。它把"长度声明"从响应级下放到块级，服务端可以边生成边发，内存峰值 O(单块)。反向坑：请求侧如果框架/代理对 Content-Length 与 Transfer-Encoding 处理不一致，就是 HTTP 走私的温床（CL-TE，Q6122）——应用侧要么纯框架解析、绝不全手工读 body，要么显式拒绝双头请求。

取舍：chunked 流式 vs 先生成完整再发：流式省内存、首字节快（TTFB），代价是不能中途改状态码/头（headers 已发出），错误只能在流中截断（客户端收到不完整数据）；所以可取消/可重试语义要靠业务层（校验先行、失败前置）。

实战：实现要点——① WSGI 返回 generator 即隐式 chunked（gunicorn/uvicorn 代发）；② 每块大小权衡 8~64KB（太小包开销大、太大内存/延迟高）；③ 与反向代理协商确认 nginx `proxy_buffering off` 才真正流式（Q6071 SSE 同款问题）；④ 手写解码必须严格按"hex\r\n"切分并校验最终 0 块，长度不匹配即断连。

```python
def encode_chunked(data: bytes, chunk_size: int = 8) -> bytes:
    """手写 chunked 编码：hex 长度 + \r\n + 数据 + \r\n，终止块 0\r\n\r\n"""
    out = bytearray(b"")
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        out += f"{len(chunk):x}\r\n".encode() + chunk + b"\r\n"
    out += b"0\r\n\r\n"
    return bytes(out)

def decode_chunked(raw: bytes) -> bytes:
    """严格解码：逐块按长度切，校验终止块；不合法即抛错（防走私式畸形输入）"""
    out = bytearray()
    pos = 0
    while True:
        eol = raw.find(b"\r\n", pos)
        if eol < 0:
            raise ValueError("malformed chunk: missing size line")
        size = int(raw[pos:eol], 16)               # 非法 hex 会直接 ValueError
        pos = eol + 2
        if size == 0:                              # 终止块：后面应只剩 trailer+CRLF
            if raw[pos:pos + 2] not in (b"\r\n", b""):
                raise ValueError("garbage after terminal chunk")
            break
        out += raw[pos:pos + size]
        pos += size + 2                            # 跳过块后 CRLF
    return bytes(out)

payload = b"x" * 21
wire = encode_chunked(payload)
print("wire bytes:", wire)
print("decoded   :", decode_chunked(wire) == payload)

# 流式服务端行为演示：headers 先行，块逐个产出，峰值 = 单块
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time

class StreamHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self):
        self.send_response(200)
        self.send_header("Transfer-Encoding", "chunked")
        self.send_header("Content-Type", "text/plain")
        self.end_headers()                          # 头已发出，状态码不可再改
        for i in range(3):
            blk = f"row-{i}\n".encode()
            self.wfile.write(f"{len(blk):x}\r\n".encode() + blk + b"\r\n")
            self.wfile.flush()
            time.sleep(0.01)
        self.wfile.write(b"0\r\n\r\n")

    def log_message(self, *a):                      # 静默测试日志
        pass

srv = HTTPServer(("127.0.0.1", 0), StreamHandler)
threading.Thread(target=srv.serve_forever, daemon=True).start()

import urllib.request
port = srv.server_address[1]
with urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=3) as resp:
    print("response TE:", resp.headers.get("Transfer-Encoding"))
    print("streamed body:", resp.read())

srv.shutdown()
```

**追问一**：为什么 chunked 响应里 `Content-Length` 必须缺席、两者同现意味着什么？——HTTP/1.1 语义中两者互斥且 Content-Length 优先（RFC 9112），同时出现且不一致是走私攻击特征，正规代理应拒绝或剥离；HTTP/2 取消 chunked（DATA 帧天然分块），迁移 H2 后该头会被丢弃。

**追问二**：流式响应中途出错，客户端会感知到什么？——连接断开或收到不完整 chunk 序列（缺 0 块），HTTP 层没有"部分失败"语义；缓解：头里加 `X-Content-Estimate`/自定义 trailer、业务层先校验全量可生成性再开流，讨论"预检 + 流"两段式设计。

**追问三**：trailer 头（chunked 尾部附加头）有什么用、Python 支持吗？——终止块后可再发头（如完整性校验值），`http.client` 会把它放进 `resp.trailers()`；实践中用得少，因为中间代理常剥离，重要校验别放 trailer。

## 背诵要点
- chunked = 每块自带十六进制长度 + `0\r\n\r\n` 终止，把长度声明下放到块级，流式生成 O(单块) 内存。
- 代价：头发出后状态码不可改、错误只能截断流；块大小 8~64KB，反代需关 buffering 才真流式。
- Content-Length 与 TE 同现是走私特征；HTTP/2 取消 chunked（DATA 帧替代）。

## 复盘追问
- 导出接口改流式后，前端"下载进度条"怎么实现？（响应头声明预计行数 + 前端按块计数，讨论估算不准的用户体验与 trailer 方案）
- 为什么有些代理会偷偷把 chunked 转 buffered 再转发，如何检测？（对比 TTFB 与总时长、抓包看 TE 头是否被剥离，讨论 proxy_buffering/缓存层排查清单）
