---
title: [FRP-061] patchFlag 的每个枚举位是什么含义？分别驱动 diff 里的哪种快速路径？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-061：patchFlag 的每个枚举位是什么含义？分别驱动 diff 里的哪种快速路径？

**答**：
- patchFlag 是**数字位标记**，告诉 runtime"这个 vnode 哪里可能变"，diff 时按位检查走快速路径，跳过全量比对。核心枚举：`1 TEXT`（动态文本内容）、`2 CLASS`、`4 STYLE`、`8 PROPS`（其他动态属性，配 dynamicProps 数组）、`16 FULL_PROPS`（含动态 key，需全 props 比对）、`32 HYDRATE_EVENTS`（仅 SSR）、`64 STABLE_FRAGMENT`（子节点顺序稳定的片段）、`128 KEYED_FRAGMENT`（带 key）、`256 UNKEYED_FRAGMENT`、`512 NEED_PATCH`（无具体 flag 但需 patch，如 ref）、`1024 DYNAMIC_SLOTS`、`4096 HOISTED`、`-1 BAIL`（退出优化，diff 全量走）。
- 对应 diff 行为举例：`TEXT` 只更新 `el.textContent`；`CLASS/STYLE` 只调 `patchClass/patchStyle`；`PROPS` 只遍历 `dynamicProps` 数组里的属性名；`FULL_PROPS` 与 `BAIL` 退回逐 key 全量比较。
- flag 可以**按位或叠加**（如 TEXT|CLASS=3），runtime 用 `&` 判断命中；命中任何 flag 都不会进入"逐子树全 diff"，这正是编译优化的提速来源。

```javascript
// 简化实现，帮助理解 patchFlag 枚举与 diff 快速路径
const PatchFlags = {
  TEXT: 1, CLASS: 2, STYLE: 4, PROPS: 8, FULL_PROPS: 16,
  NEED_PATCH: 512, DYNAMIC_SLOTS: 1024, BAIL: -1,
};

function patchElement(el, oldVNode, newVNode) {
  const flag = newVNode.patchFlag;
  if (flag === PatchFlags.BAIL) return fullDiff(el, oldVNode, newVNode); // 退出优化

  if (flag & PatchFlags.TEXT) {
    el.textContent = newVNode.children;            // 只更新文本，O(1)
  }
  if (flag & PatchFlags.CLASS) {
    el.className = newVNode.props.class;           // 只更新 class
  }
  if (flag & PatchFlags.STYLE) {
    el.style.cssText = newVNode.props.style;
  }
  if (flag & PatchFlags.PROPS) {
    // 只比对编译期记录的动态属性，静态属性完全不碰
    for (const key of newVNode.dynamicProps) {
      if (oldVNode.props[key] !== newVNode.props[key]) el.setAttribute(key, newVNode.props[key]);
    }
  }
  if (flag & PatchFlags.FULL_PROPS) {
    fullDiff(el, oldVNode, newVNode);              // 含动态 key，退回全量 props 比对
  }
  // 无任何 flag：直接 return，连 props 都不比
}

function fullDiff(el, o, n) { /* 全量遍历新旧 props 与 children */ }
function setFlag(vnode, ...flags) {
  vnode.patchFlag = flags.reduce((a, b) => a | b, 0); // 按位或叠加
  return vnode;
}

// 验证：TEXT|CLASS=3，一次标记覆盖两类快速路径
const vnode = setFlag({}, PatchFlags.TEXT, PatchFlags.CLASS);
console.log(vnode.patchFlag, !!(vnode.patchFlag & PatchFlags.TEXT)); // 3 true
```
