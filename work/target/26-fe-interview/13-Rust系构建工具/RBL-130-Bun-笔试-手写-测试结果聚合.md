---
title: [RBL-130] 笔试：手写测试结果聚合器（分片并行 + 汇总报告）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-130：笔试：手写测试结果聚合器（分片并行 + 汇总报告）
**答**：写 test-aggregate.ts：1) 把测试文件列表均匀分成 N 片并行跑（bun test 每片一个子进程）；2) 收集每片的 pass/fail 数与耗时；3) 汇总输出总报告（总/过/败/总耗时）；4) 失败片输出失败文件清单；5) 退出码 = 有失败则 1。

```typescript
// test-aggregate.ts
import { spawn } from 'node:child_process';
import { readdirSync } from 'node:fs';

const files = listTests('./src');
const SHARDS = Math.min(4, files.length);
function shard(arr: string[], n: number) {
  const out: string[][] = Array.from({ length: n }, () => []);
  arr.forEach((f, i) => out[i % n].push(f)); // 轮转均匀分片
  return out;
}
function listTests(dir: string): string[] {
  const out: string[] = [];
  const walk = (d: string) => {
    for (const e of readdirSync(d, { withFileTypes: true })) {
      const p = `${d}/${e.name}`;
      if (e.isDirectory()) walk(p);
      else if (/\.test\.(ts|tsx)$/.test(e.name)) out.push(p);
    }
  };
  walk(dir); return out;
}

const results = await Promise.all(shard(files, SHARDS).map(async (group) => {
  const t0 = performance.now();
  const p = spawn('bun', ['test', ...group], { stdio: ['ignore', 'pipe', 'pipe'] });
  let out = '';
  p.stdout.on('data', d => out += d);
  p.stderr.on('data', d => out += d);
  const code: number = await new Promise(res => p.on('exit', res));
  return {
    duration: performance.now() - t0,
    ok: code === 0,
    files: group,
    failedFiles: code === 0 ? [] : group, // 失败片粗定位（细粒度可解析输出）
    log: out,
  };
}));

const pass = results.filter(r => r.ok).length;
const totalMs = Math.max(...results.map(r => r.duration));
console.log(`分片 ${SHARDS} | 片过 ${pass}/${results.length} | 总耗时 ${(totalMs / 1000).toFixed(1)}s`);
const failed = results.filter(r => !r.ok);
if (failed.length) {
  console.error('失败分片文件:', failed.flatMap(f => f.failedFiles));
  process.exit(1);
}
```
**评分点**：
- 轮转分片（均匀且简单）。
- 并行子进程收集（Promise.all + exit code）。
- 失败定位输出失败文件清单。
- 总耗时取 max（并行墙钟时间）。
- exit code 语义正确。
