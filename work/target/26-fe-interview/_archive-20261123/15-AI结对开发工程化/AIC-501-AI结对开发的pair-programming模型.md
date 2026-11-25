---
title: [AIC-501] AI 结对的 Pair Programming 模型：Driver/Navigator 角色翻转
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-501：AI 结对的 Pair Programming 模型

**答**:
- 传统 pair = Driver（写码）+ Navigator（审查/指导）；AI 结对的角色翻转：**人 = Navigator（意图/审查），AI = Driver（写码执行）**——人描述意图、AI 生成、人审查/修正——"人审查 AI 代码"而非"人写代码"。
- 三种 AI 结对模式：1) **Chat**（对话式——Copilot Chat/Cursor Chat——一问一答逐步迭代；2) **Inline**（补全式——Copilot inline——AI 在光标处预测代码——Tab 接受；3) **Agent**（自主执行——Devin/Cursor Composer——AI 自主完成多文件变更（人给任务、AI 执行、人审查 diff）；模式的适用：Inline = 高频小补全、Chat = 逻辑讨论、Agent = 大范围重构。
- 人审的效率瓶颈：AI 生成速度 >> 人审查速度（审查成为瓶颈——AI 产出 100 行/秒 vs 人读 10 行/秒）——解决：1) 减小 diff（AI 只生成必要变更——最小 diff 原则）；2) 信任分级（核心逻辑逐行审、boilerplate 批量审——审查的粒度分级）；3) 测试驱动（AI 生成 + 测试验证——人审测试而非实现——"通过测试即可信"的简化审查）。
- 追问钩子：为什么「人从 Driver 变 Navigator」是 AI 结对的核心转变？——传统 pair = 人写码+人审查（上下文在同一脑中）；AI pair = AI 写码+人审查（上下文分裂：AI 有代码上下文、人有业务上下文——审查的焦点是"AI 是否理解了意图"而非"代码是否正确"——审查的范式从"逐行验证"变"意图验证"）。

```typescript
// AI 结对的工程实践
// 1) Inline 模式（高频补全）
// 输入：function validateEmail(  → AI 补全 → Tab 接受
// 效率：高频高频——光标处预测（不切换上下文）
// 2) Chat 模式（逻辑讨论）
// "这个分页逻辑有没有 N+1 问题？" → AI 分析 → 人决定
// 3) Agent 模式（大变更）
// "把所有 class component 重构为 hooks" → AI 扫描+修改+运行测试 → 人审 diff
// 效率模型
const pairEfficiency = {
  inline: { aiLatency: '100ms', humanReview: 'scan', bestFor: 'boilerplate' },
  chat: { aiLatency: '2s', humanReview: 'read', bestFor: 'logic' },
  agent: { aiLatency: '30s', humanReview: 'diff', bestFor: 'refactor' },
};
```
