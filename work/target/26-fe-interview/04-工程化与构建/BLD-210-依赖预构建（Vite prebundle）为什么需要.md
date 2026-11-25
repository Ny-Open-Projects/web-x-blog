---
title: [BLD-210] 依赖预构建（Vite prebundle）为什么需要？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-210：依赖预构建为什么需要？
**答**：
- 问题：dev 模式原生 ESM 直接服务 node_modules——一个包内部几百个请求（lodash-es 每函数一个文件）、CJS 包浏览器无法直接执行。
- 预构建：esbuild 把依赖预打包成单文件 ESM（缓存到 node_modules/.vite）——dev 首次请求 1 个文件而非几百个。
- 缓存失效：lockfile/配置/vite 版本变化触发重新预构建——「手动 optimizeDeps」的场景（动态 import 新依赖）。
- 与 SSR 的交互：SSR 时外部化依赖（external）直接 node require——dev 与 prod 的模块语义差异（SSR dev external vs prod bundled）导致「dev 好使 prod 报错」。
- 追问钩子：为什么 dev 模式还要「打包」依赖（与 unbundled dev 的初衷矛盾）——unbundled dev 的收益是源码按需转换（改一个文件只转一个）；而 node_modules 不常改，逐文件服务纯浪费请求——「源码 unbundled + 依赖预打包」是按「变更频率」区分处理策略，两者不矛盾。

```bash
# 预构建触发条件
node_modules/.vite/deps_temp → lockfile/config/vite version 变化 → 重跑 esbuild
```
```javascript
// vite.config
optimizeDeps: { include: ['lodash-es', 'react-dom/client'],   // 提前预构建（防瀑布）
                exclude: ['@my/ui'] }                          // link 包排除
```
