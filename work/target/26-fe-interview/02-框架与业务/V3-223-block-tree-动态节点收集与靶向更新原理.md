---
title: [V3-223] block tree（动态节点收集）与靶向更新是怎么配合工作的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-223：block tree（动态节点收集）与靶向更新是怎么配合工作的？
**答**：
- 创建阶段：block（根 block = 组件渲染，结构 block = v-if/v-for）在渲染函数执行时**收集**所有带 patchFlag 的后代动态 vnode，存入 `dynamicChildren` 数组。
- 结构化：v-if/v-for 会开启新 block，因此每个 block 的动态节点都是"扁平结构稳定"的集合，无跨层级不确定性。
- 更新阶段：组件更新不再递归遍历整棵树，直接遍历 `dynamicChildren` 按索引配对 patch——旧新树的动态节点结构一致（结构变化会生成新 block）。
- 复杂度：更新成本 = O(动态节点数)，与静态内容、总节点数无关；这是 Vue3 模板更新比手写 vdom 快的根本原因。
- 边界：v-html/dynamic component 等运行时不确定内容会退化为普通遍历（标记 NEED_PATCH）。

```javascript
// <div><p>{{a}}</p><span>b</span><b>{{c}}</b></div>
function render(_ctx) {
  return (openBlock(), createElementBlock("div", null, [
    createElementVNode("p", null, toDisplayString(_ctx.a), 1 /* TEXT */), // 收集
    createElementVNode("span", null, "b"),                                // 静态，不收集
    createElementVNode("b", null, toDisplayString(_ctx.c), 1 /* TEXT */), // 收集
  ]));
}
// 更新：componentUpdateFn 中
if (instance.dynamicChildren) {
  patchBlockChildren(instance.dynamicChildren); // O(2) 而非遍历所有子节点
}
```
