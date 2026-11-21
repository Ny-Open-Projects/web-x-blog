---
title: [RBL-143] Vite 为什么从 SWC 生态转向 Oxc/Rolldown
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-143：Vite 为什么从 SWC 生态转向 Oxc/Rolldown

**答**：
- Vite dev 阶段靠 esbuild 预构建、prod 阶段用 Rollup——双内核导致 dev/prod 行为差异（坑：esbuild 支持 `/* @vite-ignore */`、Rollup 插件语义不同，产物不一致）。
- Rolldown 愿景：一个 Rust 内核同时覆盖 dev 转换 + prod 打包 + 预构建，消掉双内核；parser/transform 直接用 Oxc（同仓库生态），避免再嵌 SWC。
- 历史上 Vite 有过 SWC 分支尝试（@vitejs/plugin-react-swc 仍在维护），但 SWC 是外部项目、AST 结构不同、插件语义对不上，集成维护成本高；Oxc 由 Vite 团队核心成员主导，可深度定制。
- 对用户的意义：未来 Vite 升级 Rolldown 后 prod 构建提速数倍，且 Rollup 插件 API 兼容层让存量插件平滑过渡。
- 追问钩子：这也是面试里"工具选型要看治理结构"的案例——技术快不只是一个维度，生态控制权同样关键。

```javascript
// 双内核不一致的经典例子（Rolldown 目标是消除这类差异）
// dev：esbuild 预构建，CJS 互操作走 esbuild 的 default interop
import pkg from 'some-cjs-package'; // dev 下 pkg.default 行为 A
// prod：Rollup + @rollup/plugin-commonjs，interop 策略不同，可能行为 B
import pkg from 'some-cjs-package'; // 产物里 pkg.default 行为 B
// 结果：dev 正常、prod 报错（或反之）。
// Rolldown：CJS 互操作在 Oxc 内统一实现，dev/prod 同一套语义，差异从根上消失。
```
