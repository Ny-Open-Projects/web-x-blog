---
title: [RBL-280] 构建产物部署到 Edge/Serverless 的适配要点
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-280：构建产物部署到 Edge/Serverless 的适配要点

**答**:
- 产物形态适配：Edge Runtime 无 Node API（fs/crypto 限定）、冷启动预算（bundle 小而精）、无持久化——构建配置按目标 runtime 分产物（edge bundle 用 web 标准 API）
- 打包约束：单 worker 体积上限（Cloudflare Workers 1-10MB）、顶层 await 与动态 import 支持、WASM 资源的打包方式
- 适配实现：构建时按 runtime 打包（target: 'webworker'）+ 条件导入（.server/.edge 后缀）+ polyfill 替换（node:buffer → web API）
- 验证：miniflare/wrangler dev 本地模拟 Edge 环境跑冒烟——「本地 Node 能跑 ≠ Edge 能跑」

```text
Edge 构建清单：target webworker / 单文件体积预算 / 无 Node API 审计 /
动态 import 静态化 / 冒烟用 wrangler dev 而非 node
```
