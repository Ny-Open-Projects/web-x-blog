---
title: [FRP-010] 什么是虚拟 DOM？h 函数返回什么结构？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-010：什么是虚拟 DOM？h 函数返回什么结构？

**答**：
- 虚拟 DOM 是用 JS 对象描述真实 DOM 的树结构：`{ type, props, children, key }`，渲染 = 数据变化后"新旧 vnode 对比，最小化操作真实 DOM"。
- `h`（createVNode）只是 vnode 的**工厂函数**，负责规范化参数（class/style 合并、children 归一化、key 提取），不触碰真实 DOM。
- 价值：声明式 UI（数据驱动而非手动操作）、跨平台（vnode 可渲染到 DOM/Canvas/SSR 字符串）、为 diff 提供可比较的快照。
- 代价：多一层对象创建与 diff 的 JS 开销，这是 Vue3 编译优化和 Svelte 的优化动机。

```javascript
// 简化实现，帮助理解 h 函数与 vnode 结构
function h(type, props = null, children = null) {
  let shapeFlag = 0;
  if (typeof type === 'string') shapeFlag = 1;              // ELEMENT
  else if (typeof type === 'object') shapeFlag = 4;         // STATEFUL_COMPONENT

  if (typeof children === 'string') shapeFlag |= 8;         // TEXT_CHILDREN
  else if (Array.isArray(children)) shapeFlag |= 16;        // ARRAY_CHILDREN

  return {
    type,                                                    // 'div' | 组件对象 | 'svg'
    props,                                                   // { class, style, onClick, ... }
    children,
    key: props?.key ?? null,                                 // diff 用的身份标识
    el: null,                                                // 挂载后回填的真实 DOM 引用
    shapeFlag,                                               // 位标记：加速后续分支判断
  };
}

// h 的三种典型用法
const vnode1 = h('div', { class: 'box', onClick: () => {} }, 'hello text');
const vnode2 = h('ul', null, [
  h('li', { key: 1 }, 'one'),
  h('li', { key: 2 }, 'two'),
]);
const vnode3 = h(MyComponent, { title: 'hi' });

console.log(vnode1.shapeFlag); // 1 | 8 = 9：元素 + 文本子节点
console.log(vnode2.shapeFlag); // 1 | 16 = 17：元素 + 数组子节点
```
