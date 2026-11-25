---
title: [FRP-205] 无 key 列表在 Vue2/Vue3/React 中 diff 行为有何差异？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-205：无 key 列表在各框架中 diff 行为差异？
**答**：
- React 无 key：按位复用（key=null 走同位置更新），就地更新文本/属性——头部插入时整列表属性更新，DOM 节点不移动。
- Vue3 无 key：走 patchUnkeyedChildren 简单按位 diff（非双端），同样就地更新。
- Vue2 无 key：同位比较 + 简单策略，也是就地更新。
- 共同风险：组件内部 state/输入焦点会「错位」——节点复用后 state 跟着节点走，导致第 1 行的输入框内容出现在第 2 行。
- 结论：无 key 就地复用性能好但语义危险，仅适合纯展示、无组件状态列表；有状态列表必须业务 key。
