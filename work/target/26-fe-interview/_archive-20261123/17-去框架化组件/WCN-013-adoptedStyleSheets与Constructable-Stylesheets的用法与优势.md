---
title: [WCN-013] adoptedStyleSheets 与 Constructable Stylesheets 怎么用？相比注入 <style> 有什么优势？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-013：adoptedStyleSheets 与 Constructable Stylesheets 怎么用？相比注入 style 标签有什么优势？

**答**：
- 构造式样式表：`new CSSStyleSheet()` 创建可编程样式表，`replaceSync(cssText)` / `replace(cssText)`（异步，可用 @import）更新内容。
- 挂载：`document.adoptedStyleSheets.push(sheet)` 作用于整个文档；`shadowRoot.adoptedStyleSheets = [sheet, theme]` 作用于影子树，同一 sheet 可被多个影子根共享且只解析一次。
- 优势一：性能——无 DOM 解析开销，主题切换只 replace 文本，不重建节点；优势二：共享——组件库上千实例共享一份 sheet，省内存。
- 动态主题实现：保存 `CSSStyleSheet` 引用，运行时 `replaceSync(':root{--primary:red}')` 即时生效，且不触发整树重排之外的开销。
- 注意：adoptedStyleSheets 是数组引用语义，直接 push 到 shadowRoot 的数组需要先取引用再 push（部分实现返回的是新数组）；顺序决定优先级，越靠后优先级越高。

```javascript
// 组件库共享样式表：解析一次，所有实例复用
const base = new CSSStyleSheet();
base.replaceSync(`
  :host { display: inline-flex; }
  .chip { padding: 4px 10px; border-radius: 999px; }
`);

const theme = new CSSStyleSheet(); // 主题层可热替换
class StatusChip extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = '<span class="chip"><slot></slot></span>';
    // 两个 sheet，theme 在后优先级更高
    root.adoptedStyleSheets = [base, theme];
  }
}
customElements.define('status-chip', StatusChip);

// 运行时换主题：不重建任何 DOM
theme.replaceSync('.chip { background: var(--primary, #2563eb); color: #fff; }');
```
