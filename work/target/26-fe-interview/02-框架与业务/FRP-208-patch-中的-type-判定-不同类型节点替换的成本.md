---
title: [FRP-208] patch 时 type 判定不同类型节点为什么必须「销毁重建」？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-208：type 不同为什么必须销毁重建？
**答**：
- DOM 类型不同（div vs span）：属性集、行为、CSS 命中完全不同——patch 属性无法收敛，复用只会错乱。
- 组件类型不同（A vs B）：state、hooks 链、fiber/实例结构不同，复用会串状态（React hooks 顺序即错位）。
- 成本：销毁重建 = 卸载子树（含 effect 清理）+ 全新创建——远贵于属性 patch，所以「同类型才复用」是铁律。
- 优化含义：条件渲染同结构用相同标签与组件，避免无谓 type 跳变；v-if/v-else 结构尽量对称。
- key 与 type 的判定顺序：先 type 后 key（type 不同直接替换，key 只在同 type 内比较）。
