---
title: [WCN-043] WC 组件如何做懒加载与代码分割？define 前的占位策略有哪些？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-043：WC 组件如何做懒加载与代码分割？define 前的占位策略有哪些？

**答**：
- 天然分割点：每个 custom element 一个 JS 模块，用动态 `import()` 按需 define；入口页只加载首屏组件，其余等出现在视口（IntersectionObserver 驱动 import）。
- 声明式懒加载：`<my-chart lazy>` —— 组件本体是极小的"加载器元素"，先渲染骨架，visible 后 import 真实实现并替换（真实实现可用不同 tag 或同一 tag 内升级）。
- `:not(:defined)` 占位：unknown 阶段由全局 CSS 提供骨架样式；define 后 `:defined` 自动接管。
- 预加载权衡：对高概率交互组件用 `import()` 触发后在 link rel=modulepreload 提示或 `requestIdleCallback` 预热，避免点击后白屏。
- 多入口产物配合：构建出 `chunk-xxx.js`，加载器元素持有映射表（tag → import 函数），失败要有重试与降级提示。

```javascript
// 加载器元素：可见时才拉真实实现
class LazyBlock extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = '<div class="sk" style="min-height:120px">加载中…</div>';
    this.#io = new IntersectionObserver((ents) => {
      if (!ents.some((e) => e.isIntersecting)) return;
      this.#io.disconnect();
      const impl = this.getAttribute('impl') ?? this.tagName.toLowerCase();
      import(`./components/${impl}.js`)          // 按 tag 动态分包
        .then(() => this.#done())
        .catch(() => { this.shadowRoot.textContent = '组件加载失败'; });
    }, { rootMargin: '300px' });
    this.#io.observe(this);
  }
  #done() { this.dispatchEvent(new CustomEvent('lazy-ready', { bubbles: true, composed: true })); }
  disconnectedCallback() { this.#io?.disconnect(); }
  #io;
}
customElements.define('lazy-block', LazyBlock);
```
