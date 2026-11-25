---
title: [PER-1019] 从浏览器视角看一次 HTTPS 请求的完整成本模型
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1019：从浏览器视角看一次 HTTPS 请求的完整成本模型

**答**：
- 成本拆解：DNS（0~2 RTT）→ TCP 握手（1 RTT）→ TLS 握手（1~2 RTT）→ 请求响应（1 RTT）；弱网高延迟下握手占大头。
- 优化杠杆：preconnect 提前并行握手、TLS 1.3 会话复用（1-RTT/0-RTT）、QUIC 合并握手与传输、HTTP Keep-Alive 复用连接。
- 实测方法：resource timing 的 domainLookupStart/End、connectStart/End、secureConnectionStart 各段差值。
- 追问点：为什么 preconnect 要限定关键第三方域名——预连接本身消耗服务器资源，泛化使用适得其反。

```javascript
// 请求成本分解
function requestCost(entry) {   // resource timing entry
  const dns = entry.domainLookupEnd - entry.domainLookupStart;
  const tcp = entry.connectEnd - entry.connectStart;
  const tls = entry.requestStart - entry.secureConnectionStart;
  const wait = entry.responseStart - entry.requestStart;
  const download = entry.responseEnd - entry.responseStart;
  const hand = dns + tcp + tls;
  return { dns, tcp, tls, wait, download,
    handshakeShare: +(hand / (entry.responseEnd - entry.startTime) * 100).toFixed(1) + '%' };
}
// handshakeShare 高 -> 用 preconnect/会话复用攻击握手段
```
