---
title: [WCN-024] 如何用 `<template>` + 克隆 + DocumentFragment 提升 WC 渲染性能？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-024：如何用 `<template>` + 克隆 + DocumentFragment 提升 WC 渲染性能？

**答**：
- `<template>` 内容惰性：不进布局树、图片不加载、脚本不执行，是"结构预声明"的最优载体；`content` 是 DocumentFragment。
- 首次渲染：`shadowRoot.append(tpl.content.cloneNode(true))` 一次成型，避免多段 `innerHTML +=` 反复解析。
- 列表渲染：先在内存 fragment 里拼好所有子项（或对行模板做 `cloneNode`），最后一次性 append，减少 N 次回流为 1 次。
- 深拷贝注意事项：`cloneNode(true)` 会复制 light DOM 内的 `<template>` 内容但不会执行其中脚本；带 `id` 的节点克隆后会重复，克隆后需重写引用。
- 性能对比：innerHTML 解析 1000 行 vs template 克隆——后者省去字符串解析，且模板可被编译器（如 Lit 的静态模板）进一步优化为只创建一次的"静态模板缓存"。

```javascript
class ProductList extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <template id="row"><li><img loading="lazy"><b class="t"></b><span class="p"></span></li></template>
      <ul id="list"></ul>`;
    // 模拟数据
    const data = Array.from({ length: 1000 }, (_, i) => ({ t: '商品' + i, p: i % 100 }));
    const rowTpl = root.getElementById('row');
    const frag = document.createDocumentFragment();
    for (const d of data) {
      const row = rowTpl.content.cloneNode(true); // 克隆而非 innerHTML 拼接
      row.querySelector('.t').textContent = d.t;
      row.querySelector('.p').textContent = '¥' + d.p;
      frag.append(row);
    }
    root.getElementById('list').append(frag); // 一次回流
  }
}
customElements.define('product-list', ProductList);
```
