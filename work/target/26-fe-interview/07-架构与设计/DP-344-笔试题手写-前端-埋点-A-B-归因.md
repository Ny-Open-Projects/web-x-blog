---
title: [DP-344] 笔试题：手写埋点归因（曝光→点击→转化链）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-344：笔试题：手写埋点归因（曝光→点击→转化链）？
**题目**：实现 FunnelTracker：1) 曝光（元素进视口 50% 持续 1s 计有效曝光）；2) 点击归因到最近曝光事件（会话内关联）；3) 转化事件携带漏斗链（exp→view→click→convert）；4) 防重复曝光（同一元素会话内一次）。
**评分点**：
- 有效曝光条件（时长 + 比例）。
- 归因链传递（上下文携带 expId/viewId）。
- 防重复（Set 记录）。
- 链式事件顺序可验证。
```javascript
class FunnelTracker {
  #seen = new Set();           // 4) 防重复
  #last = {};                  // 2) 归因上下文
  constructor(private track) {}
  expose(el, { slot, exp }) {
    if (this.#seen.has(slot)) return;
    let timer;
    const io = new IntersectionObserver(([e]) => {
      if (e.isIntersecting && e.intersectionRatio >= 0.5) {    // 1) 比例条件
        timer = setTimeout(() => {
          this.#seen.add(slot);
          this.#last[slot] = { exp, viewId: crypto.randomUUID() };
          this.track('expose', { slot, exp, viewId: this.#last[slot].viewId });
        }, 1000);                                              // 1) 时长条件
      } else clearTimeout(timer);
    }, { threshold: 0.5 });
    io.observe(el);
    el.addEventListener('click', () => this.#click(slot));     // 2) 点击归因
  }
  #click(slot) {
    const ctx = this.#last[slot] ?? {};
    this.track('click', { slot, ...ctx, clickId: crypto.randomUUID() });
    this.#last[slot].clickId = this.#last[slot].clickId ?? '';
  }
  convert(orderId, slot) {                                     // 3) 转化链
    const ctx = this.#last[slot] ?? {};
    this.track('convert', { orderId, slot, ...ctx });
  }
}
```
