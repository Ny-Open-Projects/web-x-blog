---
title: [WEB-288] 连接迁移是什么？WiFi 切 5G 时前端为什么几乎无感？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-288：连接迁移是什么？WiFi 切 5G 时前端为什么几乎无感？
**答**：
- TCP 连接由「源IP+源端口+目的IP+目的端口」四元组标识，网络切换后 IP 变了，连接只能重建，重新握手 1-2 个 RTT。
- QUIC 用 64 位 Connection ID 标识连接，IP 变了只要 CID 不变，连接照用，密码学上下文都在。
- 前端感知：上传/下载不断流，WebSocket 类业务不再频繁重连；配合 Path Validation（PATH_CHALLENGE 帧）验证新路径可达。

```javascript
// TCP: 四元组变了 → 连接死亡 → 重新 DNS/握手/TLS（1-2 RTT 起步）
// QUIC: CID 不变 → PATH_CHALLENGE/RESPONSE 验证新路径 → 继续传输
const quicConn = { cid: 'ab12cd34', path: { ip: '192.168.1.5' }, streams: 3 };
function onNetworkChange(conn, newIp) {      // WiFi → 5G
  conn.path.ip = newIp;
  conn.pendingPathChallenge = true;          // 发起路径验证
  console.log('连接保持，仅验证新路径:', conn.cid, conn.path.ip);
}
onNetworkChange(quicConn, '10.0.0.8');
```
