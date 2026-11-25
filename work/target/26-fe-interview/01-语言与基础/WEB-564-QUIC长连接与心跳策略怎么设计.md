---
title: [WEB-564] QUIC 长连接与心跳策略怎么设计
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-564：QUIC 长连接与心跳策略怎么设计

**答**：
- QUIC 有 keep-alive 机制（发 Ping 帧），但 NAT/防火墙的 UDP 映射表项超时通常 30s~几分钟，比 TCP 空闲超时更激进——心跳周期要按最短的那一环定
- 服务端 max_idle_timeout 与客户端心跳配合：客户端按 min(服务端 idle 的 1/2, NAT 超时) 发 Ping；弱网省电场景可协商更大的 idle 减少唤醒
- 移动端功耗权衡：心跳太密耗电、太疏连接被 NAT 断——用网络切换事件做「事件驱动保活」替代高频定时心跳
- 连接断了靠「快速重建 + 0-RTT」兜底：重连成本 0 RTT 级，所以可以接受稍激进的心跳间隔，断了立刻重建即可
- 监控对齐：上报连接存活时长分布与 NAT 断连占比，用数据回归心跳周期

```javascript
// 事件驱动保活: 网络事件+空闲阈值, 而非固定高频心跳
const wt = new WebTransport('https://api.example.com/wt');
await wt.ready;
let heartbeat = setInterval(() => wt.datagrams.writable.getWriter().write(PING), 25_000);
navigator.connection?.addEventListener('change', async () => {
  clearInterval(heartbeat);
  if (wt.closed) { await reconnect0RTT(); }   // 断了立即0-RTT重建
  heartbeat = setInterval(() => wt.datagrams.writable.getWriter().write(PING), 25_000);
});
```
