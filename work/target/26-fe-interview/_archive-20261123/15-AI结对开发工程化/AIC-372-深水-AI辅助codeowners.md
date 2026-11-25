---
title: [AIC-372] 如何用 AI 动态维护 CODEOWNERS（按变更内容智能路由评审人）？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-372：如何用 AI 动态维护 CODEOWNERS（按变更内容智能路由评审人）？
**答**：
- 静态为底：CODEOWNERS 目录级规则是基础，AI 只做补充路由建议。
- 智能路由：AI 按 diff 内容匹配「最近在此领域活跃且有相关知识的评审者」输出建议。
- 负载均衡：路由建议纳入评审者当前负载（待评审数），避免压到专家。
- 路由校准：评审转派记录回流，AI 建议被转派率作为路由质量指标持续优化。

```javascript
async function routeReviewers(pr: PR) {
  const staticOwners = codeowners(pr.files);
  const smart = await aiSuggest(pr.diff, { candidates: activeExperts(pr.files),
    load: currentReviewLoad(), history: prTransferStats() });
  return dedupe([staticOwners, smart]).slice(0, 3); // 静态优先
}
r
```
