---
title: [AIC-548] AI 生成的 PR 自动审查
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-548：AI 生成 PR 的自动审查

**答**:
- AI 生成 PR 的自动审查流水线（RBL-536 门禁的 PR 级）：1) **自动描述生成**（AI 生成 PR 描述——变更摘要/影响面/测试计划——PR 描述的 AI 化（人不需要手写 PR 描述）；2) **自动审查 comment**（AI 审查自己的 diff——标注潜在问题/边界条件/安全风险（AI 自审 → 人审参考 RBL-504）；3) **影响面标注**（哪些文件变更/哪些路由受影响/缓存是否失效——RBL-778 依赖图的 PR 版；4) **风险分级标注**（T0/T1/T2 标签——RBL-505 的 PR 标签化）。
- 自动审查的可信度：AI 自审 ≠ 独立审查（AI 审查 AI 的代码——"AI 验证 AI"的循环 RBL-504）；解法：AI 自审的 comment 标注为 "AI-generated review"——人参考但不依赖；「AI 自审 = 辅助信息而非最终裁决」。
- 追问钩子：为什么「AI 自动生成 PR 描述」能提升审查效率？——传统 PR 描述 = 人手写（遗漏影响面/没有测试计划——审查者需要自己探索）；AI 描述 = 全面的变更摘要（包含人可能遗漏的维度——缓存影响/安全考虑/性能影响）；「AI 描述 = 审查者的阅读指南」：审查者看到结构化的变更分析——审查效率提升（不用自己挖掘影响面）；但 AI 描述的可信度 = 辅助（人验证描述是否准确——AI 可能遗漏或误判）。

```typescript
// AI 生成 PR 描述与审查
interface PRReview {
  description: string;
  riskLevel: 'T0'|'T1'|'T2'|'T3';
  affectedRoutes: string[];
  cacheImpact: boolean;
  securityNotes: string[];
  testPlan: string;
}
async function aiReviewPR(diff: string, prMeta: { title: string; files: string[] }): Promise<PRReview> {
  const prompt = `Review this PR diff and generate:
1. Summary of changes
2. Risk level (T0-T3 per security sensitivity)
3. Affected routes
4. Cache invalidation needed?
5. Security concerns
6. Test plan

Diff: ${diff}`;
  const review = await llm.generate(prompt);
  return parseReview(review);
}
// CI 集成：PR 创建时自动添加 AI review comment
// github.postComment(pr.number, formatReview(aiReview));
```
