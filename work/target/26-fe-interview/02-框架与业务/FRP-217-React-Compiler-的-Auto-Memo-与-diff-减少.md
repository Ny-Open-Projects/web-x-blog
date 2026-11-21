---
title: [FRP-217] React Compiler 的自动 memo 如何减少 diff 范围？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-217：React Compiler 的自动 memo 如何减少 diff 范围？
**答**：
- 编译期分析组件输入（props/state/上下文），自动插入 memo 比较：props 未变则跳过该子树 render，diff 直接短路。
- 对 JSX 子树做细粒度 memo（元素级），等价手写 useMemo(jsx) 但无依赖遗漏。
- 减少的不只是 render 时间，还有 reconcile 的 vnode 创建与比较。
- 局限：动态 props（函数内联、对象字面量）需稳定引用——compiler 会把常见内联提升；不可靠代码跳过优化。
- 与虚拟列表组合：行组件自动 memo 后，虚拟滚动更新只重渲染进出视口的行。
