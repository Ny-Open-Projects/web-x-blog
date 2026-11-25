---
title: [NODE-742] 笔试题——实现请求合并器（Dataloader 模式）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-742：手写 Dataloader

**需求与边界**：
- 需求：批量+缓存合并器（SCN-NODE-662）——① batch 窗口（微任务合并——同 tick 的 key 合一次批量 IN）；② per-key memoization（同请求重复 key 缓存）；③ per-request 实例（跨请求不缓存——安全红线）；④ 批量失败语义（部分失败——结果按位对应）。
- 边界：① batch 调度用 process.nextTick/setImmediate（合并窗口）；② 错误按 key 传播（一个 key 失败不影响其他——按位 reject）；③ maxBatch 上限（IN 上限拆批）。

**答**：
```javascript
class DataLoader {
  constructor(batchFn, { maxBatch = 500 } = {}) {
    this.batchFn = batchFn; this.cache = new Map();    // per-request 缓存（SCN-NODE-662）
    this.batch = []; this.scheduled = false;
  }
  load(key) {
    if (this.cache.has(key)) return this.cache.get(key);   // memoize
    const promise = new Promise((resolve, reject) => {
      this.batch.push({ key, resolve, reject });
      if (!this.scheduled) {
        this.scheduled = true;
        process.nextTick(() => this.dispatch());       // 微任务合并窗口
      }
    });
    this.cache.set(key, promise);
    return promise;
  }
  async dispatch() {
    const b = this.batch; this.batch = []; this.scheduled = false;
    const keys = b.map(x => x.key);
    const chunks = chunk(keys, this.maxBatch);         // IN 上限拆批
    const all = await Promise.all(chunks.map(c => this.batchFn(c)));
    const byKey = new Map(all.flat().map(r => [r.key ?? r.id, r]));   // 按位对应
    b.forEach(({ key, resolve, reject }) =>
      byKey.has(key) ? resolve(byKey.get(key)) : reject(new NotFound(key)));   // 部分失败按位
  }
}
// 用法（每请求实例——安全红线）
app.use((req, res, next) => { req.dl = new DataLoader(batchUsers); next(); });
```

**评分点**:
- nextTick 合并窗口（同 tick keys 一次 IN——N+1 解）。
- per-request memoize + 实例化（跨请求缓存 = 数据越权——SCN-NODE-662 红线）。
- 部分失败按位对应（一个 key 失败不影响其他）。
- maxBatch 拆批（IN 上限防御）。
