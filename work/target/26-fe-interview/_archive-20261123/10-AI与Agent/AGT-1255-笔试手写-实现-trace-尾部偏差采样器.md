---
title: [1255] 笔试手写：实现 trace 尾部偏差采样器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, 可观测]
type: 笔试题
---

## 1255：笔试手写：实现 trace 尾部偏差采样器

**需求**：实现 sampleTraces(traces)：traces 为 { id, ms, error: bool }[]。采样规则：错误全采；ms > P90 的慢请求全采；其余按 rate（默认 0.1）随机采；记录每层采样率供反加权。返回 { sampled, rates: { error: 1, slow: 1, normal } }。

```js
function sampleTraces(traces, rate = 0.1) {
  const sorted = [...traces].sort((a, b) => a.ms - b.ms);
  const p90 = sorted[Math.floor(sorted.length * 0.9)]?.ms ?? Infinity;
  const sampled = [], counter = { error: [0, 0], slow: [0, 0], normal: [0, 0] };
  for (const t of traces) {
    const layer = t.error ? 'error' : t.ms > p90 ? 'slow' : 'normal';
    const take = layer !== 'normal' || Math.random() < rate;
    counter[layer][0]++; if (take) counter[layer][1]++;
    if (take) sampled.push({ ...t, layer });
  }
  const rates = {};
  for (const k of Object.keys(counter))
    rates[k] = counter[k][0] ? +(counter[k][1] / counter[k][0]).toFixed(3) : 0;
  return { sampled, rates };
}
```

**评分点**：
- P90 阈值先算后用（先排序取分位，再遍历分层）
- 错误层全采保证坏样本不丢
- 输出各层实际采样率（下游反加权必需）
- 能讨论：分层采样后全局 P95 需按 rates 反加权（呼应 unbiasedPercentile）
