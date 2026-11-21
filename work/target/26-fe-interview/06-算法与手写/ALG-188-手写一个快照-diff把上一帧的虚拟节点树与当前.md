---
title: [ALG-188] 手写一个快照 diff：把上一帧的虚拟节点树与当前帧对比，产出最小变更操作（更新 props、改文本、替换、删除），这是虚拟 DOM 的核心思想。如何实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-188：手写一个快照 diff：把上一帧的虚拟节点树与当前帧对比，产出最小变更操作（更新 props、改文本、替换、删除），这是虚拟 DOM 的核心思想。如何实现？
**答**：递归同层对比（深度优先，index 路径定位节点）：① 新节点不存在 => REMOVE；② 类型不同（tag 或文本）=> REPLACE 整树；③ 同类型 => 先 diff props（增/删/改），再对 children 逐位递归——真实框架在此基础上加 key 复用与最长递增子序列优化移动，简化版按位对齐即可。产出 patch 列表由 patch 函数消费。O(节点数)。

```javascript
function diff(oldV, newV, index = [], patches = []) {
  if (oldV === newV) return patches;                        // 同引用直接跳过
  if (!newV) {
    patches.push({ type: 'REMOVE', index });
  } else if (!oldV || oldV.type !== newV.type) {
    patches.push({ type: 'REPLACE', index, node: newV });   // 类型不同：整树替换
  } else if (typeof newV === 'string' || typeof newV === 'number') {
    if (oldV !== newV) patches.push({ type: 'TEXT', index, text: newV });
  } else {
    // 同类型：diff props
    const ops = [];
    for (const k of Object.keys(newV.props))
      if (newV.props[k] !== oldV.props[k]) ops.push([k, newV.props[k]]);
    for (const k of Object.keys(oldV.props))
      if (!(k in newV.props)) ops.push([k, undefined]);
    if (ops.length) patches.push({ type: 'PROPS', index, ops });
    // children 逐位递归
    const len = Math.max(oldV.children.length, newV.children.length);
    for (let i = 0; i < len; i++) {
      diff(oldV.children[i], newV.children[i], [...index, i], patches);
    }
  }
  return patches;
}
// 生产级还需 key 复用（children 重排）与 LIS 优化移动，原理一致
```
