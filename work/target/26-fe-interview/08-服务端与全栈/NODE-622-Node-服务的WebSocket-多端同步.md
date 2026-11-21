---
title: [NODE-622] Node 服务的 WebSocket 多端同步（同账号多设备消息一致）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-622：WS 多端同步
**答**:
- 场景：同账号手机+Web 同时在线——消息/未读/状态跨端一致（ARC-500/502 的服务端实现）。
- 同步协议：消息广播到全设备（同账号所有活跃连接——各端各自 seq 去重）、已读水位同步（任一端已读 → 广播水位变更——各端未读重算取 max ARC-502）、设备间操作同步（撤回/删除——操作广播各端生效）。
- 实现要点：设备注册表（uid → 各设备连接——按设备路由与广播）、增量协议（新上线设备：先快照后增量——上线时拉 lastSeq 补齐 NODE-543）、冲突语义（两端同时已读不同 seq——max 合并无冲突；两端同时编辑——业务冲突处理）。
- 性能：多端扇出（账号级广播——设备数上限）、离线设备（不在线不推——靠离线消息 ARC-543）、会话设备数控制。
- 观测：多端同步延迟（操作到各端生效 P95）、不一致事件（端上检测到状态分歧上报——对账修复）。
```javascript
// 账号级广播
async function broadcastToUser(uid, msg) {
  const devices = await registry.connectionsOf(uid);             // 所有在线设备
  devices.forEach(d => d.ws.send(seq(msg)));                     // 各端 seq 去重
}
// 已读同步：readReport(uid, deviceId, seq) → broadcastToUser(uid, { type:'read', seq }) —— 各端取 max
```
