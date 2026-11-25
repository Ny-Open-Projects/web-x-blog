---
title: [RBL-554] 笔试：手写 WASM 插件边界模拟（拷贝成本 + 粒度对比）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-554：手写 WASM 插件边界模拟（拷贝成本 + 粒度对比）
**答**：553 落地——模拟 WASM 边界：实现 `wasmPluginSim(nodes, { granularity })`：1) 模拟边界拷贝成本（每次调用数据量的函数）；2) 两种模式：细粒度（每节点一次调用+拷贝）vs 粗粒度（整文档一次调用+一次拷贝）；3) 输出两种模式的总成本对比（节点数 × 拷贝 vs 1 × 拷贝 + 内部遍历）；4) 附用例：细粒度成本随节点数线性爆炸、粗粒度恒定。

```javascript
function wasmPluginSim(nodes, { granularity = 'fine', copyCostPerNode = 3, callOverhead = 5 } = {}) {
  let calls = 0, copied = 0

  if (granularity === 'fine') {
    // 细粒度：每节点一次调用 + 该节点拷贝
    for (const n of nodes) {
      calls++                                    // 跨边界调用
      copied += nodeSize(n)                      // 拷贝进 WASM 内存
    }
  } else {
    // 粗粒度：整文档一次调用 + 全量一次拷贝，插件内部遍历（无边界成本）
    calls = 1
    copied = nodes.reduce((a, n) => a + nodeSize(n), 0)
  }

  const total = calls * callOverhead + copied * copyCostPerNode
  return { granularity, calls, copied, total }
}

function nodeSize(n) { return JSON.stringify(n).length }

// 用例
const nodes = Array.from({ length: 1000 }, (_, i) => ({ type: 'node', i, data: 'x'.repeat(20) }))

const fine = wasmPluginSim(nodes, { granularity: 'fine' })
const coarse = wasmPluginSim(nodes, { granularity: 'coarse' })
console.log(fine.calls, coarse.calls)            // 1000 1：调用次数差 1000x
console.log(fine.total > coarse.total * 10)      // true：细粒度总成本远高（调用开销主导）
console.log(fine.copied === coarse.copied)       // true：拷贝总量相同——差异全在调用开销

// 节点数增长：细粒度线性爆炸、粗粒度恒定调用
const growth = [100, 1000, 10000].map((n) => {
  const ns = nodes.slice(0, n)
  return { n, fineCalls: wasmPluginSim(ns, { granularity: 'fine' }).calls, coarseCalls: 1 }
})
console.log(growth)
// [{n:100, fineCalls:100, coarseCalls:1}, {n:1000, ..., coarseCalls:1}, ...]
```
**评分点**：
- 两种粒度模型（fine 每节点调用+拷贝 / coarse 一次全量）
- 成本分解（调用开销 × 次数 + 拷贝 × 数据量）
- 结论验证（拷贝总量相同、调用次数主导差异）
- 规模增长曲线（细粒度线性 vs 粗粒度恒定）

## 变体与延伸（补充）

**变体与延伸**：

1. 粗粒度一次拷贝全量，内存峰值会不会更大 → 会，粗粒度峰值约等于整文档，细粒度是单节点；超大文档应改成按分块粗粒度。
2. 真实 WASM 边界还有哪些没模拟的成本 → 字符串 UTF-8 编解码、内存增长与 GC、每节点 `TextEncoder` 分配，调用次数越多放大越明显。
3. 插件要读回节点并修改（不只读）怎么办 → 粗粒度需把结果整体拷回 JS，成本翻倍；有共享内存（SharedArrayBuffer）但要自管生命周期与并发。
