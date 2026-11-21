---
title: [WEB-006] HTTP/2 的头部压缩 HPACK 是什么原理？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-006：HTTP/2 的头部压缩 HPACK 是什么原理？
**答**：
- HTTP/1.1 头部是纯文本，每次请求都重复携带 Cookie、User-Agent 等大块相同内容，浪费带宽。
- HPACK 用两张表：静态表（预定义 61 个常见头）+ 动态表（连接级内存，缓存本次连接出现过的头）。
- 重复的头部只需传一个索引号；不重复的头用哈夫曼编码压缩后再传。
- 动态表要求请求按序到达才能正确解码，这也是 HTTP/2 禁止请求乱序重组失败的原因之一。

```bash
# 用 curl --http2 观察 HTTP/2 连接，头部体积由 HPACK 在传输层压缩，
# 抓包工具如 wireshark 可以看到帧不再有重复的明文 Cookie
curl --http2 -v https://nghttp2.org/ -o /dev/null 2>&1 | head -30

# 服务端（Node.js）验证：http2 模块原生支持 HPACK，头部重复内容只传索引
```

```javascript
// Node.js http2 服务：同一连接反复请求时，重复响应头命中动态表，只传输索引
const http2 = require('http2');
const server = http2.createServer();
server.on('stream', (stream, headers) => {
  stream.respond({
    ':status': 200,
    'content-type': 'application/json',
    'x-custom-trace': 'fixed-value', // 第二次起动态表命中，几乎不占带宽
  });
  stream.end(JSON.stringify({ ok: true }));
});
server.listen(8443);
```
