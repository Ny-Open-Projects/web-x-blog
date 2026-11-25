---
title: [PER-983] HTTP/3 的 0-RTT 为什么快？重放风险如何处理
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-983：HTTP/3 的 0-RTT 为什么快？重放风险如何处理

**答**：
- TLS 1.3 + QUIC 的 0-RTT：复用会话票据，首个数据包就携带请求，省去 1~2 个 RTT 的握手，弱网/高延迟场景首字节收益显著。
- 风险：0-RTT 数据没有完整握手保护，可被重放（replay attack）——攻击者录制并重放早期请求。
- 约束：0-RTT 只能携带幂等请求（GET/HEAD）；非幂等（POST 支付/下单）服务端必须拒绝在 0-RTT 阶段执行。
- 落地：CDN/网关配置 0-RTT 白名单；对业务侧保证关键 GET 接口幂等（带 requestId 去重）。

```javascript
// 0-RTT 幂等守卫：服务端视角
const seen = new Set();
function handleEarlyData(req) {
  if (req.isEarlyData) {                       // 0-RTT 阶段
    if (!['GET', 'HEAD'].includes(req.method)) return 425;   // Too Early
    const key = req.method + req.url + (req.headers['if-none-match'] ?? '');
    if (seen.has(key)) return 304;             // 重放去重
    seen.add(key);
  }
  return proxy(req);                           // 正常转发
}
// 浏览器无感知；客户端保证 GET 幂等即可享受 0-RTT
```
