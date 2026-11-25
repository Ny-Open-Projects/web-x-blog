---
title: [WEB-622] JSPI（JS Promise Integration）：让 WASM 同步调用异步 API
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-622：JSPI（JS Promise Integration）：让 WASM 同步调用异步 API

**答**：
- 问题背景：WASM 内是同步栈式执行，但 Web API（fetch/文件/加密）全是异步——传统方案要么把异步逻辑挪到 JS 胶水层（破坏算法整体性），要么用 Asyncify 全量快照（体积与性能代价大）
- JSPI 方案：标记 import（挂起函数）与 export（promising 函数），wasm 调用异步 import 时暂停栈，JS Promise 完成后恢复栈继续执行——对 wasm 代码透明，逻辑保持同步写法
- 典型场景：wasm 实现的 SDK 需要内部 fetch 数据（如 wasm 版数据库引擎、wasm 加密协议栈）、C/Rust 库移植时的网络访问
- 与 Asyncify 对比：Asyncify 编译期插桩、全量栈快照，运行时开销在每次调用；JSPI 浏览器原生栈切换，开销小但需要特性支持（Chrome 灰度中）
- 生产建议：特性检测启用 JSPI，不支持时回退 Asyncify 或 JS 胶水分层方案

```javascript
// 概念代码: JSPI 下 wasm 逻辑保持同步
// (wasm 侧) fn sync_pipeline() { data = suspend_fetch("/api/data"); process(data); }
const { instance } = await WebAssembly.instantiate(mod, {
  env: {
    // 标记为 suspending: wasm 调用它时暂停, 等待 promise
    suspend_fetch: WebAssembly.Suspending(async (url) => (await fetch(url)).arrayBuffer()),
  },
});
// promising: 把同步 wasm 导出包装成返回 promise 的 JS 函数
const run = WebAssembly.promising(instance.exports.sync_pipeline);
await run(); // JS 侧以异步方式驱动, wasm 内部同步写法
```
