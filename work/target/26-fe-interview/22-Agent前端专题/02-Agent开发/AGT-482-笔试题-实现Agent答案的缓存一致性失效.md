---
title: [AGT-482] 笔试题——实现缓存一致性失效（数据变更联动+软失效+预热）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-482：手写缓存失效：变更事件订阅、依赖图谱失效、预热与雪崩防护

**需求与边界**：
- 输入：数据变更事件（文档/配置/模型版本）；输出：缓存失效与预热计划。
- 边界要求：① 缓存项注册依赖（哪些数据 key 影响它）；② 变更事件按依赖图精确失效（不整库清空）；③ 失效后异步预热高频项（防缓存击穿）；④ 雪崩防护（失效打散+单飞重建 singleflight）。

**答**：
```javascript
class CacheInvalidator {
  constructor({ cache, depsGraph, warmer }) {
    this.cache = cache; this.deps = depsGraph;   // cacheKey -> [dataKeys]
    this.warmer = warmer;
    this.inflight = new Map();                   // singleflight
  }
  async onDataChanged(ev) {
    // 1. 依赖图反查：受影响缓存项
    const targets = [...this.deps.entries()]
      .filter(([, keys]) => keys.some(k =>
        k === ev.key || k.startsWith(ev.key + ':')))
      .map(([ck]) => ck);
    // 2. 失效打散（随机延迟防同时重建雪崩）
    await Promise.all(targets.map((ck, i) =>
      delay(i * 200 + Math.random() * 300)
        .then(() => this.cache.delete(ck))));
    // 3. 高频项异步预热（singleflight 防击穿）
    const hot = targets.filter(ck => this.hotKeys.has(ck));
    await Promise.all(hot.map(ck => this.warm(ck)));
    return { invalidated: targets.length, warmed: hot.length };
  }
  async warm(ck) {
    if (this.inflight.has(ck)) return this.inflight.get(ck);
    const p = this.warmer(ck).finally(() =>
      this.inflight.delete(ck));
    this.inflight.set(ck, p);
    return p;
  }
  register(cacheKey, dataKeys, { hot = false } = {}) {
    this.deps.set(cacheKey, dataKeys);           // 注册依赖
    if (hot) this.hotKeys.add(cacheKey);
  }
}
// 版本联动：缓存值内嵌数据版本号，
// 读取时校验版本（双保险：失效+版本校验）。
```

**评分点**:
- 依赖图谱精确失效（注册制），非整库清空。
- 失效打散随机延迟 + singleflight 重建（防击穿与雪崩双防护）。
- 高频项注册+异步预热。
- 版本号内嵌双保险意识（失效失效不了时版本校验兜底）。
