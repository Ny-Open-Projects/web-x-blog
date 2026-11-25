---
title: [BLD-241] Worker 与 WASM 的构建处理怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-241：Worker/WASM 构建处理怎么做？
**答**：
- Worker 构建模式：`new Worker(new URL('./w.js', import.meta.url))` → 构建器独立 chunk（worker 依赖单独打包）+ URL 解析；内联 worker（blob URL——小 worker 免请求）。
- Worker 的类型与产物：module worker（支持 import——现代目标）vs classic（打包器把 worker 依赖内联——兼容目标）；TS 类型（worker 脚本的类型检查同样跑）。
- WASM 处理：.wasm 资源 hash 输出 + instantiate 包装生成 + 流式加载（StreamingCompilation）；与 JS 胶水代码（wasm-bindgen 输出）打包协作。
- 追问钩子：为什么 worker 打包是「独立 chunk 树」——worker 有自己的全局与入口（与主线程不共享模块作用域）；打包器把 worker 文件当独立入口构建（其依赖闭包单独成 chunk）——主 chunk 里只有加载 URL，不是 worker 代码本体；这也是 worker 内不能直接引用主线程模块的原因。

```javascript
// worker 构建模式
const worker = new Worker(new URL('./heavy.worker.ts', import.meta.url), { type: 'module' });
// 产物: heavy.worker-abc123.js 独立 chunk
// WASM
import init from './engine.wasm?init';
const { exports } = await init();                    // 流式编译
```
