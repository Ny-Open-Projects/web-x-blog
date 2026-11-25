---
title: [WEB-627] WASM 与 JS 性能基准测试的正确方法
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## WEB-627：WASM 与 JS 性能基准测试的正确方法

**答**：
- 先预热：JIT 与 wasm 优化 tier 都需要热身，基准前空跑几十次，否则测的是解释器速度，结论全错
- 计时口径：排除数据准备（编码/拷贝进线性内存的耗时单独算），只测核心计算；多次取中位数不取均值（避免 GC 抖动拉均值）
- 隔离变量：同一进程内先后跑 JS/wasm 会互相污染（JIT 编译队列、内存布局），交叉多次分组跑；真机矩阵（低端安卓是关键样本）
- 常见误区：测微操作（单次小函数调用）证明 wasm 快——跨界成本占比大结论相反；wasm 的正确战场是「单次调用内完成大批量计算」
- 产物化：基准脚本进仓库（node --experimental-wasm 环境跑逻辑一致的版本），每次升级工具链回归对比，防止「优化反而变慢」

```javascript
function bench(fn, { warmup = 50, rounds = 30 } = {}) {
  for (let i = 0; i < warmup; i++) fn();        // 预热 JIT/优化
  const times = [];
  for (let i = 0; i < rounds; i++) {
    const t0 = performance.now();
    fn();
    times.push(performance.now() - t0);
  }
  times.sort((a, b) => a - b);
  return { p50: times[Math.floor(rounds / 2)], p90: times[Math.floor(rounds * 0.9)] };
}
// 报告: bench(() => wasmImpl(data)).p50 vs bench(() => jsImpl(data)).p50
```
