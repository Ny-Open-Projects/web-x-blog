---
title: [NODE-626] Node 服务的在线状态（presence）服务如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-626：在线状态服务
**答**:
- presence 模型：在线状态（在线/离开/隐身——多端聚合：任一端在线即在线——端级状态与账号级状态分层）、最后在线时间（离线展示"xx 前在线"——隐私分级：精确到分钟可配）、订阅关系（谁订阅谁的状态——好友/群成员范围授权）。
- 实现要点：状态源（WS 连接生命周期——连接/断开驱动状态、心跳超时判断——半开连接清理 ARC-346）、状态存储（Redis bitmap/set——好友级订阅扇出：状态变更推送给订阅者 ARC-379 presence）、状态节流（频繁断连抖动——状态变更防抖（重连窗口内不翻转））。
- 大规模：百万在线状态变更扇出（订阅关系裁剪——只推真正关心的、批量合并推送）、状态查询缓存（订阅者侧缓存——变更驱动失效）。
- 隐私与产品语义：隐身模式（可见性例外）、状态可见性配置（用户控制谁能看到——隐私设置）、企业场景（组织内可见）。
- 观测：状态翻转频率/扇出延迟/误报在线（半开连接）——presence 质量。
```javascript
ws.on('close', debounce(async () => {                            // 断连防抖
  const still = await registry.anyDeviceOnline(uid);             // 多端聚合
  if (!still) { await presence.offline(uid); await fanout(uid, 'offline'); }
}, 15e3));
```
