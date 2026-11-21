---
title: [AIC-260] 发布前的 AI 检查清单（release readiness）应包含哪些自动化项？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-260：发布前的 AI 检查清单（release readiness）应包含哪些自动化项？
**答**：
- 变更归集：本版本所有 PR 的风险分汇总，高危项清单与规避方案。
- 回归信号：新增测试通过率、变异分数变化、flaky 用例数趋势。
- 兼容性检查：API 变更（对外接口/埋点/存储结构）是否走审批、灰度与回滚预案是否齐全。
- AI 输出「发布建议书」：go / go-with-risk（列条件）/ no-go（列阻塞项），决策仍在人。

```javascript
async function releaseChecklist(version: string) {
  const prs = await prsIn(version);
  const risks = prs.map(riskScore).filter(r => r.level === 'high');
  const go = risks.length === 0 && flakyTrend() < 0.02 && breakingChangesApproved();
  return { verdict: go ? 'go' : risks.length ? 'go-with-risk' : 'no-go',
           blockers: risks, rollbackPlan: await requireRollback(version) };
}
r
```
