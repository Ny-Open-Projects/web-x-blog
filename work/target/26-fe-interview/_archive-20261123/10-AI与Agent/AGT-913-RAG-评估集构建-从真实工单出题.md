---
title: [913] RAG 评估集怎么建？为什么强调从真实工单出题
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 评估集]
type: 面试题
---

## 913：RAG 评估集怎么建？为什么强调从真实工单出题

**答**：
- 评估集是 RAG 迭代的地基，最大的坑是「开发自编问题」：自己写的 query 与自己切的 chunk 语义同源，评估分数虚高，上线即翻车。
- 正确来源：真实工单、客服对话、搜索日志里未被满足的 query，按意图分层抽样（事实型/流程型/对比型/拒答型），拒答型必须占 10%~15% 用于测幻觉。
- 每条评估项 = query + 标准答案 + 关键证据出处（chunk 或段落）+ 意图类型；没有证据出处的条目没法算检索指标。
- 规模经验：冷启动 100~200 条即可支撑迭代，稳定期按线上 badcase 每月滚动补充并冻结「回归集」（不许改，防指标漂移）。
- 追问钩子：评估集会不会过拟合？——用训练迭代没见过的「留出集」定期盲测，且证据出处随文档更新同步迁移。

```ts
interface EvalCase { query: string; goldAnswer: string; evidence: string[];
  intent: 'fact'|'flow'|'compare'|'reject'; hard?: boolean }
// 从工单导出 -> LLM 辅助提炼 query -> 人工标注答案与证据 -> 入库
const set: EvalCase[] = await buildFromTickets({
  source: ticketsDb.lastNDays(90),
  stratify: { fact: 0.4, flow: 0.25, compare: 0.2, reject: 0.15 },
});
```

