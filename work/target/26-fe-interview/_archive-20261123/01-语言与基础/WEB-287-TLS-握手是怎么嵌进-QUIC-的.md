---
title: [WEB-287] TLS 握手是怎么嵌进 QUIC 的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-287：TLS 握手是怎么嵌进 QUIC 的？
**答**：
- QUIC 把 TLS1.3 的握手消息直接放在 CRYPTO 帧里传输，TLS 记录层被剥离，握手和传输协议融为一体（不是"先 TCP 后 TLS"两步）。
- 握手完成后 QUIC 内置的加密立即生效：除了头部少数字段，包内容全部加密，包括包号。
- 收益：握手更少往返、更难被中间盒篡改；代价：抓包调试必须先解密（SSLKEYLOGFILE）。

```javascript
// QUIC + TLS1.3 1-RTT 握手时序（示意）
// Client Initial 包: CRYPTO 帧(CLIHELLO)  ---->
//   <---- Server Initial: CRYPTO(SH) + EncryptedExtensions + 证书
// Client: CRYPTO(FINISHED) + 首个 1-RTT 应用数据（不等确认！）
//   <---- Server: CRYPTO(FINISHED) + 1-RTT 数据
console.log('TLS 消息走 CRYPTO 帧，握手完成前已可发送 0.5-RTT 应用数据');
```
