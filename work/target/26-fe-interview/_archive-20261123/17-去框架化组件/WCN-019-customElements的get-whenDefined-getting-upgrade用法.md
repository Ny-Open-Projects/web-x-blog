---
title: [WCN-019] customElements.get / whenDefined / upgrade 有什么区别？如何用于懒加载与预升级？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-019：customElements.get / whenDefined / upgrade 有什么区别？如何用于懒加载与预升级？

**答**：
- `customElements.get(tag)`：返回已注册的类或 undefined，用于"是否已定义"的同步判断。
- `customElements.whenDefined(tag)`：返回 Promise，在该 tag define 时 resolve，已定义则立即 resolve；适合"等组件可用后再操作"。
- `customElements.upgrade(node)`：手动把一个未升级元素立刻升级为注册类实例——用于在 define 之前手动创建并填充的元素，避免等解析时机。
- 懒加载模式：`customElements.whenDefined` + 动态 import 实现按需 define；或先用占位 light DOM（内置 skeleton），define 后 upgrade 替换。
- 预升级应用：SSR/静态 HTML 场景里 JS 加载慢，可以先渲染 light DOM 内容，define 完成后内容自动被 slot 投影，无需闪烁。

```javascript
// 1) whenDefined 等待 + 动态 import
customElements.whenDefined('analytics-chart').then(() => {
  document.querySelector('analytics-chart')?.load('weekly');
});

// 2) 手动创建 + 提前 upgrade
function createSync(tag) {
  const el = document.createElement(tag);
  el.textContent = 'loading...';
  document.body.append(el);
  customElements.upgrade(el); // 若已 define 则立刻升级，否则保持 unknown element
  return el;
}

// 3) 懒 define（skeleton 先行）
if (!customElements.get('heavy-table')) {
  import('./heavy-table.js').then(({ HeavyTable }) => {
    customElements.define('heavy-table', HeavyTable);
    // define 后文档内所有 <heavy-table> 自动升级，skeleton 内容被投影/替换
  });
}
```
