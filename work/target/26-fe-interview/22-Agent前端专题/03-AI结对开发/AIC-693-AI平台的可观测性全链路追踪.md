---
title: [AIC-693] AI 平台的可观测性：怎么全链路追踪一次 AI 辅助开发？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-693：AI 平台怎么全链路追踪一次 AI 辅助开发？

**答**：
- 结论先行：**一次 AI 辅助开发横跨「IDE 补全/对话 → 网关 → 模型 → 返回 → 采纳/修改 → 提交 → 上线」，可观测性要能把这些串成一条链，回答「这次 AI 输出最后怎样了」**（AIC-085 Agent 可观测性 / AIC-283 代码溯源）。
- 要记录什么：1) **请求侧**：谁、何时、什么任务、什么上下文（脱敏后）、用了什么模型/prompt 版本；2) **执行侧**：token 消耗、延迟、重试次数、错误类型；3) **结果侧**：是否被采纳、被改了多少、对应哪个 commit、7 天是否存活、是否引发缺陷——这段最难但最有价值（把 AI 调用与代码结果关联）。
- 技术手段：1) **TraceID 贯穿**：从 IDE 到网关到模型全链路带同一个 trace id；2) **结构化日志**（AIC-178 遥测）：统一 event schema；3) **关联代码**：采纳时记录「接受的具体 diff 片段 + commit」，实现从线上 bug 反查是哪次 AI 输出引入。
- 价值：出事故能回放现场（「当时给模型喂了什么上下文」）、度量能闭环（AIC-681）、审计有据可查。
- 追问钩子：为什么「结果侧数据」（采纳/存活/缺陷）比「请求侧数据」（调用量/延迟）更有价值但更难采集？——因为请求侧在网关就能拿到，结果侧要跨系统关联（IDE 事件 + git + issue 系统），链路长、ID 对齐难；但正是结果侧才能回答「AI 到底创造了什么价值」——请求侧只告诉你「用了多少」，结果侧告诉你「赚了还是亏了」。

```typescript
type Span = { traceId: string; stage: string; ts: number; meta?: any };

class Trace {
  constructor(public traceId: string) {}
  span(stage: string, meta?: any): Span { return { traceId: this.traceId, stage, ts: Date.now(), meta }; }
}

function reconstructTrace(spans: Span[]): { stages: string[]; totalMs: number; complete: boolean } {
  const stages = [...new Set(spans.map(s => s.stage))];
  const sorted = [...spans].sort((a, b) => a.ts - b.ts);
  const totalMs = sorted.length ? sorted[sorted.length - 1].ts - sorted[0].ts : 0;
  // 完整链路应含：请求→模型→采纳→提交
  const complete = ['request', 'model', 'accept', 'commit'].every(s => stages.includes(s));
  return { stages, totalMs, complete };
}

const t = new Trace('trace-1');
const spans = [
  t.span('request', { user: 'alice' }),
  t.span('model', { name: 'strong', tokens: 500 }),
  t.span('accept', { diff: '+3 lines' }),
  t.span('commit', { hash: 'a1b2' }),
];
console.log(reconstructTrace(spans).complete === true);
console.log(reconstructTrace(spans.slice(0, 2)).complete === false);
```
