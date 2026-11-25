---
title: [SCN-845] 笔试题——实现历史词存储（IndexedDB LRU + 增量同步 + 删除传播）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-845：手写历史词存储与同步

**需求与边界**：
- 需求：历史词 IndexedDB 存储（上限 100 LRU）；服务端增量同步（lastSyncId）；删除双向传播（本地删除标记上传 + 服务端删除下发）；敏感词展示过滤。
- 边界：① 同步合并规则：同词取最新 ts、删除胜新增；② 同步失败重试且幂等（syncId）；③ 无痕模式不写库。

**答**：
```javascript
function createHistoryStore({ cap = 100 } = {}) {
  let lastSyncId = 0;
  async function add(q, { incognito = false } = {}) {
    if (incognito) return;                             // 无痕不写
    await idb.put('queries', { q, ts: Date.now(), deleted: false });
    await trim();
    scheduleSync();                                    // 异步同步（不阻塞输入）
  }
  async function remove(q) {
    await idb.update('queries', q, { deleted: true, ts: Date.now() });   // 标记删除（同步传播）
    scheduleSync();
  }
  async function trim() {                              // LRU 上限
    const all = await idb.all('queries');
    const active = all.filter(r => !r.deleted).sort((a, b) => b.ts - a.ts);
    for (const r of active.slice(cap)) await idb.delete('queries', r.q);
  }
  async function sync() {                              // 增量双向合并
    const local = await idb.all('queries');
    const delta = await api.post('/history/sync', { since: lastSyncId,
      changes: local.filter(r => r.ts > lastSyncId) }).catch(() => null);
    if (!delta) return scheduleSync();                 // 失败重试（syncId 幂等）
    for (const d of delta.changes) {
      const local0 = local.find(r => r.q === d.q);
      if (d.deleted || (local0 && local0.ts > d.ts && local0.deleted)) continue;  // 删除胜
      if (!local0 || d.ts > local0.ts) await idb.put('queries', d);
    }
    lastSyncId = delta.nextSyncId;
  }
  return { add, remove, sync,
    list: async () => (await idb.all('queries'))
      .filter(r => !r.deleted && !isSensitive(r.q))
      .sort((a, b) => b.ts - a.ts) };
}
```

**评分点**:
- 标记删除而非物理删（删除可传播）。
- 合并规则：删除胜新增、同词最新 ts。
- syncId 幂等 + 失败重试。
- 无痕不写库 + 展示前敏感过滤。
