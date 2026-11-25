---
title: [NODE-224] 子进程 stdio 流与管道死锁？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-224：子进程 stdio 流与管道死锁？
**答**：
- spawn 的 stdio 配置：pipe（流式交互）/inherit（直连父）/ignore（丢弃）。stdout/stderr 都要消费——只 pipe stdout 不读 stderr，stderr 缓冲满 → 子进程阻塞 → 死锁（64KB 缓冲默认值，NODE-222）。
- exec vs spawn：exec 缓冲全部输出（默认 maxBuffer 1MB，超限 kill）——大输出必须 spawn 流式。
- 交互式管道：父进程 stdin 写入子进程（backpressure 保留）。
- 实战：ffmpeg 转码子进程（NODE-182）的进度解析——按行读 stdout，stderr 消费丢入日志。

```javascript
import { spawn } from 'node:child_process';

// 反模式（死锁）：
// spawn('ffmpeg', [...]) —— stdout 监听了，stderr 没消费 → stderr 缓冲满 → 卡死
// 正确：
const child = spawn('ffmpeg', ['-i', 'in.mp4', '-f', 'null', '-']);
child.stdout.on('data', parseProgress);            // 流式进度
child.stderr.on('data', chunk => logger.write(chunk));   // 必须消费 stderr
child.on('close', code => code === 0 ? done() : retry());
// 大输出：
const big = spawn('cat', ['huge.txt']);            // 用 spawn 而非 exec
for await (const chunk of big.stdout) process(chunk);     // 流式，无 maxBuffer 限制
// 手工管道背压：
big.stdout.pipe(gzip).pipe(uploadStream);          // pipeline 更稳（NODE-212）
```
