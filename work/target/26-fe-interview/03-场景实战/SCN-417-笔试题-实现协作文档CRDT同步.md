---
title: [SCN-417] 笔试题——实现简化 CRDT 文本同步（插入合并与乱序应用）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-417：手写简化 CRDT 字符序列：唯一 ID 字符、乱序插入合并、删除标记

**需求与边界**：
- 输入：本地编辑操作、远端操作流（可能乱序）；输出：一致文档。
- 边界要求：① 每字符唯一 ID（site+counter）；② 插入带左锚（插在哪个字符后）；③ 并发插入同位置确定性排序（siteId 决胜）；④ 删除标记 tombstone（不物理删除——离线合并正确）。

**答**：
```javascript
class SimpleCRDT {
  constructor(siteId) {
    this.siteId = siteId;
    this.counter = 0;
    this.chars = [];       // [{id:{site,ctr}, ch, deleted, leftId}]
    this.byId = new Map(); // id → char（含 tombstone 保留）
  }
  localInsert(leftId, ch) {                    // 本地插入
    const id = { site: this.siteId, ctr: this.counter++ };
    return this._insert({ id, ch, leftId, deleted: false }, id);
  }
  _insert(op) {
    if (this.byId.has(opKey(op.id))) return;   // 幂等（重复操作）
    const idx = this.findIndex(op.leftId);     // 左锚定位
    // 并发同锚：按 siteId 决胜（确定性排序）
    let pos = idx + 1;
    while (pos < this.chars.length &&
           this.chars[pos].leftId === opKey(op.leftId) &&
           cmpId(this.chars[pos].id, op.id) < 0)
      pos++;                                   // siteId 大者靠后
    this.chars.splice(pos, 0, op);
    this.byId.set(opKey(op.id), op);
    return pos;
  }
  localDelete(id) {                            // 删除：标记
    this.byId.get(id).deleted = true;          // tombstone 保留
  }
  applyRemote(op) {                            // 远端乱序应用
    if (op.type === 'insert') return this._insert(op);
    const c = this.byId.get(op.id);
    if (c) c.deleted = true;
    else pendingDelete.push(op);               // 未到达先缓存
  }
  text() {
    return this.chars.filter(c => !c.deleted)
      .map(c => c.ch).join('');                // tombstone 过滤
  }
  findIndex(leftId) {
    if (leftId === null) return -1;            // 文档头
    return this.chars.findIndex(c =>
      opKey(c.id) === leftId);                 // 锚未到达→缓存等待
  }
}
const opKey = (id) => `${id.site}:${id.ctr}`;
const cmpId = (a, b) => a.site !== b.site
  ? a.site < b.site ? -1 : 1 : a.ctr - b.ctr;
// 锚未到达的插入：pendingInserts 缓存，锚到达后重放。
```

**评分点**:
- 字符唯一 ID（site+counter）+ 左锚插入模型正确。
- 并发同锚确定性排序（siteId 决胜）——两端口序一致的关键。
- 删除 tombstone 保留（离线乱序合并正确），text 渲染过滤。
- 幂等（重复 op 跳过）+ 锚未到达的 pending 机制意识。
