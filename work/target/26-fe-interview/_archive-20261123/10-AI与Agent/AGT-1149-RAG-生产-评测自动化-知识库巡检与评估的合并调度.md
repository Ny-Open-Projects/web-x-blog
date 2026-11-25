---
title: [1149] 知识库巡检和 RAG 评估能不能合并成一个调度体系
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 调度]
type: 面试题
---

## 1149：知识库巡检和 RAG 评估能不能合并成一个调度体系

**答**：
- 能合并且应该合并：两者共享「探针」机制（从文档生成问题→检索→断言），巡检是「文档视角」（每篇文档的可达性），评估是「query 视角」（每个问题的回答质量），合在一个调度器里共享探针生成与执行设施。
- 调度设计：巡检（周度全量、日度增量——只查新增/变更文档）、评估（变更触发 + 夜间全量）、探针缓存（同一文档的探针题生成一次复用）。
- 产物统一入看板：巡检发现「文档不可达」、评估发现「query 失败」汇聚到同一归因看板，交叉验证（文档不可达 + 相关 query 失败 = 确认级问题）。
- 追问钩子：合并的最大陷阱？——职责混杂：巡检产物（工单给文档 owner）和评估产物（门禁卡合并）必须分流，混在一起会出现「文档问题挡住代码合并」的误伤。

```ts
scheduler.register({
  patrol: { cron: 'weekly', scope: 'all-docs', out: 'tickets' },
  patrolIncr: { trigger: 'kb_change', scope: 'changed-docs', out: 'tickets' },
  evalGate: { trigger: 'code_change', out: 'gate' },
  evalNightly: { cron: 'nightly', out: 'report' },
}, { sharedProbeCache: true });   // 探针生成共享缓存
```
