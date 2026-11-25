---
title: [WEB-299] TLS 1.3 为什么只需要 1-RTT？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-299：TLS 1.3 为什么只需要 1-RTT？
**答**：
- TLS1.2 要 2-RTT：先协商参数再密钥交换再确认；TLS1.3 把密钥交换参数（key_share）直接放进 ClientHello，服务端一个 RTT 就能确认双方密钥。
- 核心是"猜参数"：客户端预发常用 group 的 ECDHE 公钥，服务端选定后直接派生密钥，协商与交换合并。
- 配合会话恢复还能 0-RTT（PSK），但早数据有重放风险，只放幂等请求。

```javascript
// TLS1.3 1-RTT 时序
// C: ClientHello(key_share=x25519 公钥) →
//        <- S: ServerHello(key_share) + {EncryptedExtensions} + 证书 + FINISHED
// C: FINISHED + [应用数据]                        ← 第二个往返之前已有数据
console.log('ClientHello 带公钥 → 1-RTT 完成握手并开始加密传输');
```
