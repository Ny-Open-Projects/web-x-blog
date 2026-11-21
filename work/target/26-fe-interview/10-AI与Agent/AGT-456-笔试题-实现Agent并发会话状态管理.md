---
title: [AGT-456] 笔试题——实现并发会话状态管理（状态外置+并发串号防护）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-456：手写会话状态服务：会话外置存储、并发写冲突、串号检测

**需求与边界**：
- 输入：会话操作（get/append）；输出：并发安全的状态管理。
- 边界要求：① 状态外置（进程重启不丢）；② 并发 append 乐观锁（版本冲突重试）；③ 会话 id 全链路贯穿（串号检测：读到非本会话数据即告警）；④ TTL 与清理。

**答**：
```javascript
class SessionStore {
  constructor({ db, ttlMs = 7 * 864e5 }) {
    this.db = db; this.ttlMs = ttlMs;
  }
  async get(convId, userId) {
    const s = await this.db.get(convId);
    if (!s) return null;
    if (s.userId !== userId) {                    // 串号检测
      alert('SESSION_CROSS_WIRE', { convId, userId });
      throw new Error('会话归属校验失败');
    }
    if (Date.now() - s.updatedAt > this.ttlMs)
      return { ...s, expired: true };             // 过期标记（软）
    return s;
  }
  async append(convId, userId, msg) {
    for (let retry = 0; retry < 3; retry++) {
      const s = await this.get(convId, userId);
      const version = s?.version ?? 0;
      const next = { messages: [...(s?.messages ?? []),
        { ...msg, seq: version }], version: version + 1,
        userId, updatedAt: Date.now() };
      // 乐观锁：version 不匹配即冲突
      const ok = await this.db.compareAndSet(convId, version, next);
      if (ok) return next;
      await sleep(10 * (retry + 1));              // 冲突退避重试
    }
    throw new Error('并发冲突，重试耗尽');
  }
  async cleanup() {                               // TTL 清理
    return this.db.deleteWhere({ updatedAt:
      { $lt: Date.now() - this.ttlMs } });
  }
}
// compareAndSet: UPDATE ... WHERE version = ? （原子条件写）。
```

**评分点**:
- 状态外置存储（重启可恢复）+ TTL 过期处理。
- 乐观锁 CAS 实现并发写安全（冲突退避重试上限）。
- 串号检测（归属校验失败即告警抛错）——多用户隔离防线。
- seq 由版本号生成（消息序一致性）。
