---
title: [AGT-210] Agentic RAG——让 Agent 自己决定"何时检索、检索什么"？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-210：Agentic RAG 与传统固定管线 RAG 的区别是什么？

**答**:
- 传统 RAG 是固定管线（query→检索→拼上下文→生成），无论什么问题都检索一次；Agentic RAG 把检索变成 Agent 的工具——模型自己决定是否检索、检索什么词、检索几轮、结果不够要不要换词重试。
- 收益场景：多跳问题（自动分解迭代）、需要判断"库里有没有"的问题（先检索后判断，缺证据可拒答）、混合任务（一部分靠参数知识一部分靠检索）——决策交给模型，管线从"固定流程"变"动态规划"。
- 成本与风险：每轮决策是一次 LLM 调用，成本和延迟数倍于固定管线；模型可能检索成瘾（不需要也查）或过度重试——需要最大轮数限制与"信息已足够"的显式判据（在 prompt 中定义）。
- 工程形态：function calling 暴露 `search(query, filter)` 工具 + 系统提示规定检索纪律（先想清楚查什么、结果评估后再决定下一步）+ 轮数/成本护栏，评测用轨迹指标（检索轮数分布、命中率）。

```javascript
// Agentic RAG 工具定义
const tools = [{
  name: 'search',
  description: '检索知识库。先明确要查什么；结果不足时换关键词重试，最多 3 轮；若信息已足够回答，停止检索直接作答。',
  parameters: { query: 'string', filter: 'object?' },
}];
const agent = await runAgent({
  tools, maxSteps: 6,          // 护栏：最多 3 轮检索 + 合成
  system: `检索纪律：1) 先拆解需要哪些信息；
    2) 每次检索后评估是否足够；3) 缺证据时
    明确说明缺口，不得编造。`,
});
```
