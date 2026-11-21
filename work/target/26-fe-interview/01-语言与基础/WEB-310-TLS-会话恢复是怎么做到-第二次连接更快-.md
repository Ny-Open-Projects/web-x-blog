---
title: [WEB-310] TLS 会话恢复是怎么做到"第二次连接更快"的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-310：TLS 会话恢复是怎么做到"第二次连接更快"的？
**答**：
- 全握手要 1-2 RTT；会话恢复用上次的秘密复用密钥：TLS1.2 用 session ticket（服务器加密的会话状态给客户端保管），TLS1.3 用 PSK。
- 恢复握手只要 1-RTT，配 early data 可 0-RTT——代价是早数据可重放。
- 前端关联：keep-alive 断开后重连、Service Worker fetch、图片分片加载等都受益；CDN 边缘节点间 ticket 密钥共享才能跨节点恢复。

```javascript
// TLS1.3 PSK 恢复
// C: ClientHello(psk_identity=ticket, early_data)  →
//        <- S: ServerHello + FINISHED（1-RTT，密钥已就绪）
const resumption = (first, second) => ({
  first: first + ' RTT(全握手)',
  second: Math.max(0, second - 1) + ' RTT(PSK恢复)',
});
console.log(resumption(1, 1)); // { first: '1 RTT(全握手)', second: '0 RTT(PSK恢复)' }
```
