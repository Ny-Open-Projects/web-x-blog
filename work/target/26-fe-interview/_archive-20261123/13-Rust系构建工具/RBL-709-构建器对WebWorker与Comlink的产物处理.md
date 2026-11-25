---
title: [RBL-709] 构建器对 Web Worker 的产物处理：worker chunk 的独立打包与跨线程通信
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-709：构建器对 Web Worker 的产物处理：worker chunk 的独立打包与跨线程通信

**答**:
- Worker 文件是独立模块图（有自己的 import 闭包）但物理上要独立文件——构建器处理：`new Worker(new URL('./worker.ts', import.meta.url))` 的语法识别 → worker 入口闭包单独打包成独立 chunk → 产物 URL 注入回主线程代码（hash 文件名联动 RBL-598）。
- worker chunk 的共享依赖问题：worker 与主线程都 import lodash——默认各自打包（体积翻倍）或共享（worker 无法同步 import 主线程 chunk）；解法是把共享依赖复制进 worker chunk（体积 vs 正确性，worker 加载独立的依赖副本是安全默认），构建器输出「重复依赖报告」供审计。
- 构建期转换：worker 代码里的 `self.postMessage` 类型检查、Comlink 式 RPC 的包装（`expose`/`wrap` 语法糖转真实 postMessage 代理）——构建器可以集成这类转换（@surma/comlink-loader 模式），让 worker 调用像同步函数。
- worker 与 HMR：worker chunk 变更 → 重建 worker chunk → 重新实例化 Worker（状态丢失）——构建器提供 worker 级 HMR 语义（重建 + 通知主线程重挂），状态保持交给业务（worker 里的计算状态本就不易保留）。
- 追问钩子：为什么 worker 文件不能用「内联 blob」方案一刀切？——blob worker 无独立 URL（CDN 缓存/独立调试/sourcemap 全失效），且 CSP script-src 严格时 blob 被拦；文件形态是默认，内联是特殊场景（超小 worker 免一次请求）。

```javascript
// worker 语法识别与转换
// 源码：const worker = new Worker(new URL('./heavy.ts', import.meta.url), { type: 'module' });
// 构建产物：
// const worker = new Worker('/assets/heavy.a1b2c3.js', { type: 'module' });  // hash URL 注入

// 构建器实现要点
function handleWorkerImport(mod, graph) {
  if (mod.hasWorkerSyntax) {
    const workerId = graph.makeRoot(mod.workerPath);       // worker 独立入口闭包
    graph.markChunkRoot(workerId, { kind: 'worker' });     // 独立 chunk，参与级联 hash
    rewriteCode(mod.code, worker => assetUrl(worker));     // URL 改写
  }
}
// 共享依赖报告
function reportDuplication(graph) {
  const dup = graph.sharedDeps().filter(d =>
    graph.chunksOf(d).some(c => c.kind === 'worker') &&
    graph.chunksOf(d).some(c => c.kind === 'main'));
  if (dup.length) warn(`主线程与 Worker 重复打包: ${dup.join(', ')}（worker 独立副本是默认安全策略）`);
}
```
