---
title: [WCN-768] 编译时如何计算并注入「最少必要更新」来优化 keyed diff？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-768：编译时如何计算并注入「最少必要更新」来优化 keyed diff？

**答**：
- 结论：编译器为每个动态节点打 patchFlag（如 TEXT/CLASS/PROPS），运行时 diff 只检查被标记的动态部分，跳过静态属性与结构；keyed 列表在编译期确定 key 来源，运行时只做移动/增删。
- 对 v-if 块生成稳定 block 树（收集动态子节点到扁平数组），更新时只遍历动态数组而非整棵树，复杂度从 O(树大小) 降为 O(动态节点数)。
- 追问钩子：动态节点数量很多时 block 数组退化怎么办？考察「嵌套 block 分层」优化。

```javascript
const TEXT = 1, CLASS = 2, PROPS = 4;
function patchElement(oldVNode, newVNode) {
  const flag = newVNode.patchFlag;
  if (flag & TEXT) oldVNode.el.textContent = newVNode.children[0];
  if (flag & CLASS) oldVNode.el.className = newVNode.props.class;
  if (flag & PROPS) updateProps(oldVNode.el, newVNode.props);
  // 未标记的部分一律跳过 —— 这就是「最少必要更新」
}
function updateProps(el, props) { /* 仅更新变化的 props */ }
const vnode = { el: document.createElement('div'), patchFlag: TEXT | CLASS,
  children: ['新文本'], props: { class: 'active' } };
patchElement(vnode, { ...vnode, children: ['更新'], props: { class: 'done' } });
console.log(vnode.el.textContent, vnode.el.className);
```
