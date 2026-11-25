---
title: [PER-985] HTTP/2 队头阻塞与 HTTP/3 的流级多路复用差异
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-985：HTTP/2 队头阻塞与 HTTP/3 的流级多路复用差异

**答**：
- H2 在 TCP 层仍有队头阻塞：任一包丢失，所有流停等重传；H3 的 QUIC 流独立恢复，丢包只影响所在流。
- 影响面：高丢包弱网下 H2 多流并发反而放大阻塞（包越多丢的概率越高）；H3 收益集中在此。
- 验证方法：弱网模拟（100ms RTT + 2% 丢包）对比 H2/H3 的 LCP 与 TTFB 分布，看 P75 差异。
- 前端动作：开启 H3 后检查资源并发数策略是否还要手动分片（不需要，域名分片是 H1 时代的遗产）。

```javascript
// 弱网对比实验框架（headless）
async function probe(proto) {
  const ctx = await launch({ network: { rttMs: 100, loss: 0.02 } });
  await ctx.setH3(proto === 'h3');
  const t0 = Date.now();
  await ctx.goto('https://shop.example.com');
  const nav = await ctx.metrics();
  return { proto, lcp: nav.lcp, ttfb: nav.ttfb, ms: Date.now() - t0 };
}
// 输出对比表：h2 vs h3，弱网高丢包时 h3 的 LCP 应明显更优
```
