---
title: [WCN-257] 跨 iframe/多窗口的信号同步方案？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-257：跨 iframe/多窗口的信号同步方案？
**答**：
- 同源跨窗口：BroadcastChannel/postMessage 广播写操作（信号写事件流）。
- 冲突：两端同时写 → last-write-wins 或向量时钟合并——按业务语义选。
- 应用：多屏协同（主屏购物车 ↔ 副屏详情）。
- 性能：广播只传「变更」不传全量；重连接时快照对齐。

```javascript
const bc = new BroadcastChannel('signals-sync');
function set(sig, v) { sig.value = v; bc.postMessage({ id: sig.id, v }); }
bc.onmessage = ({ data }) => { mute(() => byId(data.id).value = data.v); }; // mute 防回环广播
r
```
