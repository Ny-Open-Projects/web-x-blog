---
title: [WEB-206] QUIC 连接迁移是怎么回事？解决了什么问题？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-206：QUIC 连接迁移是怎么回事？解决了什么问题？

**答**：
- TCP 用四元组标识连接，IP 变了连接必断——手机从 Wi-Fi 切 4G、电梯里基站切换，正在进行的请求全部中断重连。
- QUIC 用连接 ID（Connection ID）标识连接，与 IP/端口解耦。网络变化后客户端用同一 Connection ID 继续发包，服务端验证密钥材料后无缝续传，请求不断。
- 迁移分两类：路径验证（PATH_CHALLENGE/RESPONSE 确认新路径可达）与地址变更时的反欺骗校验（防止攻击者伪造源地址发动放大攻击）。
- 对业务的价值：IM 推送不断线、直播不卡顿重连、上传大文件切换网络后继续传。

```javascript
// 移动端弱网场景对比（示意）
// TCP: Wi-Fi(192.168.1.5) → 4G(10.20.30.40)，四元组变化
//      → 连接 RST → TCP 重握手 + TLS 重握手 ≈ 秒级中断，未完成请求失败
// QUIC: Connection ID 不变 → PATH_CHALLENGE 验证新路径 → 请求继续
const upload = fetch('/api/upload', { method: 'POST', body: bigFile });
// HTTP/3 下网络切换，upload 的 promise 不会 reject
```
