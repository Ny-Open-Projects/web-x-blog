---
title: [FRP-289] 笔试：手写迷你 block tree 渲染器
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-289：笔试：手写迷你 block tree 渲染器
**答**：实现 `renderBlock(buildFn)`：buildFn 内调 `trackDynamic(vnode)` 收集动态节点到 block；返回 { mount, update }——update 时只遍历收集到的动态 vnode 做 patch（不遍历静态树）；嵌套 block（v-if 边界）各自独立。

```javascript
let currentBlock = null
function renderBlock(buildFn) {
  const block = { dynamics: [], root: null, children: [] }
  const prev = currentBlock
  currentBlock = block
  block.root = buildFn()
  currentBlock = prev
  return {
    mount(container) { container.appendChild(block.root.el) },
    update(newRoot) {
      // 重新 build 收集新动态点，按序 patch
      const nextBlock = renderBlock(buildFn)
      block.dynamics.forEach((oldV, i) => patchVnode(oldV, nextBlock.dynamics[i] || oldV))
      block.dynamics = nextBlock.dynamics
    }
  }
}
function trackDynamic(vnode) {
  if (currentBlock && vnode.flag) currentBlock.dynamics.push(vnode)
  return vnode
}
```
**评分点**：
- render 期间收集动态点（openBlock 语义）。
- update 只遍历 dynamics（跳过静态）。
- 嵌套 block 用栈式 currentBlock 恢复。
- 结构变化时整块重建的语义说明。
