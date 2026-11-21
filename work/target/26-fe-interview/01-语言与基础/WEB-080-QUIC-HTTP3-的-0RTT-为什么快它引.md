---
title: [WEB-080] QUIC/HTTP3 的 0-RTT 为什么快？它引入了什么安全代价？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-080：QUIC/HTTP3 的 0-RTT 为什么快？它引入了什么安全代价？
**答**：
- 0-RTT：复用此前会话的 PSK，客户端在第一个飞行包里就携带加密的应用数据（early data），省掉整个握手往返。
- 代价一：early data 用旧密钥加密，不具备前向保密；代价二：没有握手去重，同一份 early data 可被恶意重放多次（重放攻击）。
- 协议层约束：early data 必须是幂等的——GET 可以，POST 付款绝不允许放进 0-RTT；服务端要实现反重放（单次 ticket、时间窗、按 ticket 去重）。
- nginx 通过 `$ssl_early_data` 暴露 early data 状态，标准做法是在应用层拒绝携带非幂等语义的 early data。

```nginx
# nginx 配合 0-RTT：透传状态给上游，让应用决定是否处理 early data
server {
    listen 443 quic reuseport;
    ssl_early_data on;
    proxy_set_header Early-Data $ssl_early_data;  # 值为 1 表示该请求来自 0-RTT
}
```

```javascript
// 应用层反重放：上游收到 Early-Data: 1 时拒绝非幂等请求
const http = require('http');
http.createServer((req, res) => {
  if (req.headers['early-data'] === '1' && req.method !== 'GET' && req.method !== 'HEAD') {
    res.writeHead(425, { 'Retry-After': '1' }); // 425 Too Early 是为此设计的状态码
    return res.end('0-RTT 不允许携带非幂等请求');
  }
  res.writeHead(200); res.end('ok');
}).listen(3000);
```
