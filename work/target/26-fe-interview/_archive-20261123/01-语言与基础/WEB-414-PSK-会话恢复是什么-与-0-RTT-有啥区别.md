---
title: [WEB-414] PSK 会话恢复是什么，与 0-RTT 有啥区别
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTPS]
type: 面试题
---

## WEB-414：PSK 会话恢复是什么，与 0-RTT 有啥区别

**答**：
- PSK（预共享密钥）：上次连接结束时双方约定一个密钥，下次握手直接用它恢复，省掉非对称运算
- 1-RTT PSK 恢复：客户端发 Hello 时带上 PSK 身份，服务端确认即可，安全（有新鲜随机数参与）
- 0-RTT：客户端在第一个飞行里就带着 PSK 加密的应用数据，把首包也省了，但这段数据没有前向安全、可被重放
- 工程结论：0-RTT 只放幂等请求（GET、预热的静态资源），写操作绝不放 0-RTT；服务端要用 nonce 去重兜底

```javascript
// 服务端识别并拒绝 0-RTT 中的非幂等请求（伪代码）
app.use((req, res, next) => {
  if (req.socket.isEarlyData && req.method !== 'GET') {
    // RFC8446 建议：对 0-RTT 中的非幂等请求返回 425 Too Early
    return res.status(425).end();
  }
  next();
});
```
