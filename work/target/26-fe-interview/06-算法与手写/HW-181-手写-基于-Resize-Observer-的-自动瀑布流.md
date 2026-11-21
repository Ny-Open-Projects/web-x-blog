---
title: [HW-181] 手写自动瀑布流——最短列优先放置 + 容器宽度自适应列数 + 渐进式渲染
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-181：手写自动瀑布流——最短列优先放置 + 容器宽度自适应列数 + 渐进式渲染

**答**：瀑布流布局引擎：① 列高数组 + 最短列优先（新项放入当前最矮列）；② 列数按容器宽度自适应（RO 监听容器，宽度变化分档）；③ 渐进渲染（rAF 分批挂载，帧预算）；④ 图片高度用预计算（服务端返回 w/h），布局 O(n) 无实测——避免"先渲染后修正"的双次重排。

```javascript
class Masonry {
  constructor(container, { gutter = 12, minColWidth = 240 } = {}) {
    Object.assign(this, { container, gutter, minColWidth });
    this.cols = []; this.items = [];
    new ResizeObserver(() => this.#relayout()).observe(container);
  }
  add(items) {                                            // items: { id, el, height }（height 预计算）
    this.items.push(...items);
    this.#place(items);
  }
  #colCount() {
    const w = this.container.clientWidth;
    return Math.max(1, Math.floor((w + this.gutter) / (this.minColWidth + this.gutter)));
  }
  #place(newItems) {
    const n = this.#colCount();
    const colW = (this.container.clientWidth - (n - 1) * this.gutter) / n;
    for (const it of newItems) {                          // 最短列优先：每项 O(列数)
      const c = this.cols.indexOf(Math.min(...this.cols));
      const x = c * (colW + this.gutter);
      const y = this.cols[c];
      it.el.style.cssText = `position:absolute;transform:translate(${x}px,${y}px);width:${colW}px`;
      this.cols[c] = y + it.height + this.gutter;
    }
    this.container.style.height = Math.max(...this.cols) + 'px';   // 容器高度 = 最高列收口
  }
  #relayout() {                                           // 列数变化才全量重排
    const n = this.#colCount();
    if (n !== this.cols.length) { this.cols = new Array(n).fill(0); this.#place(this.items); }
  }
}
// transform 定位（合成器友好，PER-347）
// 高度预计算（服务端给 w/h）—— 若用"渲染后实测修正"，每项两次布局且全列连锁重排（动态高度瀑布流的经典翻车点）
// 列数临界抖动：RO 回调可叠加滞回（HW-139 思路）防 ±1px 反复重排
```

**评分点**：
- 最短列优先放置（列高数组 + Math.min 索引）O(n×列数)。
- 高度预计算避免双次重排——本题核心（实测修正模式的连锁布局成本）。
- 列数自适应 + 仅列数变化才重排。
- transform 定位与容器高度收口。
