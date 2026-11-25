---
title: [WCN-836] Signals 与 WebAssembly 结合、把计算放到 WASM 的架构怎么设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-836：Signals 与 WebAssembly 结合、把计算放到 WASM 的架构怎么设计？

**答**：
- 结论先行：WASM 负责「重计算」（图像处理、物理模拟、大量数据派生），Signals 负责「响应式编排与 UI」——架构上是「JS 侧 signal 持有输入 → 触发 WASM 计算 → 结果写回 signal → 细粒度更新 UI」。
- 分工边界：只有 CPU 密集、可批处理、数据可序列化的计算才值得放 WASM；频繁的小计算跨界开销（JS↔WASM 调用、线性内存拷贝）反而更慢。
- 异步衔接：WASM 计算通常耗时，用 Signal 的异步派生模式——计算中 signal 置 `pending`，完成时把结果写进成功 signal；避免阻塞主线程与 UI 卡死。
- 内存与序列化：大数组用共享线性内存（`SharedArrayBuffer`）零拷贝传递，或Worker + WASM 组合；注意 WASM 有自己的内存，别在每次计算时反复分配。
- 追问钩子：面试官会问「WASM 里能跑响应式追踪吗」——答：一般不这么做——依赖追踪的图结构放 JS 更灵活；WASM 只做纯函数式计算，响应式调度仍归 JS，职责清晰。

```javascript
// 架构：signal 输入 → WASM 重计算（异步）→ 结果 signal → UI
import { signal } from '@preact/signals-core';
const input = signal(new Float32Array([1, 2, 3, 4]));
const result = signal({ status: 'idle', data: null });

async function recompute() {
  result.value = { status: 'pending', data: null };
  try {
    const ptr = wasm.alloc(input.value.length);
    wasm.memory.set(input.value, ptr);            // 写入 WASM 线性内存
    wasm.heavyCompute(ptr, input.value.length);   // WASM 重计算（示意）
    const out = new Float32Array(wasm.memory.buffer, ptr, input.value.length);
    result.value = { status: 'success', data: out.slice() }; // 写回 signal，UI 细粒度更新
  } catch (e) {
    result.value = { status: 'error', data: null };
  }
}
input.subscribe(recompute);
```
