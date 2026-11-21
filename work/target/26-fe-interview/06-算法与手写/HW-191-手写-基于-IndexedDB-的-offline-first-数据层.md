---
title: [HW-191] 手写 offline-first 数据层——本地优先读写 + 服务端同步队列 + 冲突版本向量
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：offline-first 数据层（本地优先架构）：读写都走本地 IDB（离线可用零延迟），写操作进同步队列（带版本号），恢复后与服务端对账（last-write-win 或版本向量检测冲突）。三层：Store（IDB 封装 HW-107）、Queue（outbox）、Sync（重放 + 冲突处理）。

```javascript
class OfflineStore {
  #queue = [];
  async get(key) { return (await db.get('data', key))?.value; }
  async put(key, value) {
    const rev = (await db.get('data', key))?.rev ?? 0;
    await db.put('data', { value, rev: rev + 1, dirty: true }, key);   // 本地版本号递增
    this.#queue.push({ key, rev: rev + 1, value, at: Date.now() });
    scheduleSync(this);
    return rev + 1;
  }
  async sync(server) {                                     // 恢复后对账
    while (this.#queue.length) {
      const op = this.#queue[0];
      const result = await server.put(op.key, op.value, { ifMatchRev: op.rev - 1 }).catch(() => null);
      if (!result) break;                                   // 断网：停住等下次
      if (result.conflict) {                                 // 服务端 rev 更新：冲突
        this.#queue.shift();
        await onConflict(op, result.serverValue);            // UI 提示用户选择（不静默覆盖）
        continue;
      }
      await db.put('data', { value: op.value, rev: result.rev, dirty: false }, op.key);
      this.#queue.shift();                                   // 同步成功：清 dirty
    }
  }
}
// 语义：
// 本地优先：读写零延迟、离线完整可用 —— 服务端是"同步目标"不是"数据源"
// rev 版本号：本地递增 + 服务端 ifMatchRev 条件写（乐观锁）—— 冲突可检测
// 冲突不静默：UI 提示（本地值 vs 服务端值二选一）—— offline-first 的正确姿势（PER-331 脏读防线）
// 断网停住：队列保留，下次 sync 续传（HW-108 语义）
```

**评分点**：
- 本地优先读写 + 同步队列的三层架构——本题核心。
- rev 版本号 + ifMatchRev 条件写的乐观锁冲突检测。
- 冲突 UI 提示不静默覆盖（PER-331）。
- 断网停住续传（HW-108）与 dirty 标记的清理时机。
