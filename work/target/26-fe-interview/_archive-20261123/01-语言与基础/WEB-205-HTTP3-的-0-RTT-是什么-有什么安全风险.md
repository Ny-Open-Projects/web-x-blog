---
title: [WEB-205] HTTP/3 的 0-RTT 是什么？有什么安全风险？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-205：HTTP/3 的 0-RTT 是什么？有什么安全风险？

**答**：
- 0-RTT：客户端复用之前会话的 PSK（预共享密钥），在第一个飞行包里就直接带上加密的应用数据，省掉一个 RTT，弱网/跨国场景收益巨大。
- 风险一：重放攻击。0-RTT 数据没有防重放保证，攻击者抓包后可原样重发。所以只允许幂等的 GET 请求走 0-RTT，POST 下单/支付必须等服务端完成完整握手后再发。
- 风险二：前向保密不完整。0-RTT 密钥来自旧会话，攻击者若拿到旧密钥可解 0-RTT 数据。
- 工程实践：服务端要配置 0-RTT 白名单（只接受 GET），并在关键接口校验请求时间戳/nonce 防重放。

```javascript
// 服务端（Node + quic/nodejs 示意）拒绝 0-RTT 的非幂等请求
function handleRequest(req) {
  if (req.earlyData) {           // 0-RTT 期间到达的请求
    if (req.method !== 'GET') {
      return respond425TooEarly(req); // RFC 8470: Too Early
    }
  }
  return route(req);
}
```
