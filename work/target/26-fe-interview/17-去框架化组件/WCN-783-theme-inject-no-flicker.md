---
title: [WCN-783] 白标场景下主题的运行时注入如何避免样式污染与闪烁？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-783：白标场景下主题的运行时注入如何避免样式污染与闪烁？

**答**：
- 结论：主题以 CSS 自定义属性注入到 `:root` 或组件的 `:host`，用 `adoptedStyleSheets` 复用同一份样式表；先注入主题再挂载组件，避免 FOUC（先渲染默认色后跳变）。
- 多租户白标用作用域选择器（如 `[data-tenant]`）隔离，避免全局 `:root` 被覆盖；切换主题时批量更新 CSS 变量（一次 style 写入）。
- 追问钩子：首屏主题从服务端下发，怎么保证 hydration 前后不闪？考察「内联脚本提前设置 data 属性 + 临界 CSS」。

```javascript
// 提前注入主题，避免闪烁
const theme = { '--brand': '#06f', '--bg': '#fff' };
const root = document.documentElement;
for (const [k, v] of Object.entries(theme)) root.style.setProperty(k, v);
root.setAttribute('data-brand', 'acme');           // 作用域标记
// 组件只消费变量，不写死颜色
class DsButton extends HTMLElement {
  connectedCallback() {
    const s = new CSSStyleSheet();
    s.replaceSync(':host { background: var(--brand, #888); color: #fff }');
    this.attachShadow({ mode: 'open' }).adoptedStyleSheets = [s];
  }
}
console.log('主题先注入，组件后挂载：无闪烁');
```
