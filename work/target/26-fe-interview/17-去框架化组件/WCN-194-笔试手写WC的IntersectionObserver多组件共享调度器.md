---
title: [WCN-194] 笔试：手写多组件共享的 IntersectionObserver 调度器（单例复用 + 回调隔离）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-194：笔试：手写共享 IntersectionObserver 调度器

**题目**：长页面有 500 个组件各自 new IntersectionObserver——实现共享调度器 `SharedIO`：① 单例 observer（按 rootMargin 分桶，同配置共用）；② `observe(el, cb)` / `unobserve(el)`；③ 回调隔离：只调用自己的 cb；④ 页面隐藏（visibilitychange）暂停派发，恢复时补发变化；⑤ 元素移除 DOM 自动清理；⑥ 统计： observers created（应恒为分桶数）、tracked 数。

**答**：

```javascript
export class SharedIO {
  static #buckets = new Map();       // rootMargin -> SharedIO 实例
  static get(rootMargin = '0px') {
    if (!this.#buckets.has(rootMargin))
      this.#buckets.set(rootMargin, new SharedIO(rootMargin));
    return this.#buckets.get(rootMargin);
  }

  #obs; #cbs = new WeakMap(); #pending = [];
  #paused = false;
  constructor(rootMargin) {
    this.#obs = new IntersectionObserver((entries) => {
      if (this.#paused) { this.#pending.push(...entries); return; }  // 页面隐藏攒批
      for (const en of entries) {
        const cb = this.#cbs.get(en.target);
        if (cb) cb(en);                     // 回调隔离：只触发自己的
      }
    }, { rootMargin });
    document.addEventListener('visibilitychange', () => {
      this.#paused = document.hidden;
      if (!this.#paused && this.#pending.length) {
        const list = this.#pending; this.#pending = [];
        for (const en of list) this.#cbs.get(en.target)?.(en);
      }
    });
  }
  observe(el, cb) { this.#cbs.set(el, cb); this.#obs.observe(el); }
  unobserve(el) { this.#cbs.delete(el); this.#obs.unobserve(el); }
  get stats() { return { buckets: SharedIO.#buckets.size, tracked: this.#cbs.size ?? 'WeakMap' }; }
}
// 组件用法（500 个组件 → 只有几个 observer 实例）
// SharedIO.get('200px').observe(this, (en) => { if (en.isIntersecting) this.#load(); });
```

**评分点**：
- 按 rootMargin 分桶共享（同配置单例），observer 数从 N 降到桶数。
- WeakMap 存回调（元素销毁自动清理，无泄漏）。
- 回调隔离（entries 按 target 分发）。
- 页面隐藏暂停派发 + 恢复补发（电量/性能优化）。
