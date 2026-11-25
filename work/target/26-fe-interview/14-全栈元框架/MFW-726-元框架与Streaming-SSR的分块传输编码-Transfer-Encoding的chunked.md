---
title: [MFW-726] Transfer-Encoding chunked
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-726：Transfer-Encoding chunked

**答**:
- chunked 编码与流式 SSR：1) **chunked 语义**（Transfer-Encoding: chunked——服务器不确定内容长度时分块发送；每块前有长度前缀（hex 长度 + \r\n + 数据 + \r\n）；零长度块 = 结束）；2) **流式 SSR 的依赖**：React 的 pipe(res) → res.write(chunk) → Node 自动 chunked（无 Content-Length 时 Node 自动 chunked）；3) chunked 的 CDN 行为（某些 CDN 缓冲整个 chunked 响应——破坏流式（RBL-588 代理缓冲的 CDN 版——CDN 的缓冲策略影响流式）。
- chunked 与 Content-Length 的互斥：设置了 Content-Length = 非 chunked（一次发送）；流式 = 无 Content-Length + chunked；「Content-Length 的缺失」对缓存的含义（无长度 = 不可缓存——CDN 需要 length 判断完整性）。
- 追问钩子：为什么「chunked 流式 SSR」在某些 CDN 上会退化为非流式？——CDN 的缓冲策略：某些 CDN 等完整响应（或缓冲到固定大小）才转发——chunked 的实时性被 CDN 缓冲破坏（「SSE 变成一次性返回」同 RBL-588 的 nginx 问题）；流式的部署检查单：CDN 的缓冲策略 + HTTP/2 的流式支持 + 代理超时——流式的全链路验证（不只看 server 还看中间层）。

```javascript
// Node 的 chunked 自动化
import http from 'http';
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'content-type': 'text/html' });   // 无 content-length → Node 自动 chunked
  res.write('<html><head>...</head><body>');              // 块 1
  // 流式渲染
  const { pipe } = renderToPipeableStream(<App />, {
    onShellReady() { pipe(res); },                       // React 写入块
    onAllReady() { res.end(); },                         // 零长度块 = 结束
  });
});
// chunked 协议格式
// HTTP/1.1 200 OK
// Transfer-Encoding: chunked
// 5\r\n
// hello\r\n
// 0\r\n\r\n                                            ← 零长度 = 结束
// CDN 检查单
// 1) nginx: proxy_buffering off;
// 2) Cloudflare: 不缓冲 HTML（默认直通）
// 3) HTTP/2: 分帧传输（天然支持流式）
// 4) 检测方法：curl -N（--no-buffer）看首包时间
```
