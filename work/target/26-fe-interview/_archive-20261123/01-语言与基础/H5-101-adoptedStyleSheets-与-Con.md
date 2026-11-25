---
title: [H5-101] adoptedStyleSheets 与 Constructable Stylesheet 如何避免样式重复解析？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-101：adoptedStyleSheets 与 Constructable Stylesheet 如何避免样式重复解析？
**答**：
- `new CSSStyleSheet()` 构造样式表，`replaceSync(css)` 填充，再挂到 `shadowRoot.adoptedStyleSheets = [...old, sheet]`。
- 核心价值：**一份 CSSStyleSheet 实例可被任意多个 shadowRoot 共用**，浏览器只解析一次，相比每个组件的 `<style>` 标签解析 N 次成本大降。
- 运行时可换肤/主题切换：改同一个 sheet 的 replace 内容，所有组件即时生效，无需逐组件改 DOM。
- 与 `<style>` 的区别：adoptedStyleSheets 是引用数组，可增删可排序（优先级按数组顺序），`<style>` 标签一旦插入是独立的。
- 兼容性：Chrome 73+、Safari 16.4+、Firefox 101+，现代浏览器已可用，老环境需回退 `<style>` 注入。

```javascript
// 1) 构造一次，全站组件共用
const baseSheet = new CSSStyleSheet();
baseSheet.replaceSync(`
  :host { display: block; box-sizing: border-box; }
  .title { font-weight: 600; margin: 0 0 8px; }
`);

const btnSheet = new CSSStyleSheet();
btnSheet.replaceSync(`
  button { border: 1px solid #ddd; border-radius: 4px; padding: 6px 14px; cursor: pointer; }
`);

function defineCard() {
  class MyCard extends HTMLElement {
    connectedCallback() {
      if (!this.shadowRoot) {
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `<h3 class="title"><slot name="t"></slot></h3><slot></slot>`;
        // 2) 数组挂载：引用共享，顺序即优先级
        this.shadowRoot.adoptedStyleSheets = [baseSheet, btnSheet];
      }
    }
  }
  if (!customElements.get('my-card')) customElements.define('my-card', MyCard);
}
defineCard();

// 3) 主题热切换：只 replace 一份 sheet，所有卡片同步变化
function setTheme(dark) {
  baseSheet.replaceSync(`
    :host { display: block; color: ${dark ? '#eee' : '#222'};
            background: ${dark ? '#222' : '#fff'}; }
    .title { font-weight: 600; margin: 0 0 8px; }
  `);
}

// 4) 兼容回退：不支持时退回 style 标签注入
function ensureStyles(root, css) {
  if ('adoptedStyleSheets' in Document.prototype) return false;
  const s = document.createElement('style');
  s.textContent = css;
  root.prepend(s);
  return true;
}
```
