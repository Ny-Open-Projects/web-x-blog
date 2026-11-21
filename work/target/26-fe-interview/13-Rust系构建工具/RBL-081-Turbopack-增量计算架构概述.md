---
title: [RBL-081] Turbopack 的增量计算架构是怎么回事？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-081：Turbopack 的增量计算架构是怎么回事？
**答**：
- 核心思想：Turbopack 不是"模块级缓存重编"（webpack/Rspack 模式），而是把整个构建建模为函数级增量计算——每个编译步骤（解析、转换、分割）都是一个可记忆化（memoized）的纯函数，输入不变直接复用缓存结果。
- 记忆化粒度到"函数调用"：单文件改一个字符，只重新执行依赖该输入的最小函数链（文件→AST→模块→chunk 的受影响部分），其余全部缓存命中。
- 结果：官方宣称 HMR 可低至毫秒级（个别例子 9.8ms），万级模块应用的冷启动也是秒级。
- 与 Rspack 差异：Rspack 缓存粒度是模块（改一个文件重编该模块及其传播链），Turbopack 粒度是函数调用，理论上更细；代价是缓存结构与依赖追踪复杂度大幅上升。
- 持久化：Turbopack 的持久缓存把函数级计算结果写盘，跨进程重启仍可复用。
- 追问钩子：为什么 Vercel 要自研而不是用 Rspack？——Next.js 需要的 dev 极致增量与 SSR/架构深度集成，webpack 兼容不是它的优先目标。

```text
输入变更 → 依赖图（函数级）反向传播 → 只重算受影响函数
例：改 Button.tsx 一个字符
  parse(Button)      → 重算
  transform(Button)  → 重算
  chunk(“page”)      → 重算该 chunk 的相关片段
  parse 其他 5000 模块 → 全部缓存命中
对比：模块级缓存 → 重编 Button 模块 + 重建包含它的 chunk 产物
```
