---
title: [AIC-940] 商品列表一次 AI 结对对话吃掉几十万 token，账单吓人，上下文成本应该怎么系统性地降？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-940：商品列表一次 AI 结对对话吃掉几十万 token，账单吓人，上下文成本应该怎么系统性地降？
**答**：
- 先「看清钱花在哪」：建立 token 计量与归因（按会话/任务/模型统计输入与输出 token），结论：没有成本可观测性，优化就是盲猜。
- 分层优化手段：① 减少输入——上下文裁剪、去重、RAG 按需检索（呼应 AIC-940+）；② 减少输出——让 AI 简洁作答、结构化输出避免废话；③ 选对模型——简单任务用便宜小模型，难任务才用大模型。
- 利用缓存：稳定前缀（系统提示、规则文件、公共上下文）做 prefix caching，重复对话只传增量；把高频问答沉淀为可复用模板。
- 追问钩子：能提出「成本优化不是一味省 token，而是让每个 token 产生价值——省掉无效上下文比压缩有效上下文更重要」的候选人有正确的成本观。

```typescript
// token 成本归因与优化决策
function costReport(calls) {
  const byTask = {};
  for (const c of calls) {
    const k = c.task || 'unknown';
    byTask[k] ??= { in:0, out:0, usd:0 };
    byTask[k].in += c.inTok; byTask[k].out += c.outTok;
    byTask[k].usd += (c.inTok*c.inRate + c.outTok*c.outRate)/1000;
  }
  return Object.entries(byTask).map(([task,v]) => ({ task, usd:+v.usd.toFixed(3) }))
    .sort((a,b)=>b.usd-a.usd);
}
const calls = [
  { task:'商品列表', inTok:80000, outTok:4000, inRate:0.003, outRate:0.015 },
  { task:'埋点',     inTok:5000,  outTok:1000, inRate:0.003, outRate:0.015 },
];
console.log(costReport(calls)); // 定位最烧钱任务，优先优化
```
