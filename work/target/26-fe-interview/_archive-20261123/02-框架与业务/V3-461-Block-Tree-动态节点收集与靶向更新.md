---
title: [V3-461] Block Tree：动态节点收集与靶向更新的数据结构
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-461：Block Tree：动态节点收集与靶向更新的数据结构

**答**：
- Block 概念：v-if/v-for/组件等「结构边界」开启新 block，收集其子孙中所有「动态节点」（带 patchFlag 的 vnode）到 block.dYNAMIC_CHILDREN 平铺数组
- 靶向更新原理：更新时不再递归整棵树 diff，只遍历 block 的动态节点数组按 patchFlag 做「定点修复」——静态节点完全绕过，这就是 Vue3 更新快的本质
- 嵌套结构：block 之间形成树（openBlock/createBlock），v-for 内每项是子 block——update 时先 diff block 结构再逐 block 修动态点
- 收集时机限制：只有「编译模式」才有 block 信息（runtime 模板编译退化到传统 diff）；patchFlag 编码（1 TEXT/2 CLASS/4 STYLE/8 PROPS/16 FULL_PROPS/64 STABLE_FRAGMENT...）决定修复动作
- 深水点：manuallyOpenedBlock 场景（v-html 内容里的动态性无法收集）→ 退回 FULL_PROPS 全量 diff——「动态性藏在字符串里」是靶向更新的盲区

```text
<div>静态头 {{ msg }} <Comp :n="n"/></div>
block.dYNAMIC_CHILDREN = [
  { vnode: text, flag: TEXT },          // 只修 textContent
  { vnode: Comp, flag: PROPS['n'] },    // 只更新 n prop
]
// 更新: 两次定点修复, 不遍历静态头
```
