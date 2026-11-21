---
title: [RBL-301] 构建产物里的 Web Worker 打包怎么处理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-301：构建产物里的 Web Worker 打包怎么处理

**答**:
- 语法：`new Worker(new URL('./worker.ts', import.meta.url), { type: 'module' })`——bundler 识别 URL worker 语法，把 worker.ts 单独打包为独立 chunk
- 关键配置：worker 打包的 target（worker 格式 module vs classic，老浏览器兼容）、chunk 命名（worker 入口加 [name].[contenthash]）、内联模式（小 worker 转 blob URL 减请求）
- 依赖处理：worker 内 import 同步进行（有自己的模块图）；与主线程共享代码会重复打包（体积×2）——共享逻辑抽 pure 函数两处引用可接受，大依赖共享则权衡
- 验证：worker chunk 的 sourcemap 与错误上报（worker 内 unhandled 错误也要监控）

```javascript
// 主线程
const w = new Worker(new URL('./heavy.ts', import.meta.url), { type: 'module' })
// 配置
{ test: /\.worker\.ts$/, use: { loader: 'ts', options: {} },
  chunkFormat: ... }  // 或全局 worker 打包 target
```
