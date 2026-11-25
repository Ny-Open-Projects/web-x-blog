---
title: [AIC-259] AI 评审的「采纳率」怎么定义和统计才不掺水？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-259：AI 评审的「采纳率」怎么定义和统计才不掺水？
**答**：
- 采纳定义要严格：评审意见对应的代码在后续 commit 中被修改，且修改与建议语义一致。
- 排除掺水：开发者为了「关闭评论」做的无意义改动、建议本身就错但开发者照做（错误采纳）。
- 对照指标：采纳率 × 建议正确率（抽样人审）→ 有效采纳率才是真指标。
- 分层统计：按严重度/问题类型分别统计，安全类和风格类的采纳率意义完全不同。

```javascript
function adoption(reviews: Review[], commits: Commit[]) {
  const taken = reviews.filter(r =>
    commits.some(c => modifiesAsSuggested(c, r) && isSemanticFix(c, r)));
  const valid = taken.filter(r => humanAudit(r) === 'correct'); // 抽样人审
  return { raw: taken.length / reviews.length, effective: valid.length / reviews.length };
}
r
```
