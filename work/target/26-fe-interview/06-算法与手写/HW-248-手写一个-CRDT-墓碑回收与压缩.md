---
title: [HW-248] 手写一个 CRDT 墓碑回收与压缩
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-248：手写一个 CRDT 墓碑回收与压缩

**答**：
- 需求：实现 CRDTGC：统计 tombstone（deleted 元素）占比；回收条件：所有站点都已确认看到该删除（版本时钟覆盖）且 tombstone 连续段 >= 阈值；回收方式：压缩为单个"区间删除标记"元素（保留排序锚点），或快照重置（生成不含墓碑的新基线 + 之后日志）。
- 边界：回收不能破坏后续插入的定位（保留区间两端锚点元素）；版本时钟（每站点已见最高 counter 向量）判断"都已见"。
- 评分点：版本时钟判定；锚点保留；快照重置选项。

```javascript
class CRDTGC {
  constructor(doc) { this.doc = doc; this.clock = new Map(); }  // site -> maxCounter seen
  observe(op) {
    const [site, counter] = op.id;
    this.clock.set(site, Math.max(this.clock.get(site) ?? 0, counter));
  }
  canCollect(item) {                                       // 所有站点都已见该元素
    const [site, counter] = item.id;
    return [...this.clock.entries()].every(([s, c]) => s === site || c >= counter);
  }
  collect({ minRun = 50 } = {}) {                          // 连续墓碑压缩
    const items = this.doc.items;
    let run = [], saved = [];
    const flush = () => { if (run.length >= minRun) {
      const anchorLeft = run[0].left, anchorRight = run.at(-1).right;   // 保留两端锚点
      saved.push({ tombstoneRun: { left: anchorLeft, right: anchorRight, count: run.length } });
      run = [];
    } };
    for (const it of items) {
      if (it.deleted && this.canCollect(it)) { run.push(it); continue; }
      flush();
      if (!it.deleted || !this.canCollect(it)) saved.push(it);  // 活元素/未见墓碑保留
    }
    flush();
    this.doc.items = saved.filter(i => i.ch != null || i.tombstoneRun);
    return { collected: run.length, items: this.doc.items.length };
  }
  snapshotReset() {                                        // 快照重置：干净基线
    return { baseline: this.doc.text(), clock: new Map(this.clock) };
  }
}
```
