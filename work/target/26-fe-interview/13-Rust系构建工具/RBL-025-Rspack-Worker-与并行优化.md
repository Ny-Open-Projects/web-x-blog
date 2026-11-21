---
title: [RBL-025] Rspack 中 worker/多线程相关优化有哪些？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-025：Rspack 中 worker/多线程相关优化有哪些？
**答**：
- 内核已并行：parse/transform/minify 在 Rayon 线程池跑，webpack 时代的 thread-loader/terser 的 parallel 选项在 Rspack 里不再需要甚至有害（额外进程管理成本）。
- 需要并行的是 JS 侧：多个 JS plugin 钩子回调仍在 Node 主线程串行；重计算任务（如生成大 JSON manifest）应挪到独立 worker（node worker_threads）异步做。
- worker_threads + loader：如果必须保留重 JS loader，可以把 loader 放 worker pool；但 Rspack 官方更建议换成 Rust 内置等价物。
- 构建器外并行：把互相独立的构建（多端产物）拆成并行 CI job，比进程内优化收益更稳定。
- 监控指标：CPU 利用率曲线——Rust 内核并行好的构建接近满核；若构建中 CPU 长期单核满载其余空闲，瓶颈多半在 JS 侧。
- 追问钩子：npm 包并行安装（如 pnpm）与构建并行是两个层面，别混淆。

```javascript
// worker_threads 侧路：plugin 钩子里把重活扔给 worker，不阻塞构建
const { Worker } = require('worker_threads');
function runHeavyAsync(data) {
  return new Promise((resolve, reject) => {
    const w = new Worker(`${__dirname}/manifest-worker.js`, { workerData: data });
    w.on('message', resolve).on('error', reject);
  });
}
class AsyncManifestPlugin {
  apply(compiler) {
    compiler.hooks.emit.tapPromise('AsyncManifestPlugin', async (compilation) => {
      const manifest = await runHeavyAsync({ assets: Object.keys(compilation.assets) });
      compilation.emitAsset('manifest.json',
        { source: () => manifest, size: () => manifest.length });
    });
  }
}
```
