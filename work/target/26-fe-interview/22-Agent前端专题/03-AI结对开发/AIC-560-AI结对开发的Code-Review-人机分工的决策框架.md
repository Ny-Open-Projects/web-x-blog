---
title: [AIC-560] AI 代码审查的人机分工决策框架
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-560：人机分工决策框架

**答**:
- AI 代码审查的人机分工：1) **AI 擅长**（机械检查：lint/类型/API 幻觉/规范一致性/重复代码检测——规则可枚举的检查 RBL-507 三层防线）；2) **人擅长**（意图验证/业务逻辑/架构决策/安全审计——需要领域知识和判断力的检查 RBL-532 检查点）；3) **分工决策**：机械检查 → AI 自动化（零人工成本）；意图/架构 → 人工（不可自动化）；边界（复杂逻辑）→ AI 辅助 + 人确认；4) **人机分工的框架**：AI 做第一遍（机械检查——筛掉 80% 的问题）→ 人做第二遍（只看 AI 标记为"需要人工"的项目——聚焦意图和架构）。
- 人机分工的效率：AI 第一遍筛掉机械问题 → 人只看逻辑问题（审查时间减 60%——RBL-944 效率叙事）；AI 无法完全替代人的原因：意图理解（AI 不知道业务上下文）、架构权衡（AI 不知道团队历史决策）、安全直觉（AI 只能模式匹配——人的安全直觉超越模式）。
- 追问钩子：为什么「AI 先筛、人后审」比「人直接审」效率更高？——人直接审 100 行：先花 30% 时间检查格式/lint/类型（机械问题——AI 5 秒完成）；AI 先筛：机械问题已修 → 人只看逻辑/意图（审 70% 的内容——节省 30%）；「AI 筛的边际价值」：AI 筛掉的是"人不需要看的"（机械问题）——人只审"AI 不能判断的"（意图/架构/安全直觉）——分工的核心 = 各自做擅长的事（RBL-522 团队规范的流水线哲学：AI 生成 → AI 审 → 人审逻辑）。

```typescript
// 人机分工的审查流水线
async function hybridReview(code, { aiReviewer, humanRequired }) {
  // Phase 1: AI 机械检查
  const aiResults = await aiReviewer(code);
  const mechanicalIssues = aiResults.filter(i => i.type === 'mechanical');
  const humanNeeded = aiResults.filter(i => i.type === 'needs-human');
  // 2) AI 自动修复机械问题
  const fixed = await autoFix(mechanicalIssues);
  // 3) 人只审需要人的部分
  if (humanNeeded.length > 0 || humanRequired) {
    return { humanReview: { items: humanNeeded, autoFixed: fixed.length },
      verdict: 'needs-human-review' };
  }
  return { verdict: 'auto-approved', autoFixed: fixed.length };
}
```
