---
title: [NODE-201] Node 22 的核心新特性有哪些？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-201：Node 22 的核心新特性有哪些？
**答**：
- require(esm)：同步 require ESM 模块（顶层 await 除外），CommonJS 与 ESM 互操作门槛大幅降低——渐进迁移利器（NODE-158 的痛点）。
- 稳定的 WebSocket 客户端：全局 WebSocket（浏览器同款 API），服务端作为 WS 客户端不再需要 ws 库。
- watch 模式：node --watch 内置文件监听重启（nodemon 常规场景可省）。
- V8 12.4：Set 方法（union/intersection/difference）、iterator helpers（map/filter/group）。
- 其他：--experimental-strip-types（22.6+ 直接跑 TS）、AbortSignal.any 稳定、process.features.typescript。
- 追问钩子：require(esm) 的限制（同步加载，不能有 TLA）与未解析 ESM 的错误形态。

```javascript
// Node 22 快速上手
// 1) require ESM（模块无顶层 await 时）
const { version } = require('./pkg-info.mjs');    // 22+ OK（21 加 --experimental-require-module）
// 2) 原生 WebSocket
const ws = new WebSocket('wss://echo.example.com');
ws.onopen = () => ws.send('hi');
ws.onmessage = ({ data }) => console.log(data);
// 3) iterator helpers
const active = users.values().filter(u => u.online).take(10).toArray();
// 4) Set 数学
const all = new Set(a).union(new Set(b));
// 5) watch
// node --watch --experimental-strip-types server.ts —— 无 nodemon 无编译，直接跑 TS
```
