---
title: [FRP-215] patchFlag 在 diff 子节点时如何分流（跳过 keyed diff）？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-215：patchFlag 如何在子节点 diff 时分流？
**答**：
- patchFlag 记录「子节点形态」：KEYED_FRAGMENT / UNKEYED_FRAGMENT / STABLE_FRAGMENT 等。
- KEYED：走完整 keyed diff；UNKEYED：走简单按位 diff；STABLE（无列表，仅普通子节点）：跳过 diff 直接逐个 patch。
- 动态属性 flag（TEXT/CLASS/STYLE/PROPS）：只 patch 对应字段，跳过完整属性遍历。
- 编译器保证：flag 由模板静态分析得出，运行时零成本读取（位与判断）。
- 与手写 JSX 的差距：JSX 无此信息，React 需通用 diff——这就是 Vue3 模板性能优势的来源。
