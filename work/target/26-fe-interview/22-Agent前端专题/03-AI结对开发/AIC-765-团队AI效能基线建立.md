---
title: [AIC-765] 团队 AI 效能基线如何建立与校准
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-765：团队 AI 效能基线如何建立与校准

**答**：
- 结论先行：效能基线 = 引入 AI 前的「历史水位」，没有它就无法回答「AI 到底带来多少提升」；基线要按任务类型分层建立，因为不同任务的天然周期差异巨大。
- 建立方法：1) 取 AI 引入前 4-8 周的稳定期数据；2) 按任务类型/复杂度分层取 P50；3) 记录外部干扰因素（大促、版本发布）；4) 基线版本化，业务剧变时重设。
- 校准：基线不是一次性工作，需定期用「无 AI 对照组」校准，防止基线随团队技能提升自然漂移而被误算成 AI 功劳。
- 追问钩子：为什么基线要按任务类型分层？——把「改 bug」和「写新功能」混在一起算均值，会被结构变化污染，看不出真实提升。

```javascript
// 分层基线：按任务类型取 P50
function buildBaseline(history) {
  const groups = {};
  history.forEach(h => (groups[h.type] ??= []).push(h.cycleDays));
  const out = {};
  for (const [type, vals] of Object.entries(groups)) {
    const s = [...vals].sort((a, b) => a - b);
    out[type] = s[Math.floor((s.length - 1) * 0.5)]; // P50
  }
  return out;
}
const base = buildBaseline([
  { type: 'bugfix', cycleDays: 2 }, { type: 'bugfix', cycleDays: 4 },
  { type: 'feature', cycleDays: 10 }, { type: 'feature', cycleDays: 14 },
]);
console.log(base); // { bugfix:4, feature:14 }（取上中位数）
```
