---
title: [WCN-810] 组件平台的「内部客户满意度」（NPS）怎么度量并真正用来改进？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-810：组件平台的「内部客户满意度」（NPS）怎么度量并真正用来改进？

**答**：
- 结论先行：NPS 不是收集了就算，关键是「低分有人跟、问题能闭环」——度量要嵌入业务方真实触点（接入、提需、排障），而不是年终发一次问卷。
- 触点式收集：在三个时刻埋点——刚接入完（问接入体验）、需求关闭时（问响应质量）、事故复盘后（问兜底是否到位）；每次只问一道题 + 一句开放反馈。
- 计算与拆分：NPS = 推荐者% − 贬损者%；按 BU、按组件、按环节拆分，定位「是谁在哪个环节不满意」，别只看总分。
- 闭环机制：每个贬损者反馈必须有 owner 跟进并在看板显示状态，下轮 NPS 回访验证是否改善；把 NPS 改善纳入平台团队 OKR。
- 追问钩子：面试官会问「NPS 和客观指标冲突怎么办（比如用的人多但评分低）」——答：这正是信号——说明采纳是被 KPI 强推的，体验没跟上，要优先修体验而不是继续推量。

```javascript
// NPS 计算与按维度拆分，定位真实的痛点环节
function nps(scores) { // 0~10
  if (!scores.length) return 0;
  const promoters = scores.filter(s => s >= 9).length;
  const detractors = scores.filter(s => s <= 6).length;
  return Math.round((promoters - detractors) / scores.length * 100);
}
const feedback = {
  onboarding: [9, 10, 8, 3, 6, 9],
  support:    [10, 9, 8, 7, 9],
  incident:   [5, 4, 8, 6],
};
for (const [stage, arr] of Object.entries(feedback)) {
  console.log(`${stage}: NPS ${nps(arr)}`); // onboarding 最低 → 优先优化接入
}
```
