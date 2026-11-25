---
title: [NODE-208] node --watch 与本地开发体验？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-208：node --watch 与本地开发体验？
**答**:
- node --watch：官方文件监听重启（22 稳定），--watch-path 可指定目录；替代 nodemon 的常规场景（少一个依赖）。
- 与 nodemon/nodemon 生态对比：官方版零配置、启动更快；缺 env 重载/自定义事件钩子（复杂项目仍可用 nodemon）。
- --watch-preserve-output 保留上次输出（调试日志不刷屏）。
- 组合开发链：node --watch --experimental-strip-types + env-file（--env-file=.env）= 极简 TS 后端开发链（零构建）。

```bash
# 极简开发链（Node 22）
node --watch --env-file=.env --experimental-strip-types server.ts
# 指定监听目录（模块图之外也要热重启时）
node --watch-path=./src --watch server.ts
# monorepo：只 watch 当前包
node --watch-path=./packages/api/src packages/api/server.mjs
# 局限：worker_threads 的重启行为、native 模块更改需要手动重启 —— 复杂场景仍 nodemon
```
