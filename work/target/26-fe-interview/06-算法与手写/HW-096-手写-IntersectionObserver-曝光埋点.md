---
title: [HW-096] 手写曝光埋点（IntersectionObserver）——批量上报、去重、50% 阈值与离开即算
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：曝光定义：元素 50% 可见且持续（或进入即算，按业务）。实现：单例 IO 观察所有埋点元素，进入时记录时间戳与首次可见，离开/页面隐藏时结算曝光时长，批量上报 + 已曝光去重。用 Map 存待结算项，visibilitychange 时 flush。

```javascript
class ExposureTracker {
  constructor({ threshold = 0.5, report } = {}) {
    this.report = report; this.pending = new Map();   // el -> {start, key}
    this.done = new Set();                            // 已曝光去重
    this.io = new IntersectionObserver((entries) => {
      for (const e of entries) {
        const key = e.target.dataset.track;
        if (e.intersectionRatio >= threshold) {
          if (!this.pending.has(e.target)) this.pending.set(e.target, { key, start: performance.now() });
        } else this.#settle(e.target);
      }
    }, { threshold: [threshold] });
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') this.flush();   // 离开页面结算所有
    });
  }
  observe(el) { this.io.observe(el); }
  unobserve(el) { this.io.unobserve(el); this.#settle(el); }
  #settle(el) {
    const item = this.pending.get(el);
    if (!item) return;
    this.pending.delete(el);
    if (this.done.has(item.key)) return;
    this.done.add(item.key);
    this.report({ key: item.key, duration: Math.round(performance.now() - item.start) });
  }
  flush() { for (const el of [...this.pending.keys()]) this.#settle(el); }
}
// 用法：商品卡片埋点
const tracker = new ExposureTracker({ report: (d) => rumQueue.push({ metric: 'exposure', ...d }) });
document.querySelectorAll('[data-track]').forEach((el) => tracker.observe(el));
// 同一商品重复滚动进出：done 去重只算首次曝光（可按业务改成累计时长）
```

**评分点**：
- 单例 IO（不是每元素一个 observer），threshold 数组传入。
- 进入记录 start、离开/隐藏结算 duration 的完整生命周期。
- done 去重防重复上报；visibilitychange 兜底 flush。
- batch 上报走统一队列（不逐条 sendBeacon）。
