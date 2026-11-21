---
title: [MFW-308] React Compiler 自动记忆化的能力边界
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-308→MFW-308：React Compiler 边界

**答**:
- 能做什么：组件/props 级自动 memo（useMemo/useCallback 大部分手写可省）、渲染期表达式缓存——按编译期可静态分析的规则（引用透明/无副作用）
- 边界一：外部 store 订阅（useSyncExternalStore 语义）与命令式 ref 逃逸——编译器保守跳过（该处仍需手写优化或接受重渲染）
- 边界二：跨 RSC 边界 props 每次新引用（MFW-204）——编译器无法阻止（序列化产物天然不稳），值比较责任仍在业务
- 采用策略：先 lint 模式（报告可优化/跳过清单）→ 无害组件批开 → 热路径组件逐个验证（Profiler 前后对比）——不是全局开关一开了事

```text
能力：自动 memo 化静态可析组件
边界：外部 store/ref 逃逸跳过；RSC props 引用不稳不归它管
策略：lint 报告 → 批量无害 → 热路径逐个 Profiler 验证
```
