---
title: [WCN-188] 笔试：手写图片瀑布流布局 WC（列数自适应 + 最短列放置 + 视口懒加载）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-188：笔试：手写图片瀑布流布局 WC

**题目**：`<wc-masonry cols="auto">`：① 子项为 `<img data-h> `（已知宽高比）；② cols=auto 按 host 宽度自适应（≥1200:4 列 / ≥800:3 / ≥560:2 / 否则 1），ResizeObserver 驱动重排；③ 布局算法：每项放入当前最短列（按累积高度）；④ 绝对定位实现（transform），容器高度 = 最高列；⑤ 图片 IntersectionObserver 懒加载；⑥ 重排节流（rAF）。

**答**：

```javascript
class WcMasonry extends HTMLElement {
  static observedAttributes = ['cols'];
  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <style>:host{display:block;position:relative}
        ::slotted(*){position:absolute;transition:transform .2s}</style>
        <slot id="s"></slot>`;
      this.#slot = this.shadowRoot.getElementById('s');
      this.#ro = new ResizeObserver(() => this.#schedule());
      this.#ro.observe(this);
      this.#slot.addEventListener('slotchange', () => this.#schedule());
      // 懒加载
      this.#io = new IntersectionObserver((ents) => {
        for (const en of ents) {
          if (en.isIntersecting) {
            const img = en.target;
            img.src = img.dataset.src; img.loading = 'lazy';
            this.#io.unobserve(img);
          }
        }
      }, { rootMargin: '300px' });
    }
  }
  #slot; #ro; #io; #raf = 0;
  disconnectedCallback() { this.#ro.disconnect(); this.#io.disconnect(); cancelAnimationFrame(this.#raf); }
  #schedule() { if (!this.#raf) this.#raf = requestAnimationFrame(() => { this.#raf = 0; this.#layout(); }); }
  #layout() {
    const w = this.clientWidth;
    const auto = w >= 1200 ? 4 : w >= 800 ? 3 : w >= 560 ? 2 : 1;
    const cols = this.getAttribute('cols') === 'auto' ? auto : Number(this.getAttribute('cols')) || auto;
    const gap = 12, colW = (w - gap * (cols - 1)) / cols;
    const heights = new Array(cols).fill(0);
    const items = this.#slot.assignedElements().filter((el) => el.matches('img'));
    for (const img of items) {
      const i = heights.indexOf(Math.min(...heights));        // 最短列
      const h = colW * (Number(img.dataset.h) || 0.75);        // 按 data-h 高宽比
      const x = i * (colW + gap), y = heights[i];
      img.style.width = `${colW}px`;
      img.style.transform = `translate(${x}px, ${y}px)`;
      heights[i] += h + gap;
      this.#io.unobserve(img); this.#io.observe(img);
    }
    this.style.height = `${Math.max(...heights)}px`;          // 容器 = 最高列
  }
}
customElements.define('wc-masonry', WcMasonry);
```

**评分点**：
- 最短列放置算法（heights.indexOf(Math.min)）与容器高度取最高列。
- ResizeObserver + rAF 节流 + slotchange 兜底（子项后到）。
- 绝对定位 + transform 重排（不回流）；宽高比 data-h 防 CLS。
- IO 懒加载与 disconnected 清理。
