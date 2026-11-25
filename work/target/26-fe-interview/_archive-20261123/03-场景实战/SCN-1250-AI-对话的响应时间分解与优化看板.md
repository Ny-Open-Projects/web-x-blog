---
title: [SCN-1250] AI 对话的响应时间分解与优化看板
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1250：AI 对话的响应时间分解与优化看板

**答**：
- 分解：响应时间 = 排队 + TTFT + 生成时长，分模型/时段看板。
- 优化：瓶颈定位（排队高→扩容/限流；TTFT 高→预连接/prompt 精简）。
- 目标：TTFT P75 < 2s、总时长按输出长度归一（tokens/s 吞吐）。

```javascript
// 响应看板
function latencyBoard(samples) {
  const byModel = groupBy(samples, s => s.model);
  return Object.entries(byModel).map(([model, rows]) => ({
    model,
    queueP75: quantile(rows.map(r => r.queueMs), 0.75),
    ttftP75: quantile(rows.map(r => r.ttftMs), 0.75),
    throughput: +(rows.reduce((s, r) => s + r.outputTokens / (r.genMs / 1000), 0)
      / rows.length).toFixed(1) + ' tok/s',
  }));
}
function quantile(a, q) { const s = [...a].sort((x, y) => x - y);
  return s[Math.floor(s.length * q)] ?? 0; }
function groupBy(arr, fn) { const m = {}; arr.forEach(x => { const k = fn(x); (m[k] ??= []).push(x); }); return m; }
```
