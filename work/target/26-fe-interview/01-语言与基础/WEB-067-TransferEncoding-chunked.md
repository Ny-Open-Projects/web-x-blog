---
title: [WEB-067] Transfer-Encoding: chunked 的编码格式是什么？和 Content-Length 什么关系？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-067：Transfer-Encoding: chunked 的编码格式是什么？和 Content-Length 什么关系？
**答**：
- 适合"边生成边发送"的场景：服务器无法预先算出总长度（如流式 LLM 输出、日志推送），就分块发送，每个块前有一个十六进制长度行。
- 格式：`块长度\r\n块数据\r\n` 循环，最后以 `0\r\n` 结束，可再跟 trailer 头，最终 `\r\n` 收尾。
- 两者互斥：有 Content-Length 就不能用 chunked；HTTP/2 中 chunked 被废弃，分帧由二进制帧层完成。
- 前端可感知的体现：fetch 的 `res.body` 是 ReadableStream，chunked 响应可以逐块读取实现流式渲染。

```javascript
// Node 服务端：不设置 Content-Length 并持续 write，Node 自动使用 chunked
const http = require('http');
http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  let i = 0;
  const timer = setInterval(() => {
    res.write(`chunk ${i}\n`); // 每次写入就是一个 chunk
    if (++i >= 5) { clearInterval(timer); res.end(); }
  }, 200);
}).listen(3000);

// 报文形态：每块前是十六进制长度，0 块结束
// 8\r\nchunk 0\n\r\n 8\r\nchunk 1\n\r\n ... 0\r\n\r\n

// 前端逐块消费流式响应
fetch('http://localhost:3000').then(async (res) => {
  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    console.log(decoder.decode(value)); // 每收到一个 chunk 立即处理
  }
});
```

## 十三、HTTPS 深入
