---
title: [AIC-884] 跨时区团队接力开发，如何保持 AI 的上下文不断片？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-884：跨时区团队接力开发，如何保持 AI 的上下文不断片？
**答**：
- 问题本质：A 地工程师下班时的 AI 会话上下文，B 地工程师上班时看不到——AI 不记得「昨天为什么选了方案 X 而不是 Y」，导致重复讨论或推翻决策。
- 解法是把**上下文从「会话」升级为「工件（artifact）」**：把决策、约束、待办写进仓库里的文档（ADR 架构决策记录、`DECISIONS.md`、任务看板），而不是留在某个人的 AI 聊天记录里。AI 每次开工先读这些工件作为共享上下文（配合规则文件 AIC-001）。
- 结构化交接：每个任务留「交接卡」——当前状态、已完成、下一步、已知坑、相关决策链接；提交信息带结构化 trailer（taskId/decision）。B 地的人（和 AI）能快速恢复现场。
- 会话要可持久化与可检索：AI 会话导出为可搜索的记录并关联到任务/PR；但要脱敏且控制访问——上下文里可能有敏感讨论。
- 追问钩子：能说出「上下文要沉淀为仓库里的工件（ADR/交接卡），不依赖个人会话」的候选人，把 AI 协作从个人工具提升到团队工程实践。

```typescript
type Handoff = { taskId: string; from: string; status: string;
  done: string[]; next: string[]; knownPits: string[]; decisions: string[]; updatedAt: number };

function handoffCard(h: Handoff) {
  // 生成结构化交接卡，写入仓库 docs/handoffs/{taskId}.md
  // AI 每次开始任务时读此文件作为共享上下文
  return [
    `# 交接卡：${h.taskId}`,
    `负责人：${h.from} ｜ 状态：${h.status} ｜ 更新：${new Date(h.updatedAt).toISOString()}`,
    '', '## 已完成', ...h.done.map(x => '- ' + x),
    '', '## 下一步', ...h.next.map(x => '- ' + x),
    '', '## 已知坑', ...h.knownPits.map(x => '- ' + x),
    '', '## 相关决策', ...h.decisions.map(x => '- ' + x),
  ].join('\n');
}
console.log(handoffCard({ taskId:'T-42', from:'Alice(UTC+8)', status:'in-progress',
  done:['数据层完成'], next:['补前端表单'], knownPits:['旧接口返回 null'],
  decisions:['ADR-007 用乐观更新'], updatedAt:Date.now() }));
// B 地同事的 AI 读这份卡即可无缝接力，不依赖 Alice 的会话
```
