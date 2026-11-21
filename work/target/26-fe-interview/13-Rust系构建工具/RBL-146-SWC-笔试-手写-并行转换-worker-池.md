---
title: [RBL-146] 笔试：手写多进程并行转换器（swc transform worker 池）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-146：笔试：手写多进程并行转换器（swc transform worker 池）

**题目**：写 transpile-all.mjs：1) 递归收集 src 下所有 .ts/.tsx 文件；2) 用 worker_threads 起 min(CPU核数-1, 8) 个 worker 并行调用 @swc/core 转换（target es2020，automatic runtime）；3) 结果写到 .out/ 目录同名 .js；4) 任一文件转换失败不影响其他文件，最后汇总成功/失败数并以失败数非 0 退出码 1 退出；5) 主线程不转文件，只做调度。

```javascript
// transpile-all.mjs
import { Worker, isMainThread, parentPort, workerData } from 'node:worker_threads';
import { readdirSync, mkdirSync, writeFileSync, readFileSync } from 'node:fs';
import { join, dirname, relative } from 'node:path';
import os from 'node:os';

const SRC = 'src', OUT = '.out';

if (!isMainThread) {
  // worker：只做转换
  const { transform } = require('@swc/core');
  const files = workerData.files;
  const results = [];
  for (const file of files) {
    try {
      const code = readFileSync(file, 'utf8');
      const out = transform.sync(code, {
        filename: file,
        jsc: { parser: { syntax: 'typescript', tsx: file.endsWith('.tsx') }, target: 'es2020',
               transform: { react: { runtime: 'automatic' } } },
        module: { type: 'es6' },
      });
      results.push({ file, code: out.code });
    } catch (e) { results.push({ file, error: e.message }); }
  }
  parentPort.postMessage(results);
} else {
  function collect(dir, acc = []) {
    for (const e of readdirSync(dir, { withFileTypes: true })) {
      const p = join(dir, e.name);
      if (e.isDirectory()) collect(p, acc);
      else if (/\.(ts|tsx)$/.test(e.name)) acc.push(p);
    }
    return acc;
  }
  const files = collect(SRC);
  const N = Math.min(Math.max(1, os.cpus().length - 1), 8);
  const buckets = Array.from({ length: N }, () => []);
  files.forEach((f, i) => buckets[i % N].push(f)); // 轮转分桶

  const all = await Promise.all(buckets.map(b =>
    new Promise(res => {
      const w = new Worker(new URL(import.meta.url), { workerData: { files: b } });
      w.on('message', res);
    })));

  let ok = 0, fail = 0;
  for (const batch of all.flat()) {
    if (batch.error) { console.error('FAIL', batch.file, batch.error); fail++; continue; }
    const target = join(OUT, relative(SRC, batch.file).replace(/\.tsx?$/, '.js'));
    mkdirSync(dirname(target), { recursive: true });
    writeFileSync(target, batch.code); ok++;
  }
  console.log(`done ok=${ok} fail=${fail}`);
  process.exit(fail ? 1 : 0);
}
```
**评分点**：
- 主线程只调度、worker 只转换（职责分离，isMainThread 分支正确）。
- worker 数 = min(cpu-1, 8) 且轮转分桶均衡。
- 单文件失败捕获不中断整批，退出码语义正确。
- 输出路径用 relative 重映射 + tsx→js 后缀处理 + mkdir recursive。
- 能说明 transform.sync 在 worker 内跑避免主线程阻塞。
