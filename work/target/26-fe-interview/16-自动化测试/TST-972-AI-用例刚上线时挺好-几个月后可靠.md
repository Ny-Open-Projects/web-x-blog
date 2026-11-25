---
title: [TST-972] AI 用例刚上线时挺好，几个月后可靠性悄悄下滑，怎么监控这种「漂移」？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-972：AI 用例刚上线时挺好，几个月后可靠性悄悄下滑，怎么监控这种「漂移」？
**答**：
- 结论：建立「可靠性时间序列」——按周记录 flake 率、失效比例、断言有效率，设置基线 + 阈值，连续两周恶化即告警。
- 做法：每次代码变更后重跑 AI 用例集，把存活率与检出率打点；与上线初期基线对比，而非与绝对阈值比。
- 归因：漂移常因业务代码演进使 AI 用例假设失效，需定期「再生成 + 人工复核」。
- 追问钩子：某周 flake 率从 2% 涨到 7%，但业务代码没大改，你怎么判断是 AI 用例老化还是测试环境变了？

```javascript
function detectDrift(weeklyStats, baseline, threshold = 0.03) {
  const alerts = [];
  for (const w of weeklyStats) {
    const deltaFlake = w.flakeRate - baseline.flakeRate;
    const deltaSurvival = baseline.survival - w.survival;
    if (deltaFlake > threshold || deltaSurvival > threshold)
      alerts.push({ week: w.week, deltaFlake: +deltaFlake.toFixed(2),
        deltaSurvival: +deltaSurvival.toFixed(2) });
  }
  return alerts;
}
console.log(detectDrift([
  { week: 'W1', flakeRate: 0.02, survival: 0.95 },
  { week: 'W2', flakeRate: 0.07, survival: 0.88 },
], { flakeRate: 0.02, survival: 0.95 }));
// [{ week:'W2', deltaFlake:0.05, deltaSurvival:0.07 }] → 触发再生成
```
