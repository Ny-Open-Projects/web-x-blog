---
title: [HW-247] 手写一个 CRDT 并发插入合并：多站点操作流收敛验证
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-247：手写一个 CRDT 并发插入合并：多站点操作流收敛验证

**答**：
- 需求：实现 CRDTMerger：接收多站点操作日志 [{site, type: ins|del, id, ch, left, right}]，乱序到达时缓存依赖（left 未达则等待），依赖齐后按序 apply；提供 converged(docs) 断言多站点 text() 一致。
- 边界：乱序缓存按依赖图释放（拓扑序）；循环依赖不可能（链结构保证）但要防丢失 left 永不达（超时告警）；重复 apply 幂等。
- 评分点：乱序依赖缓存；幂等 apply；收敛断言。

```javascript
class CRDTMerger {
  constructor(doc) { this.doc = doc; this.waiting = []; this.seen = new Set(); }
  apply(op) {
    if (this.seen.has(key(op.id))) return;                 // 幂等
    const depReady = !op.left[0] || this.seen.has(key(op.left));
    if (!depReady) { this.waiting.push(op); return; }
    this.doc.remoteApply(op);
    this.seen.add(key(op.id));
    this.flushWaiting();                                   // 依赖链释放
  }
  flushWaiting() {
    let progressed = true;
    while (progressed) {
      progressed = false;
      this.waiting = this.waiting.filter(op => {
        if (this.seen.has(key(op.left))) { this.apply(op); progressed = true; return false; }
        return true;                                       // 依赖未齐：继续等
      });
    }
  }
  converged(others) {                                      // 多站点收敛断言
    const base = this.doc.text();
    return others.every(d => d.text() === base);
  }
}
const key = id => id.join(':');
```
