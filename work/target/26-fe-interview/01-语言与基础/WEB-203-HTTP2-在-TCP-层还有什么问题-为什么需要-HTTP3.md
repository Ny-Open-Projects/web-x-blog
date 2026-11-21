---
title: [WEB-203] HTTP/2 在 TCP 层还有什么问题？为什么需要 HTTP/3？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-203：HTTP/2 在 TCP 层还有什么问题？为什么需要 HTTP/3？

**答**：
- TCP 层队头阻塞：HTTP/2 的所有 stream 共用一条 TCP 字节流，任一包丢失，TCP 必须等重传补齐才能把后续数据交给应用层，所有 stream 一起卡住。丢包率高时 HTTP/2 甚至不如 HTTP/1.1 的多连接。
- TCP 连接建立慢：TCP 握手 + TLS 握手叠加，首次要 2~3 个 RTT 才能发数据。
- 连接与网络强绑定：TCP 四元组（源IP/源端口/目的IP/目的端口）变了连接就断，Wi-Fi 切 4G 必须重来。
- HTTP/3 用 QUIC 解决：基于 UDP，stream 之间独立确认（丢包只堵自己的 stream），1-RTT 甚至 0-RTT 建连，连接 ID 与网络解耦支持迁移；TLS 1.3 内建其中。

```javascript
// 检测当前环境是否支持 HTTP/3（生产灰度常用做法）
async function probeHttp3() {
  // 浏览器无法直接查协议版本，通常靠资源时序推断或服务端响应头
  const res = await fetch('/__http3_probe', { priority: 'low' });
  // 服务端在 Nginx 上可加 header 暴露实际协商协议
  console.log(res.headers.get('x-protocol')); // h3 / h2 / http/1.1
}
```
