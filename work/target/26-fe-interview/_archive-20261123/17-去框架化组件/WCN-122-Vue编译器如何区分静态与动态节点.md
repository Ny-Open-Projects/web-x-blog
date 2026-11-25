---
title: [WCN-122] Vue 编译器如何区分静态与动态节点？patchFlag/block 树机制是什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-122：Vue 编译器如何区分静态与动态节点？patchFlag/block 树机制是什么？

**答**：
- 静态提升：纯静态的节点/属性被 hoist 到 render 外只创建一次；超长静态内容（>20 节点）内联缓存。
- patchFlag：每个动态 vnode 带位标记（TEXT=1、CLASS=2、PROPS=8、FULL_PROPS 等），diff 时只检查 flag 声明的更新类型与动态属性列表，跳过静态内容。
- block 树：渲染函数把"结构可能变化的节点"（v-if/v-for）收集为 dynamicChildren 平铺数组——diff 直接遍历该数组跳过整棵静态子树，把 O(树大小) 变为 O(动态节点数)。
- v-pre/v-memo：显式跳过编译/缓存子树（依赖数组不变时整树跳过）。
- 与 WCN 的关联：Vapor 模式更进一步——动态点直接编译为 DOM effect，连 vnode 都不再创建。

```jsx
// 模板 → 编译产物（示意）
// <div><span class="t">静态</span><span :class="cls">{{ msg }}</span></div>
const _hoisted_1 = createElementVNode("span", { class: "t" }, "静态"); // 静态提升

export function render(_ctx) {
  return (openBlock(), createElementBlock("div", null, [
    _hoisted_1,
    createElementVNode("span", {
      class: normalizeClass(_ctx.cls)         // 动态
    }, toDisplayString(_ctx.msg), 3 /* TEXT | CLASS */)  // patchFlag
  ]));
}
// diff：flag=3 → 只比对 class 与 text，不遍历静态 span
```
