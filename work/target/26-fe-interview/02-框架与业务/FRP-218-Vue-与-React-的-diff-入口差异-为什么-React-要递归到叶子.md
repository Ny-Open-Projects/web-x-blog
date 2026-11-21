---
title: [FRP-218] Vue 与 React 的 diff 入口差异：为什么 React 要「递归到叶子」？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-218：为什么 React 的 reconcile 要遍历整棵树？
**答**：
- React 无编译期信息，无法知道「哪些子树不可能变化」——必须递归比较保证正确性（保守正确）。
- beginWork/completeWork 双阶段遍历：每个 fiber 都要「进入」判断 props 是否变化。
- Vue 有 patchFlag/block tree：静态子树整段跳过（compile 时已知），diff 范围由编译器圈定。
- React 的补救：React.memo（人工/Compiler 自动）、shouldComponentUpdate 短路；RSC 把静态部分移到服务端不进客户端 diff。
- 面试表达：「React 用运行时保守遍历 + 人工 memo 补偿 vs Vue 用编译期信息裁剪遍历范围」。
