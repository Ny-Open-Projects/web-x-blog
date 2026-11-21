---
title: [WCN-059] WC 在生产环境的性能调优有哪些手段？从加载、渲染、更新三个阶段展开
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-059：WC 在生产环境的性能调优有哪些手段？从加载、渲染、更新三个阶段展开

**答**：
- 加载阶段：按 tag 动态 import + IntersectionObserver 触发（WCN-044 的调度器）；modulepreload 高概率组件；组件 CSS 内联进影子树避免额外请求；版本化 URL + 长缓存。
- 渲染阶段：constructor 一次 attachShadow、模板克隆复用（template/静态模板缓存）；`contain: content`、`content-visibility: auto` 收敛重排；列表行用 DocumentFragment 批量插入。
- 更新阶段：细粒度更新（Signals/局部 DOM 引用直改）替代全量 innerHTML 重写；`attributeChangedCallback` 中合并高频变更（microtask 去抖）；离屏组件用 `elementInternals` 或标志位暂停 effect。
- 测量方法：Performance 面板看强制同步布局（紫色 Layout）；为 define 与首次渲染打 `performance.mark`；LCP 元素若是 WC 首屏内容，确认 DSD 已避免等待 JS。
- 典型反模式：connectedCallback 里同步 fetch 阻塞交互、每次 attribute 变化重建整个影子树、多实例重复注册样式表（未用 adoptedStyleSheets 共享）。

```javascript
// 更新阶段示例：高频 attribute 合并为微任务一次渲染
class StockTicker extends HTMLElement {
  static observedAttributes = ['price'];
  #scheduled = false;
  attributeChangedCallback() {
    if (this.#scheduled) return;
    this.#scheduled = true;
    queueMicrotask(() => {   // 同帧多次 setAttribute 只渲染一次
      this.#scheduled = false;
      this.#render();        // 直改文本节点，不重建影子树
    });
  }
  #render() {
    this.#priceNode ??= this.shadowRoot.querySelector('#p'); // 缓存节点引用
    this.#priceNode.textContent = this.getAttribute('price') ?? '';
  }
  #priceNode;
}
customElements.define('stock-ticker', StockTicker);
```
