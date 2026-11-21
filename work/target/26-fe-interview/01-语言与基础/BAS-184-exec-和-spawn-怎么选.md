---
title: [BAS-184] exec 和 spawn 怎么选？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-184：exec 和 spawn 怎么选？
**答**：
- exec：走 shell 执行命令字符串，stdout/stderr 缓冲整体返回（默认上限 200KB），适合短命令、需要管道的场景。
- spawn：不走 shell，参数用数组传递（天然免疫命令注入），流式输出，适合大输出或长驻进程。
- 相关：execSync 阻塞主线程；execFile 类似 spawn 但带回调。

```javascript
const { exec, spawn } = require('child_process');
// exec：shell 字符串 + 整体缓冲，默认 200KB 上限
exec('ls -l | wc -l', (err, stdout) => console.log(stdout));
// spawn：参数数组不走 shell，流式输出，适合大文件与长进程
const ps = spawn('ffmpeg', ['-i', 'input.mp4', 'out.mp4']);
ps.stdout.on('data', chunk => process.stdout.write(chunk));
```
