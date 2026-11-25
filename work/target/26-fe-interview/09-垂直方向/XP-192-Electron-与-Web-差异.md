---
title: [XP-192] Electron 与 Web 差异：Node 能力带来的架构变化
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-192：Electron 与 Web 差异：Node 能力带来的架构变化

**答**：
- Electron vs Web 架构差异：Node 能力（文件系统/进程/原生模块）使客户端架构多出「本地数据层」「离线优先」「系统集成」三块。
- 本地数据层：SQLite 本地库 + 服务端同步（离线优先，HW-336 复用）；系统集成：托盘/通知/快捷键/文件关联。
- 数据一致性：本地写 + 服务端同步 → 冲突解决（最后写胜/LWW）——离线编辑器场景。

```javascript
class DesktopDataLayer {
  constructor() { this.local = new SQLiteDB(); this.syncQueue = []; }
  async write(entity) {                                           // 离线优先写
    const id = await this.local.insert(entity);                    // 先写本地（快）
    this.syncQueue.push(entity);                                   // 入同步队列
    if (this.isOnline()) this.flushSync();                          // 在线即同步
    return id;
  }
  async flushSync() {                                              // 同步队列
    while (this.syncQueue.length && this.isOnline()) {
      const entity = this.syncQueue.shift();
      await serverSync.push(entity).catch(() => this.syncQueue.unshift(entity));   // 失败回队
    }
  }
  onConflict(local, remote) { return local.ts > remote.ts ? local : remote; }   // LWW 冲突
}
```
