---
title: [V3-230] 手写：v-memo 的跳过 diff 机制（缓存比较 + patch 跳过）
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-230：手写：v-memo 的跳过 diff 机制（缓存比较 + patch 跳过）
**需求**：实现 `withMemo(memo, render, parent, anchor)`：memo 数组各项与上次缓存逐项相等（===）时完全跳过重渲染并复用上次 DOM；否则执行 render 并记录本次依赖值。用于大列表行渲染跳过。
**评分点**：
- 缓存结构：`cache[i] = [deps..., vnode]` 的槽位设计
- 依赖比较用 === 且短路
- 命中时能正确返回已渲染 DOM（不重复 insert）
- 说明适用边界：行内依赖不变的列表场景才有收益，频繁变化的行反而多一次比较开销

```javascript
// v-memo="[item.id, item.checked]" 编译产物核心逻辑
export function withMemo(memo, render, parent, anchor) {
  const slot = parent.cache[parent.renderCacheIndex]; // 本组件的缓存数组槽
  // 逐项比较依赖
  const hit = slot && memo.every((dep, i) => isSameVNodeTypeValue(dep, slot[i]));
  parent.renderCacheIndex++;
  if (hit) return slot[memo.length]; // 返回缓存的 vnode，跳过 render
  const vnode = render();            // 未命中：重渲染
  const newSlot = [...memo];         // 记录本轮依赖快照
  newSlot[vnode ? vnode.cacheIndex ?? memo.length : memo.length] = vnode;
  parent.cache[cacheIndexOf(parent, slot)] = newSlot;
  mount(vnode, parent, anchor);
  return vnode;
}
function isSameVNodeTypeValue(a, b) { return a === b; } // 引用相等即跳过
// 父组件更新时：renderCacheIndex 归零 + 遍历 dynamicChildren 前先过 withMemo
// 行级收益：1000 行列表只重渲染依赖变化的行，其余行 diff 整段跳过
```
