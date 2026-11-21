---
title: [DP-345] 笔试题：手写 SSR 页面缓存层？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-345：笔试题：手写 SSR 页面缓存层？
**题目**：实现 SSR 页面缓存：1) 页面级缓存（URL+查询签名 → HTML）；2) TTL + 主动失效（数据变更时 purge 路径）；3) stale-while-revalidate（过期先返回旧值后台刷新）；4) 缓存穿透保护（并发同 key 只渲染一次）。
**评分点**：
- 缓存 key 规范化（查询排序、用户无关字段剥离）。
- SWR 双返回（旧值立即 + 后台刷新）。
- 单飞防击穿（inflight Map）。
- 失效按路径模式（glob）。
```javascript
class PageCache {
  #store = new Map();       // key → { html, ts }
  #inflight = new Map();
  key(url) { const u = new URL(url, 'http://x');
    const sp = [...u.searchParams.entries()].sort(([a], [b]) => a < b ? -1 : 1);   // 1) 规范化
    return `${u.pathname}?${new URLSearchParams(sp)}`; }
  async get(url, render, { ttl = 30_000 } = {}) {
    const k = this.key(url);
    const cached = this.#store.get(k);
    if (cached && Date.now() - cached.ts < ttl) return cached.html;
    if (cached) {                                            // 3) SWR
      this.#refresh(k, render);
      return cached.html;
    }
    if (this.#inflight.has(k)) return this.#inflight.get(k);   // 4) 单飞
    const p = render().then(html => { this.#store.set(k, { html, ts: Date.now() });
      this.#inflight.delete(k); return html; });
    this.#inflight.set(k, p);
    return p;
  }
  #refresh(k, render) { if (!this.#inflight.has(k)) { const p = render()
    .then(html => this.#store.set(k, { html, ts: Date.now() })); this.#inflight.set(k, p); } }
  purge(pattern) {                                            // 2) 模式失效
    const re = new RegExp('^' + pattern.replace(/\*/g, '.*'));
    for (const k of [...this.#store.keys()]) if (re.test(k)) this.#store.delete(k);
  }
}
```
