---
title: [RBL-948] 综合深水：WASM 模块的运行时集成——裁剪、流式加载与内存复用
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-948：综合深水：WASM 模块运行时集成——裁剪与内存复用

**答**:
- WASM 产物集成（RBL-632 基础上的深水）：1) **模块裁剪**（Rust 侧 wasm-opt/wasm-gc：tree shaking 的 wasm 版——未导出函数的 DCE，体积常砍 40%+；与构建器管线集成：裁剪是产物后处理 pass）；2) **流式加载与缓存**（CompileStreaming + Cache API——编译结果缓存（二次访问零编译成本——编译是 WASM 加载的最大成本）；3) 内存复用（多实例共享 memory vs 独立 memory——独立隔离安全/共享省内存：按模块信任级别选 RBL-557）。
- 构建器的集成点：wasm 裁剪工具链（wasm-pack --target web 产物 → wasm-opt pass）；「WASM 体积预算」（RBL-662 的 wasm 维度——wasm 比 js 更难压缩，预算独立）；加载器胶水的 hash 联动（RBL-632）。
- 裁剪的正确性验证：裁剪后模块的「导出面不变」断言（裁剪器误删被 JS 调用的函数 = 运行时 undefined import——RBL-715 契约校验的 wasm 版：wasm exports ⊆ JS 调用面 ∩）。
- 与 RSC/边缘的结合：edge runtime 的 wasm（workerd 支持 wasm imports——RBL-787 约束下的 wasm 模块体积更敏感）。
- 追问钩子：为什么「编译缓存」对 WASM 比对 JS 更重要？——JS 的解析是 V8 常年优化过的快路径（懒解析/预解析），WASM 编译（验证+编译全模块）在低端机可达数百 ms 且同步占主线程；Cache API 缓存 compiled module（wasm 缓存的原生形态 Safari/Firefox 支持差异）——「缓存的单位与成本」决定策略：WASM 的缓存单位是编译产物而非字节流，与构建缓存的「缓存阶段性产物」思想（RBL-633）同构。

```javascript
// 流式加载 + 编译缓存
async function loadWasmCached(url, { cacheName = 'wasm-v1' } = {}) {
  const cache = await caches.open(cacheName);
  const key = `${url}?h=${manifestHashOf(url)}`;         // 内容寻址键
  const hit = await cache.match(key);
  if (hit) {
    const cachedModule = await hit.arrayBuffer();        // 已编译模块缓存（浏览器实现差异注意）
    return WebAssembly.instantiate(cachedModule, imports);
  }
  const { module, instance } = await WebAssembly.instantiateStreaming(fetch(url), imports);
  // 缓存编译产物（浏览器编译缓存机制可用时）
  const compiled = await cache.put(key, new Response(await module.arrayBuffer?.() ?? new ArrayBuffer(0)));
  return { module, instance };
}
// 裁剪正确性断言
function verifyWasmExports(wasmExports, jsCallSites) {
  const missing = jsCallSites.filter(fn => !(fn in wasmExports));
  if (missing.length) fail(`裁剪误删被调用函数: ${missing}——导出面契约破坏`);
  return true;
}
```
