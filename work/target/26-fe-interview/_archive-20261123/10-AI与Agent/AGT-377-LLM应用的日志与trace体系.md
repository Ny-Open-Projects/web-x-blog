---
title: [AGT-377] LLM 日志与 Trace——可观测体系怎么建？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-377：LLM 应用的日志与 trace 体系怎么设计（区别于传统应用）？

**答**:
- trace 结构：以"任务"为根（task_id），每步 LLM 调用/工具调用/检索为 span——记录输入输出全文（不同于传统只记元数据：LLM 调试必须能看全文）、token 与成本、模型与 prompt 版本（AGT-289 审计要求）。
- 与传统 trace 的差异：span 的"耗时"之外还有"质量"维度（每步可挂 judge 评分/校验结果）——质量维度是 LLM trace 的特有属性；上下文快照（每步的完整 prompt 存档——AGT-369 回放的原料）。
- 存储策略：全文日志量大且含敏感——分级存储（近期全量可查/长期采样归档）、脱敏管道（日志中的 PII 处理）、保留期合规。
- 应用面：调试回放（AGT-369）、评测关联（badcase 一键带入 trace 上下文）、成本分析（AGT-276 切片）、审计（合规追溯）——trace 是其他所有治理能力的地基。

```javascript
trace.task(taskId, {
  spans: [{ type: 'llm', model, promptVer,
    input, output, tokens, cost, qualityScore },
    { type: 'tool', name, args, result }],
  contextSnapshot: fullPrompt,       // 回放原料
});
// 分级存储 + PII 脱敏 + 保留期合规；
// trace = 调试/评测/成本/审计的地基。
```
