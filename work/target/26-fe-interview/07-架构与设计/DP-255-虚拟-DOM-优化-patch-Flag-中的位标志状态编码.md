---
title: [DP-255] 源码识别：PatchFlag 与 Lane 中的位标志编码？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-255：源码识别：PatchFlag 与 Lane 中的位标志编码？
**答**:
- 位标志（状态编码策略）：Vue3 PatchFlag（TEXT=1, CLASS=2, PROPS=4...）标记节点"哪部分动态"，patch 时只处理标记位——把"全量 diff"降为"按需 diff"。
- React Lane 同构：优先级用位图（每个 bit 一个 lane），合并/交集/移除都是位运算 O(1)。
- 享元色彩：编译期静态提升（hoisted 常量 vnode）跨渲染共享同一对象——位标志 + 静态提升共同构成"动态点最小化"。
- 识别要点：面试能现场用位运算表达"动态 props 集合"（flag & PROPS → 遍历 dynamicProps 数组）。

```javascript
// PatchFlag 位标志（源码级简化）
export const PatchFlags = { TEXT: 1, CLASS: 2, STYLE: 4, PROPS: 8, FULL_PROPS: 16 };
function patchElement(n1, n2) {
  if (n2.patchFlag === 0) { fullDiff(n1, n2); return; }         // 无标记：全量
  if (n2.patchFlag & PatchFlags.TEXT) {                          // 位测试
    if (n1.children !== n2.children) setElementText(n1.el, n2.children);
    return;                                                      // 只更新文本，跳过 props/children
  }
  if (n2.patchFlag & PatchFlags.PROPS) {
    for (const key of n2.dynamicProps) if (n1.props[key] !== n2.props[key]) patchProp(...);  // 只 diff 动态 props
  }
}
// Lane 位图：
// const NoLanes = 0b00000; includesSomeLanes(lanes, syncLane) → lanes & syncLane !== 0
// mergeLanes(a, b) → a | b；优先级比较：更低的 bit 值 = 更高优先级
```
