---
title: [WCN-978] 无障碍与 islands 的矛盾：静态岛交互怎么保证键盘可达（无 JS 时）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-978：无障碍与 islands 的矛盾：静态岛交互怎么保证键盘可达（无 JS 时）

**答**：
- 结论先行：islands 把 JS 降到最低，但「键盘可达」不依赖 JS——靠原生可聚焦元素（button/a/input）和正确的 tabindex 顺序，静态岛在 JS 加载前就应能被键盘操作。
- 原生优先：交互控件用 `<button>` `<a href>` 而非 `<div onclick>`；前者天然可 Tab、可回车/空格触发，后者无 JS 时完全不可达。
- 无 JS 的可达交互：用 `<details>/<summary>`、`<a href="#section">` 锚点跳转、表单提交走原生 action——这些零 JS 也能键盘操作。
- JS 增强时不破坏：hydration 只增强行为，不改变 DOM 顺序与可聚焦性；动态插入的内容要保证焦点顺序合理，必要时用 `aria-flowto` 或 tabindex=0。
- 追问钩子：面试官问「自定义元素何时可聚焦」——答：WC 默认不可聚焦，要显式加 tabindex 或 delegatesFocus，且 SSR 输出里就要带上，别等水合。

```javascript
// 静态岛：零 JS 也键盘可达
const staticIsland = `
<details><summary>筛选选项</summary>
  <a href="#result-1" class="filter">价格从低到高</a>
</details>
<button type="submit" form="filter-form">应用筛选</button>`;
// 全部是原生可聚焦元素：Tab 可达、Enter/Space 可触发，无需 JS。
// WC 形态需显式可聚焦：
class DsFilter extends HTMLElement {
  connectedCallback() { this.setAttribute('tabindex', '0'); } // SSR 阶段也可带上
}
customElements.define('ds-filter', DsFilter);
```
