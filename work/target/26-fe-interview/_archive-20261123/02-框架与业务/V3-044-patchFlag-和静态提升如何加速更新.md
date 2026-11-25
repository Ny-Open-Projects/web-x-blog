---
title: [V3-044] patchFlag 和静态提升如何加速更新？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-044：patchFlag 和静态提升如何加速更新？
**答**：
- 静态提升：纯静态 vnode 只创建一次，被提升到 render 函数外，diff 时直接跳过。
- patchFlag：编译器给动态节点打标（1 文本、2 class、8 props 等），diff 只比对标记的部分。
- block tree：动态节点被收集进 block 的扁平数组，更新时不再递归遍历整棵树。
- 这些是"编译时优化"，让 Vue3 的更新性能接近手动优化代码。

```javascript
// 编译器输出对比（简化）
// 模板：<div><p>静态文本</p><span>{{ dynamic }}</span></div>

// 1 静态提升：静态 vnode 只创建一次，提到 render 函数外
const hoisted = createElementVNode("p", null, "静态文本", -1 /* HOISTED */);

function render(_ctx) {
  return (openBlock(), createElementBlock("div", null, [
    hoisted, // 静态节点，diff 直接跳过
    // 2 patchFlag：1 表示只有文本是动态的
    createElementVNode("span", null, toDisplayString(_ctx.dynamic), 1 /* TEXT */),
  ]));
}
// openBlock 开启 block 收集：动态节点进入扁平数组
// 更新时沿 block tree 只遍历动态节点，不再递归整棵树
```

## 第十一章 异步组件
