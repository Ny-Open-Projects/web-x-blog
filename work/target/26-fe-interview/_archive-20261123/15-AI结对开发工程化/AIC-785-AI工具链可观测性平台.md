---
title: [AIC-785] 如何为 AI 工具链设计统一的可观测性平台
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-785：如何为 AI 工具链设计统一的可观测性平台

**答**：
- 结论先行：统一可观测性 = 把分散在各工具（IDE 插件、CI、网关）的日志/指标/追踪汇聚到一处，用统一 traceId 串联「一次 AI 任务的全生命周期」；没有统一观测就无法定位跨工具问题。
- 三大支柱：1) 指标（延迟、成功率、采纳率、成本）；2) 日志（结构化、带 traceId）；3) 追踪（span 级，覆盖生成/审查/回归各阶段）。
- 平台化要点：采集 SDK 统一上报格式；采样策略（全量关键链路 + 抽样普通链路）；数据脱敏（prompt 含敏感信息）。
- 追问钩子：为什么 prompt 内容上报必须脱敏？——可观测数据通常集中存储、权限更宽，明文 prompt 会成为新的数据泄露面。

```javascript
// 统一可观测：结构化事件 + traceId + 脱敏
function observe(traceId, span, data, redact) {
  const safe = redact ? redact(data) : data;
  return { traceId, span, ts: Date.now(), data: safe };
}
const events = [
  observe('T1', 'ide.complete', { prompt: '登录逻辑', latency: 120 }, d => ({ ...d, prompt: '[redacted]' })),
  observe('T1', 'ci.review', { comments: 3, latency: 800 }),
];
console.log(events[0].data.prompt); // [redacted]
console.log(new Set(events.map(e => e.traceId)).size === 1); // 全链路串联
```
