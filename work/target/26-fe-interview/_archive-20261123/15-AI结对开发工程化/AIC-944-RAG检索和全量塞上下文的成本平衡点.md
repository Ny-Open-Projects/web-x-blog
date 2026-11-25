---
title: [AIC-944] 什么时候该用 RAG 检索而不是把整个代码库塞进上下文？成本和效果的平衡点怎么找？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-944：什么时候该用 RAG 检索而不是把整个代码库塞进上下文？成本和效果的平衡点怎么找？
**答**：
- 判断标准是「信息密度与规模」：代码库小、强相关时全量塞简单直接；库大、只需少量相关片段时用 RAG——结论：全量的优势是零遗漏，RAG 的优势是成本低且抗干扰。
- 全量塞的问题不仅是贵，还有「注意力稀释」：无关代码会干扰模型判断，导致生成质量下降——RAG 通过只给相关上下文反而可能提升效果。
- 平衡点靠实验：建一组代表性任务，对比全量/RAG 的「成本 + 通过率 + 召回率」，找到满足质量门槛下成本最低的方案；注意 RAG 的召回失败会漏关键信息，需给兜底。
- 追问钩子：能指出「RAG 不是省钱万能药——检索本身有成本且可能漏召回；关键是评估漏召回的代价是否可接受」的候选人，理解方案的真实权衡。

```typescript
// 成本-质量权衡实验：全量 vs RAG
function evaluate(strategy, tasks, run) {
  let cost=0, pass=0;
  for (const t of tasks) {
    const ctx = strategy === 'full' ? t.allCode : retrieve(t.allCode, t.query);
    cost += ctx.length; // 近似 token 成本
    if (run(ctx, t.expect)) pass++;
  }
  return { strategy, cost, passRate:+(pass/tasks.length).toFixed(2) };
}
function retrieve(code, query){ return code.filter(c => c.includes(query)); }
const tasks = [{ allCode:['a.ts','price.ts','b.ts'], query:'price', expect:'ok' }];
console.log(evaluate('full', tasks, ()=>true), evaluate('rag', tasks, ()=>true));
```
