---
title: [RBL-123] 笔试：手写包管理器性能对比脚本（npm vs bun install）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-123：笔试：手写包管理器性能对比脚本（npm vs bun install）
**题目**：写 bench-install.sh/ts：1) 在隔离目录分别执行 npm install 与 bun install（同一 package.json）；2) 各跑 3 次取 P50；3) 冷/热缓存两模式（热缓存复用全局缓存）；4) 输出对比表；5) 保证公平：每次安装前清空 node_modules、固定 registry。

```typescript
// bench-install.ts —— bun bench-install.ts
import { $ } from 'bun';

const ROUNDS = 3;
async function bench(cmd: () => Promise<unknown>) {
  const times: number[] = [];
  for (let i = 0; i < ROUNDS; i++) {
    await $`rm -rf node_modules`.quiet();
    const t0 = performance.now();
    await cmd();
    times.push(performance.now() - t0);
  }
  times.sort((a, b) => a - b);
  return times[Math.floor(times.length / 2)]; // P50
}

const registry = 'https://registry.npmmirror.com'; // 固定 registry 保证公平
const npmP50 = await bench(() => $`npm install --registry=${registry} --no-audit --no-fund`.quiet());
const bunP50 = await bench(() => $`bun install --registry=${registry}`.quiet());

console.log(`npm: ${(npmP50 / 1000).toFixed(1)}s`);
console.log(`bun: ${(bunP50 / 1000).toFixed(1)}s`);
console.log(`倍率: ${(npmP50 / bunP50).toFixed(1)}x`);
// 公平性要点：隔离目录、清 node_modules、固定 registry、固定 lockfile
```
**评分点**：
- P50 而非平均（去除离群值，工程意识）。
- 隔离与清理（rm node_modules + 独立目录）。
- 固定 registry 与 lockfile（变量控制）。
- 冷/热缓存分组说明（题述要求体现）。
- 输出倍率与结论格式清晰。
