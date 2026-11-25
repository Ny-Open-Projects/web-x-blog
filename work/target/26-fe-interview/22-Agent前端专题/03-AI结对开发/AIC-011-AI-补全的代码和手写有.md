---
title: [AIC-011] AI 补全的代码和手写代码混在一起，团队怎么知道 AI 产出的占比与质量差异？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-011：AI 补全的代码和手写代码混在一起，团队怎么知道 AI 产出的占比与质量差异？
**答**：
- 采集层：企业版工具（Copilot Business API、Cursor Teams 后台）能拿到接受率（accept rate）、补全次数、Chat 使用量等遥测指标。
- 度量口径：单看接受率会失真（接受 5 行垃圾也算），更实用的是「接受后存活率」——被接受的补全在一周内未被删除/重写的比例。
- 质量差异不能靠占比推，要靠产出对比：同任务量下的 PR 数、变更行数、bug 率（缺陷回溯时打标是否 AI 辅助产出）。
- 注意反指标：AI 让变更行数暴涨不代表效率涨，可能引入冗余代码；要看「每需求交付周期」类端到端指标。
- 追问钩子：能说出「度量是为了改进流程而非考核个人」的团队会更容易落地（避免工程师关掉指标刷好看）。

```typescript
// 简化的补全遥测上报：接受率 + 存活率埋点（工具侧数据经企业后台获取，此处为自建示意）
interface CompletionEvent {
  userId: string;         // 脱敏后的用户 id
  ts: number;
  suggested: boolean;     // 是否给出建议
  accepted: boolean;      // 是否被接受
  lines: number;          // 接受行数
}

interface SurvivalSample {
  userId: string;
  commitSha: string;
  aliveAfter7d: boolean;  // 7 天后 diff 仍存在（未被重写）
}

// 指标计算
const acceptRate = (evts: CompletionEvent[]) =>
  evts.filter(e => e.suggested).length
    ? evts.filter(e => e.accepted).length / evts.filter(e => e.suggested).length
    : 0;
const survivalRate = (s: SurvivalSample[]) =>
  s.length ? s.filter(x => x.aliveAfter7d).length / s.length : 0;
```
