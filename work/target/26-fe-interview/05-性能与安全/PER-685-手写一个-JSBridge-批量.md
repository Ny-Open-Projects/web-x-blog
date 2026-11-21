---
title: [PER-685] 手写一个 JSBridge 批量调用器：rAF 周期合并调用、调用耗时统计与超预算告警
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-685：手写一个 JSBridge 批量调用器：rAF 周期合并调用、调用耗时统计与超预算告警

**答**：
- 批量器：`bridgeBatch('getLocation', params)` 收集一帧内的调用，rAF 回调时打包成 `invokeBatch([{method, params, cbId}...])` 一次往返，结果按 cbId 分发。
- 要点：只有可延迟的方法进批量（读类），写类/一次性类立即调用；结果分发要与请求一一对应；耗时统计按方法聚合（次数/p95/总耗时占比）。
- 边界：批量大小上限（防单包过大）；Native 不支持 invokeBatch 时降级逐个调用；超预算告警按方法排序输出治理建议。
- 评分点：读/写分类与降级路径。

```javascript

class BatchedBridge {
  constructor(native, { maxBatch = 10 } = {}) {
    this.native = native; this.queue = []; this.stats = new Map(); this.scheduled = false;
  }
  call(method, params, { batchable = true } = {}) {
    return new Promise((resolve, reject) => {
      const item = { method, params, resolve, reject, t0: performance.now() };
      if (!batchable || !this.native.supportsBatch) {           // 写类/降级：立即调用
        return this.execOne(item);
      }
      this.queue.push(item);
      if (!this.scheduled) { this.scheduled = true; requestAnimationFrame(() => this.flush()); }
    });
  }
  flush() {
    this.scheduled = false;
    const batch = this.queue.splice(0, 10);                     // 上限防大包
    if (!batch.length) return;
    this.native.invokeBatch(batch.map(b => ({ m: b.method, p: b.params, id: b.method + batch.indexOf(b) })))
      .then(results => results.forEach((r, i) => this.settle(batch[i], r)))
      .catch(() => batch.forEach(b => this.execOne(b)));        // 失败降级逐个
  }
  execOne(item) { this.native.invoke(item.method, item.params).then(r => this.settle(item, r)); }
  settle(item, r) {
    const dur = performance.now() - item.t0;                    // 往返耗时统计
    const s = this.stats.get(item.method) ??= { n: 0, total: 0, max: 0 };
    s.n++; s.total += dur; s.max = Math.max(s.max, dur);
    r.ok ? item.resolve(r.data) : item.reject(r);
  }
  report() { // 总耗时占比 > 15% 的方法优先治理
    return [...this.stats.entries()].map(([m, s]) =>
      ({ m, p: s.n, avgMs: +(s.total / s.n).toFixed(1) }))
      .sort((a, b) => b.avgMs - a.avgMs);
  }
}
```
