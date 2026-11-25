---
title: [BAS-185] fs 的同步、异步 API 怎么选？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-185：fs 的同步、异步 API 怎么选？
**答**：
- 同步 readFileSync：CLI 脚本、启动时一次性读配置，简单但阻塞整个进程。
- 回调/promise 版（fs.promises 或 await）：服务端常规首选，不阻塞事件循环。
- createReadStream：大文件处理、边读边写、限流转发，配合流式管道。

```javascript
const fs = require('fs');
// 同步：CLI 启动时读一次配置，简单直接
const config = JSON.parse(fs.readFileSync('config.json', 'utf8'));
// 异步 promise：服务端首选，不阻塞事件循环
async function load() { return JSON.parse(await fs.promises.readFile('config.json', 'utf8')); }
// 流式：GB 级日志按行处理
fs.createReadStream('app.log').pipe(process.stdout);
```
