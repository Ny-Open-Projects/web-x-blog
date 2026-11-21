---
title: [WCN-010] Shadow DOM 的事件重定向（retargeting）是怎么工作的？composed 属性起什么作用？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-010：Shadow DOM 的事件重定向（retargeting）是怎么工作的？composed 属性起什么作用？

**答**：
- retargeting：事件从影子树内部冒泡穿越边界时，外层监听者看到的 `event.target` 被替换为宿主元素，防止内部结构泄露。
- composed 标志决定事件能否穿越边界：`click`、`input`、`focusin` 等内置 UI 事件 composed 为 true；`focus`、`blur`、`resize`、`scroll`、`mouseover` 部分不 composed，只能在影子树内监听（focus 用 focusin 代替）。
- `event.composedPath()` 返回真实传播路径，但在 closed shadow 外调用会被裁剪，只包含宿主以上的节点。
- 自定义事件必须显式 `{ bubbles: true, composed: true }` 才能冒出影子树，否则宿主外永远收不到。
- 追问钩子：`event.relatedTarget` 在跨越边界时同样被 retarget（可能变为 null）。

```javascript
class Combobox extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = '<button id="btn">选择</button><ul id="list" hidden></ul>';
    root.getElementById('btn').addEventListener('click', () => {
      // 自定义事件跨边界必须 bubbles + composed
      this.dispatchEvent(new CustomEvent('combo-open', { bubbles: true, composed: true }));
    });
    // mouseover 不 composed：只在影子树内监听
    root.addEventListener('mouseover', () => root.style.cursor = 'pointer');
  }
}
customElements.define('x-combobox', Combobox);

document.querySelector('x-combobox').addEventListener('combo-open', (e) => {
  console.log(e.target.tagName);            // X-COMBOBOX（retargeted）
  console.log(e.composedPath()[0].id);      // btn（真实源头）
});
```
