---
title: [AIC-257] 每个 PR 都跑 AI 评审，CI 成本如何控制？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-257：每个 PR 都跑 AI 评审，CI 成本如何控制？
**答**：
- 触发策略：风险分级预筛——低风险 PR 只做轻量评审（小模型/摘要级），中高风险才全量评审。
- 增量评审：只在新增 commit 上评审，历史已评审 diff 引用结论不重跑。
- 缓存：相同文件内容的重复 PR（rebase/cherry-pick）命中缓存。
- 预算熔断：单仓库日评审预算超限自动降级为轻量模式并告警，而不是停摆。

```javascript
async function reviewPr(pr: PR) {
  const r = riskScore(pr);
  if (r.level === 'low' && cacheHit(pr.headSha)) return cached(pr.headSha);
  const model = r.level === 'high' ? 'strong-max' : 'fast-mini';
  return budgetGuard(repo, () => call(model, pr.diff), {
    fallback: 'light-review', onExceed: 'alert',
  });
}
r
```
