---
title: [RBL-122] 笔试：手写 bun 风格的一键打包脚本（含产物体积报告）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-122：笔试：手写 bun 风格的一键打包脚本（含产物体积报告）
**题目**：用 Bun API 写 build.ts：1) 调 Bun.build 打包 src/index.ts 到 dist；2) 输出每个产物的体积与 gzip 估算（用 Bun.file 读产物 + 压缩 API）；3) sourcemap 外部产出；4) 失败时收集日志并 exit 1；5) 总耗时输出。

```typescript
// build.ts —— bun build.ts 直接运行（TS 免编译）
import { gzipSync } from 'node:zlib';

async function main() {
  const start = performance.now();
  const result = await Bun.build({
    entrypoints: ['./src/index.ts'],
    outdir: './dist',
    target: 'browser',
    minify: true,
    splitting: true,
    sourcemap: 'external',
    define: { 'process.env.NODE_ENV': '"production"' },
  });

  if (!result.success) {
    console.error('[build] 失败:');
    for (const log of result.logs) console.error(' -', log);
    process.exit(1);                 // 失败让 CI 断
  }

  let total = 0;
  for (const out of result.outputs) {
    const buf = await out.arrayBuffer();
    const gzip = gzipSync(buf).length;
    total += buf.byteLength;
    console.log(`${out.path}  ${(buf.byteLength / 1024).toFixed(1)}KB (gzip≈${(gzip / 1024).toFixed(1)}KB)`);
  }
  console.log(`total ${(total / 1024).toFixed(1)}KB, ${(performance.now() - start).toFixed(0)}ms`);
}
main();
```
**评分点**：
- Bun.build API 正确（entrypoints/outdir/result.outputs）。
- success 判定 + logs 收集 + exit 1（CI 语义）。
- gzip 用同步压缩估算并标注"估算"。
- 产物遍历含 sourcemap/分片（outputs 全量）。
- 耗时打点（performance.now）。
