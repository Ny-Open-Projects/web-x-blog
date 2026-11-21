---
title: [PER-386] Worker 通信的隐藏成本：什么时候 postMessage 的序列化开销比计算本身还大？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-386：Worker 通信的隐藏成本：什么时候 postMessage 的序列化开销比计算本身还大？

**答**：
- 成本结构：postMessage 的 structured clone 对大对象（10 万行数组、深层嵌套树）的序列化/反序列化是主线程上的同步开销——10MB 对象 clone 约 50~150ms，可能超过 Worker 里省下的计算时间。结论：**小计算 + 大数据 = 不该用 Worker**。
- 判定公式：收益 ≈ Worker 计算时间 - 2×clone 时间 - 调度开销。数据/计算比（字节 ÷ 预期计算 ms）> 100KB/ms 时不划算；< 10KB/ms 时划算。实测方法：主线程直接算 vs Worker 算的端到端耗时对比（同一数据）。
- 规避手段：① Transferable——二进制数据用 ArrayBuffer transfer（零 clone，PER-269）；② 数据常驻——大数据一次性传给 Worker 常驻内存，后续只传小指令（查询/更新），结果只传摘要；③ 压缩传输——大 JSON 先压缩或传字段子集；④ SharedArrayBuffer——高频双向大块数据（PER-269，需 COOP/COEP）。
- 架构含义：Worker 化不是无脑搬——"数据常驻 + 指令通信"的 Worker 服务模式才是大数据场景的正确形态。

```javascript
// 反例：小计算大传输
worker.postMessage(hugeArray);        // clone 120ms
// worker 里 filter 只花 30ms —— 净亏 90ms + 复杂度
// 正解：数据常驻 + 指令通信
// 初始化（一次）：worker.postMessage({ type: 'init', data: hugeArray }) —— clone 一次 120ms
// 之后每次查询：
worker.postMessage({ type: 'query', predicate: 'price<100' });   // 小消息
// worker 返回命中 id 数组（小结果）—— 端到端 5ms
// 判定公式：收益 = workerTime - 2×cloneTime - 调度；数据/计算比 > 100KB/ms 时不该搬
```
