---
title: [FRP-013] Vue3 的编译优化（patchFlag、静态提升、Block Tree）分别做了什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-013：Vue3 的编译优化（patchFlag、静态提升、Block Tree）分别做了什么？

**答**：
- **patchFlag**：编译期分析模板，给每个 vnode 打上"哪些属性是动态的"位标记（TEXT=1、CLASS=2、PROPS=8...），运行时只 diff 被标记的部分，跳过纯静态 props。
- **静态提升（hoistStatic）**：纯静态的 vnode 被提到 render 函数外只创建一次，之后每次渲染复用同一引用；连续静态节点超 20 个还会合并成一个 `createStaticVNode`（innerHTML 一次性插入）。
- **Block Tree**：render 时动态节点（含跨层级）被收集到 block 的 `dynamicChildren` 数组，更新时**跳过整棵树的 diff**，只遍历这个扁平数组精准更新——结构稳定时复杂度接近 O(动态节点数)。
- 效果是把"运行时全量 diff"变成"编译期定点打击"，这也是 Vue3 模板性能显著优于手写 render 函数的原因。

```javascript
// 一一对应：模板编译产物的关键片段（近似还原）
// 模板：<div><span>静态标题</span><p :class="cls">{{ msg }}</p></div>

// 1. 静态提升：纯静态 span 被提到 render 外，只创建一次
const _hoisted_1 = createElementVNode('span', null, '静态标题', -1 /* HOISTED */);

function render(_ctx) {
  return (openBlock(), createElementBlock('div', null, [
    _hoisted_1,                              // 复用提升的静态节点
    createElementVNode('p', { class: _ctx.cls }, toDisplayString(_ctx.msg), 9 /* TEXT, CLASS */),
    // 2. patchFlag = 9 = 1(TEXT) | 8(CLASS)：只 diff 文本和 class
    //    PROPS 类型的 flag 还会附带动态 props 名数组：["class"]
  ]));
}

// 3. Block Tree：openBlock/createElementBlock 开始收集动态后代节点
//    更新时不再走全量 diff，而是：
function patchBlock(block1, block2) {
  // 只对比 dynamicChildren 数组，静态节点完全跳过
  for (let i = 0; i < block2.dynamicChildren.length; i++) {
    patch(block1.dynamicChildren[i], block2.dynamicChildren[i]);
  }
}
```
