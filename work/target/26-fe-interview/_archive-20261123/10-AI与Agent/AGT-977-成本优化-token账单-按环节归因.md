---
title: [977] token 成本怎么按环节归因找到最贵的部分
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 成本延迟, token]
type: 面试题
---

## 977：token 成本怎么按环节归因找到最贵的部分

**答**：
- 归因维度：调用类型（检索改写/生成/摘要/审查）、Agent、任务类型；一次任务的成本瀑布图能直接暴露「审查 Agent 比主生成还贵」这类反直觉问题。
- 常见大头：把全量检索结果塞 prompt（上下文膨胀）、多轮对话历史无裁剪、低效重试。治理顺序：上下文裁剪 > 缓存 > 模型降档。
- 计费口径要统一：输入/输出单价不同（输出贵 3~5 倍），成本统计必须分开算，只统计总 token 会误判。
- 追问钩子：缓存命中怎么算成本？——前缀缓存命中的输入按折扣价计（如 10%），统计里单列「缓存节省金额」，这是向上汇报优化成果的硬指标。

```ts
function costOf(calls, price) {
  return calls.map(c => ({
    type: c.type, agent: c.agent,
    in: c.inTokens * price[c.model].in * (c.cacheHit ? 0.1 : 1),
    out: c.outTokens * price[c.model].out,
  })).reduce((m, x) => { const k = x.type + ':' + x.agent;
    (m[k] ??= { in: 0, out: 0 }); m[k].in += x.in; m[k].out += x.out; return m; }, {});
}
```
