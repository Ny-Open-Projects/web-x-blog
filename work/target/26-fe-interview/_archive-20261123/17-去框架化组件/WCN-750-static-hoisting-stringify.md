---
title: [WCN-750] 前端编译响应式里「静态提升 + 预字符串化」为什么能大幅减少运行时开销？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-750：前端编译响应式里「静态提升 + 预字符串化」为什么能大幅减少运行时开销？

**答**：
- 结论：模板中不变的节点/属性在编译期提取为常量（hoist），避免每次渲染重建；整段纯静态子树可预序列化为 HTML 字符串，运行时直接 `innerHTML` 一次性插入。
- 原理：把「创建元素 + 设属性 + 建层级」的 O(n) DOM 操作前移到编译期，运行时只处理动态绑定；配合 patchFlag 跳过静态子树 diff。
- 追问钩子：预字符串化对带 event handler 的节点适用吗？考察「动态部分必须留在运行时」的边界判断。

```javascript
// 编译前模板：<div class="hd"><span>静态标题</span></div>
// 编译后：
const HOISTED = '<div class="hd"><span>静态标题</span></div>'; // 预字符串化
function render(dynamicText) {
  const host = document.createElement('section');
  host.innerHTML = HOISTED;                      // 静态部分一次性插入
  const dyn = document.createElement('p');
  dyn.textContent = dynamicText;                 // 仅动态部分运行时创建
  host.appendChild(dyn);
  return host;
}
console.log(render('动态内容').innerHTML);
```
