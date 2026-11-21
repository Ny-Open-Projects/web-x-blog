---
title: [AIC-218] 规则很多时明显感觉响应变慢变贵，除了 token 数还有哪些影响？如何量化？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-218：规则很多时明显感觉响应变慢变贵，除了 token 数还有哪些影响？如何量化？
**答**：
- 首 token 延迟随输入长度上升；长规则还会让模型输出更啰嗦（模仿规则的长度）。
- 注意力稀释：中段内容容易被忽略，关键约束应放规则开头或结尾。
- 量化：记录每次请求的输入 token、TTFT、产出修改行数，画趋势图找异常规则。
- 缓存友好：规则内容稳定可命中 prompt cache，频繁改规则会让缓存失效。

```javascript
function reportPerf(logs: Array<{ ruleId: string; inTok: number; ttft: number; edits: number }>) {
  const by = new Map<string, { tok: number; ttft: number; n: number }>();
  for (const l of logs) {
    const s = by.get(l.ruleId) ?? { tok: 0, ttft: 0, n: 0 };
    s.tok += l.inTok; s.ttft += l.ttft; s.n++;
    by.set(l.ruleId, s);
  }
  return [...by].map(([id, s]) => ({ id, avgTok: s.tok / s.n, avgTTFT: s.ttft / s.n }));
}
r
```
