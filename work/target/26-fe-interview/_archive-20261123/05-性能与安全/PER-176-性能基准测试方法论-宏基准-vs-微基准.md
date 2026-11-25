---
title: [PER-176] 性能基准测试方法论（宏基准 vs 微基准）？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-176：性能基准测试方法论（宏基准 vs 微基准）？

**答**：
- **宏基准**（Lighthouse/真机 RUM/WebPageTest）回答"用户感知快不快"，**微基准**（循环计时）回答"这段代码快不快"——顺序永远是先用宏基准找瓶颈，再用微基准验证具体实现。
- 微基准四守则：**预热**（触发 JIT 与内联缓存）、**多轮取样**（7 轮取中位数而非平均值）、**校准空转**（减去循环本身开销）、**防死代码消除**（结果要被消费）。
- 微基准陷阱：不同 JS 引擎/版本结果不可迁移；GC 时机污染单次样本；`performance.now()` 精度有限，单次操作要循环放大。
- 提交基准进 CI：核心算法（如 diff、排序）建基准快照，回归超阈值即拦截。

```javascript
// 微基准：预热 + 多轮取样 + 中位数统计
export function microBench(fn, { iterations = 1e6, samples = 7 } = {}) {
  fn(0); // 预热：触发 JIT 编译与内联缓存
  const results = [];
  for (let s = 0; s < samples; s++) {
    let sink = 0;                       // 防死代码消除：结果必须被消费
    const t0 = performance.now();
    for (let i = 0; i < iterations; i++) sink += fn(i);
    if (sink === -1) console.log(sink);
    results.push(performance.now() - t0);
  }
  results.sort((a, b) => a - b);
  return { median: results[(results.length / 2) | 0], min: results[0], max: results.at(-1) };
}

// 示例：arr[i] vs arr.at(i)，输出 ns/次便于跨迭代数比较
const arr = Array.from({ length: 1e5 }, (_, i) => i);
const r1 = microBench((i) => arr[i % arr.length], { iterations: 1e7 });
const r2 = microBench((i) => arr.at(i % arr.length), { iterations: 1e7 });
console.log('ns/次：', ((r1.median * 1e6) / 1e7).toFixed(1), ((r2.median * 1e6) / 1e7).toFixed(1));
// 方法论：先宏基准定位瓶颈，再用微基准验证实现；顺序不可反
```
