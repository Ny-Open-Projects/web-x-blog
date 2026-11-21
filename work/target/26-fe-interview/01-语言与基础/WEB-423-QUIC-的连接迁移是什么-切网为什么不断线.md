---
title: [WEB-423] QUIC 的连接迁移是什么，切网为什么不断线
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-423：QUIC 的连接迁移是什么，切网为什么不断线

**答**：
- TCP 用「四元组」（源IP/端口+目标IP/端口）标识连接，WiFi 切 4G 时 IP 变了，连接必须断开重连
- QUIC 用 Connection ID 标识连接，IP 变了只要 CID 还在，连接继续——这就是连接迁移
- 收益场景：地铁通勤切网、手机热点切换，页面里的长连接（H3 请求、WebTransport）不断
- 前端注意：迁移后的 RTT 变了，若做了网络质量自适应（码率、图片清晰度），要监听 `navigator.connection.change` 重新评估
- 钩子：迁移需要双方配合（PATH_CHALLENGE 帧校验），NAT 重绑定或运营商中间盒可能干扰迁移成功

```javascript
// 感知网络切换，配合连接迁移调整策略
const c = navigator.connection;
c?.addEventListener('change', () => {
  console.log('网络变化:', c.effectiveType, c.rtt);
  // 重新评估图片清晰度/视频码率
});
```
