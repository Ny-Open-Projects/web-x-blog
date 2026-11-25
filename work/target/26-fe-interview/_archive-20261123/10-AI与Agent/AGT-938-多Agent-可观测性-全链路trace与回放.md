---
title: [938] 多 Agent 系统的可观测性要建设哪些东西
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 可观测性]
type: 面试题
---

## 938：多 Agent 系统的可观测性要建设哪些东西

**答**：
- Trace 三层：任务级（编排视图：子任务 DAG 与状态）、消息级（Agent 间每条消息）、模型调用级（每次 LLM 调用的 prompt/响应/token/耗时）；统一 traceId 串联。
- 回放能力：持久化全部消息与工具调用记录，坏 case 能「按原输入重跑」——是归因和回归测试的基础，没有回放的多 Agent 系统没法调试。
- 核心面板指标：任务完成率、平均轮次、子 Agent 失败率分布、token 成本瀑布、人工介入率。
- 追问钩子：prompt 里含敏感数据怎么落 trace？——脱敏存储（密钥/PII 打码）+ 分级查看权限，宁可 trace 少存也不能裸奔。

```ts
function span(type, data) {
  const s = { id: genId(), traceId: ctx.traceId, parent: ctx.spanId,
    type, data: redact(data), ts: Date.now() };
  traceStore.append(s);                     // 全量落盘支持回放
  return { end: (out) => traceStore.patch(s.id, { out: redact(out), dur: Date.now() - s.ts }) };
}
// 用法：const sp = span('llm_call', { agent: 'coder', prompt }); ... sp.end(resp);
```

