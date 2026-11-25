---
title: [AIC-570] AI 代码审查的团队流程
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-570：AI 代码审查的团队流程

**答**:
- 团队级 AI 代码审查流程：1) **生成阶段**（AI 生成代码 → 开发者审查（RBL-532 检查点）→ 提交 PR（provenance 标注 RBL-942）；2) **CI 阶段**：幻觉检测（RBL-508）→ 规范审计（RBL-523）→ 测试质量（RBL-535）→ 安全扫描（RBL-733）→ 信任路由（RBL-505）；3) **人审阶段**：信任路由决定的审查级别（T0 逐行/T1 测试驱动/T2 抽样/T3 免审）；4) **反馈闭环**（RBL-566：审查反馈 → 规则更新 → AI 改进）。
- 团队流程的落地：1) **PR 模板**（AI 生成的 PR 必须包含：变更摘要/风险等级/测试计划——RBL-548 AI 生成 PR 描述；2) **审批规则**（T0 需要 security reviewer + tech lead 双审；T1 需要 owner 单审；T2/T3 可以 auto-merge RBL-505）；3) **度量看板**（AI 代码的接受率/bug 率/审查时间——RBL-516 度量的团队看板）。
- 追问钩子：为什么「团队级 AI 审查流程」需要「信任路由」（而非固定流程）？——不同类型的 AI 代码风险不同（安全代码 vs 样式代码——审查需求差 10 倍）；固定流程 = 全部全审（安全代码审了但样式代码也审了——效率低）或全部抽审（安全代码漏审——风险高）；「信任路由 = 风险适配」（RBL-505 的动态校准 RBL-551）——按代码风险动态调整审查深度——团队的审查资源有限（按风险分配——最重要的最先审）。

```typescript
// 团队级 AI 审查流水线
async function teamAIReviewProcess(pr: PR, config: TeamConfig) {
  // 1) CI 门禁（RBL-536）
  const gateResult = await aiCodeGate(pr, config);
  if (!gateResult.ok) return { blocked: true, gate: gateResult };
  // 2) 信任路由（RBL-505）
  const route = routeReview(pr, config);
  // 3) 分配 reviewer
  if (route.action === 'manual-review-required') {
    await assignReviewers(pr, route.reviewers);
    await addLabels(pr, [`risk:${route.level}`, 'ai-generated']);
    return { status: 'pending-human-review', route };
  }
  // 4) auto-merge（T3）
  if (route.action === 'auto-merge') {
    await autoMerge(pr);
    return { status: 'auto-merged', route };
  }
  // 5) merge-with-note（T1）
  await mergeWithNote(pr, route.reviewers[0]);
  return { status: 'merged', route };
}
```
