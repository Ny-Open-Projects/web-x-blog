---
title: [WCN-965] 首屏 LCP 优化：WC 样式内联（DSD）与关键 CSS 提取的矛盾怎么平衡
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-965：首屏 LCP 优化：WC 样式内联（DSD）与关键 CSS 提取的矛盾怎么平衡

**答**：
- 结论先行：DSD 把样式内联进每个组件，天然利好人像独立渲染，但重复样式增大 HTML、阻塞解析；关键 CSS 提取把首屏样式内联 head 加速 LCP，两者要「共享样式外提、私有样式内联」。
- 做法：把组件公共 token/基础样式提取成一份外部 CSS（<link> preload），只在 DSD 里内联「该组件特有、首屏必需」的少量规则，避免每个组件重复一大段。
- 构造式样式表（adoptedStyleSheets）让多个 shadow root 共享同一 CSSStyleSheet 对象，减少重复解析与内存。
- 测量：LCP 受「最大元素渲染时间」影响，优先保证首屏最大 WC（如商品主图卡）的样式同步可用；非首屏组件延迟 define 与样式加载。
- 追问钩子：面试官问「preload 太多 CSS 反而变慢怎么办」——答：只 preload 首屏关键样式，其余用 media=print 技巧异步加载，避免与关键渲染路径争抢带宽。

```javascript
// 共享样式表：多个 shadow root 复用同一 CSSStyleSheet
const sharedSheet = new CSSStyleSheet();
sharedSheet.replaceSync(':host{display:block} button{background:var(--ds-primary)}');
class DsCard extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.adoptedStyleSheets = [sharedSheet]; // 共享，不重复内联
    root.innerHTML = '<slot></slot>';
  }
}
customElements.define('ds-card', DsCard);
// 首屏关键 CSS 外提 preload：<link rel=preload as=style href=critical.css>
```
