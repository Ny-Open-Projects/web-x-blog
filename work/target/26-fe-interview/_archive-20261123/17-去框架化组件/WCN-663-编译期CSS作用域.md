---
title: [WCN-663] 编译期 scoped CSS（组件样式隔离）的实现原理是什么？与 Shadow DOM 有何不同？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-663：编译期 scoped CSS（组件样式隔离）的实现原理是什么？与 Shadow DOM 有何不同？

**答**：
- 结论：编译时给组件模板元素加唯一属性（如 data-v-abc），并把 CSS 选择器改写为 .cls[data-v-abc]；是「约定式隔离」而非浏览器原生隔离。
- 区别：Shadow DOM 是真隔离（样式不进出）；scoped CSS 靠选择器加属性，全局样式仍可渗透，需 :deep() 穿透子组件。
- 追问钩子：为什么 WC 项目仍可能需要 scoped CSS？因为 light DOM 模式或为了与旧样式体系共存——考察对「隔离方案组合」的理解。

```javascript
function scopeCss(css, scopeId) {
  return css.replace(/\.([\w-]+)/g, (m, cls) => `.${cls}[data-v-${scopeId}]`);
}
function scopeTemplate(html, scopeId) {
  return html.replace(/<(\w+)([^>]*)>/g,
    (m, tag, attrs) => `<${tag}${attrs} data-v-${scopeId}>`);
}
const id = 'abc123';
console.log(scopeCss('.btn { color: red }', id));
// .btn[data-v-abc123] { color: red }
console.log(scopeTemplate('<button class="btn">x</button>', id));
// <button class="btn" data-v-abc123>x</button>
```
