---
title: [HW-109] 手写请求取消管理器——按 key 取消在途请求、页面卸载全量取消、复用 signal
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：fetch 一旦发出无法"暂停"，取消靠 AbortController。管理器：按业务 key（如 'search'）注册 controller，同 key 新请求自动取消旧请求（竞态治理）；AbortSignal.any 组合多个信号（页面卸载 + 业务取消都触发）；卸载前全量取消防止僵尸请求。

```javascript
class AbortManager {
  constructor() {
    this.controllers = new Map();                     // key -> {ctrl, children: Set}
    addEventListener('pagehide', () => this.abortAll());   // 卸载全量取消
  }
  async fetch(key, url, { extraSignal, ...opts } = {}) {
    this.abort(key);                                  // 同 key 新请求取消旧请求（竞态）
    const ctrl = new AbortController();
    const signals = extraSignal ? [ctrl.signal, extraSignal] : [ctrl.signal];
    const signal = AbortSignal.any ? AbortSignal.any(signals) : this.#combine(signals);
    const entry = { ctrl, children: new Set() };
    this.controllers.set(key, entry);
    try {
      return await fetch(url, { ...opts, signal });
    } catch (e) {
      if (e.name === 'AbortError') e.cancelledBy = extraSignal?.aborted ? 'extra' : 'manager';
      throw e;
    } finally {
      if (this.controllers.get(key) === entry) this.controllers.delete(key);
    }
  }
  abort(key) { const e = this.controllers.get(key); if (e) { e.ctrl.abort(); this.controllers.delete(key); } }
  abortAll() { for (const [, e] of this.controllers) e.ctrl.abort(); this.controllers.clear(); }
  #combine(signals) {                                  // AbortSignal.any 的 polyfill
    const ctrl = new AbortController();
    const onAbort = (e) => ctrl.abort(e.target.reason);
    for (const s of signals) { s.addEventListener('abort', onAbort, { once: true }); }
    return ctrl.signal;
  }
}
// 用法：搜索竞态
const am = new AbortManager();
input.oninput = (e) => am.fetch('search', `/api/s?q=${e.target.value}`)
  .then(render).catch((err) => { if (err.cancelledBy !== 'extra') showErr(err); });
// 组件卸载：am.abort('search') 或卸载回调里 abortAll
```

**评分点**：
- 同 key 自动取消旧请求（竞态治理的核心封装）。
- AbortSignal.any 多信号组合（卸载+业务取消），并给出 polyfill。
- AbortError 区分"谁取消的"（cancelledBy），便于上层决定是否静默。
- pagehide 全量取消防僵尸请求；finally 清理 Map。
