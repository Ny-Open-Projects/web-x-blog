---
title: [AV-391] WebSocket 重连与状态同步的完整流程
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-391：WebSocket 重连与状态同步的完整流程

**答**：
- 断线检测：心跳超时（5s 无 pong）/ws onclose；指数退避重连（1s/2s/4s，上限 30s）+ 抖动。
- 重连后同步：发本地 lastSeq -> 服务端回增量（缺失区间）或全量快照。
- 本地缓存：离线期间操作入队（内存/IndexedDB），重连后 flush 并接受服务端合并结果。

```javascript
// 重连同步流程
class SyncClient {
  async reconnect() {
    for (let attempt = 1; attempt <= 5; attempt++) {
      const delay = Math.min(30_000, 1000 * 2 ** attempt) * Math.random();
      await sleep(delay);
      try { await this.connect(); break; } catch {}
    }
    const { updates } = await rpc('sync-since', { seq: this.lastSeq });
    for (const u of updates) Y.applyUpdate(this.doc, u);
    for (const u of this.offlineQueue) wsSend(u);      // 本地离线操作
    this.offlineQueue = [];
  }
}
```
