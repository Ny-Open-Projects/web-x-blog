---
title: [RBL-128] 笔试：手写多任务并行 runner（子进程 + 失败聚合）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-128：笔试：手写多任务并行 runner（子进程 + 失败聚合）
**答**：写 run-tasks.ts：1) 并行执行给定命令列表（bun spawn 子进程）；2) 实时透传各任务输出（带任务名前缀）；3) 任一失败不立即退出，等全部结束后统一报告失败清单并 exit 1；4) 支持 maxConcurrency 限流；5) 总耗时输出。

```typescript
// run-tasks.ts —— bun run-tasks.ts "build:a" "build:b" "test"
import { spawn } from 'node:child_process';

const tasks = process.argv.slice(2);
const MAX = 4;
const failures: string[] = [];
const start = performance.now();

function run(cmd: string) {
  return new Promise<void>((resolve) => {
    const [bin, ...args] = cmd.split(' ');
    const p = spawn(bin, args, { stdio: ['ignore', 'pipe', 'pipe'] });
    const tag = `[${cmd}]`;
    p.stdout.on('data', d => console.log(tag, d.toString().trimEnd()));
    p.stderr.on('data', d => console.error(tag, d.toString().trimEnd()));
    p.on('exit', (code) => {
      if (code !== 0) failures.push(cmd);   // 失败聚合，不提前退出
      resolve();
    });
  });
}

// 限流执行：同时最多 MAX 个
const queue = [...tasks];
async function worker() {
  while (queue.length) await run(queue.shift()!);
}
await Promise.all(Array.from({ length: Math.min(MAX, tasks.length) }, worker));

console.log(`\n总耗时 ${(performance.now() - start / 1) .toFixed ? ((performance.now() - start) / 1000).toFixed(1) : 0}s`);
if (failures.length) {
  console.error('失败任务:', failures.join(', '));
  process.exit(1);
}
```
**评分点**：
- 失败聚合不提前退出（等全部完成统一报告）。
- 输出带任务名前缀（可读性）。
- 限流 worker 池模式（maxConcurrency）。
- exit code 语义（CI 门禁）。
- 子进程 stdout/stderr 分流透传。
