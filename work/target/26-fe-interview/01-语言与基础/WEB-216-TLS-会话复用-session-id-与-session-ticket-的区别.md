---
title: [WEB-216] TLS 会话复用 session ID 与 session ticket 的区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-216：TLS 会话复用 session ID 与 session ticket 的区别？

**答**：
- 目的相同：跳过完整密钥协商，用上次会话的密钥材料快速恢复连接，把 1-RTT 握手变成简短握手（TLS1.3 下 0-RTT 恢复）。
- Session ID：会话状态存服务端，客户端重连时带上 ID，服务端查缓存恢复。问题：多台服务器要共享缓存（粘性会话或分布式存储）。
- Session Ticket：服务端把会话状态加密后发给客户端保存，重连时原样带回，服务端解密即恢复——无需服务端存储，天然支持水平扩展。
- 安全注意：ticket 加密密钥泄漏则该密钥加密的所有 ticket 对应会话被解密，需定期轮换；ticket 对前向保密有削弱，TLS1.3 里 0-RTT 数据同理，敏感请求不应使用早期数据。

```bash
# 抓包验证会话恢复（简短握手无 Certificate）
openssl s_client -connect example.com:443 -reconnect </dev/null 2>/dev/null \
  | grep -E 'Reused|New'
# 第一次 New, TLSv1.3，后续 Reused, TLSv1.3
```
