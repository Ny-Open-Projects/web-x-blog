---
title: [AV-428] 手写一个 CRDT 数组的本地实现（带 siteId 的 LWW 列表）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## AV-428：手写一个 CRDT 数组的本地实现（带 siteId 的 LWW 列表）

**答**：
- 需求：implement LWWList(siteId)。insert(index, value) 产生带 (ts, siteId) 的元素；remoteInsert(element) 合并（同 index 冲突 ts 新者胜，ts 相同 siteId 大者胜）；toArray() 输出排序结果；保证两端合并结果一致。
- 边界：ts 用逻辑时钟（递增）；并发同 index 插入两侧各保留自己的再按规则排序；删除走墓碑。
- 评分点：LWW 规则；逻辑时钟；墓碑；排序一致

```javascript
class LWWList {
  constructor(siteId) {
    this.siteId = siteId; this.clock = 0;
    this.items = [];                                  // { id, value, ts, site, deleted }
  }
  insert(index, value) {
    this.clock++;
    const item = { id: `${this.siteId}-${this.clock}`, value,
      ts: this.clock, site: this.siteId, deleted: false };
    this.items.splice(index, 0, item);
    return item;
  }
  remoteUpsert(item) {
    this.clock = Math.max(this.clock, item.ts);
    const existing = this.items.find(i => i.id === item.id);
    if (existing) {
      if (item.ts > existing.ts) Object.assign(existing, item);   // LWW
      return;
    }
    const at = Math.min(item.index ?? this.items.length, this.items.length);
    this.items.splice(at, 0, item);
    this.items.sort((a, b) => a.ts - b.ts || (a.site < b.site ? -1 : 1));
  }
  toArray() { return this.items.filter(i => !i.deleted).map(i => i.value); }
}
```
