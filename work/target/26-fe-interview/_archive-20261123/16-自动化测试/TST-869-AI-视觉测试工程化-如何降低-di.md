---
title: [TST-869] AI 视觉测试工程化：如何降低 diff 误报率并沉淀规则？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-869：AI 视觉测试工程化：如何降低 diff 误报率并沉淀规则？
**答**：
- 结论：AI 视觉判定要做「分层过滤」——先规则化忽略动态区域（时间/动画/广告位），再 AI 判断是否真回归，最后人工抽检反馈闭环。
- 降误报：mask 掉已知动态区域、固定字体/动画/时间、多轮取稳定截图（呼应 TST-231/234）。
- AI 判定：用视觉模型区分「布局崩了」与「合理变化」，输出置信度，高置信自动判定、低置信转人工。
- 规则沉淀：人工裁决结果回流为规则/样本，持续训练，形成「越用越准」的飞轮。
- 追问钩子：AI 把一次真实的配色回归误判为「合理设计调整」放行了，你如何在流程上补上？

```javascript
// AI 视觉判定的置信度路由 + 反馈闭环
function visualVerdict(diff, model) {
  const filtered = diff.regions.filter(r => !isDynamic(r)); // 规则过滤动态区
  if (!filtered.length) return { verdict: 'no-real-diff', source: 'rule' };
  const ai = model.classify(filtered); // { isRegression, confidence }
  if (ai.confidence >= 0.9) return { verdict: ai.isRegression ? 'regression' : 'ok', source: 'ai' };
  return { verdict: 'needs-human', source: 'low-confidence', regions: filtered };
}
function isDynamic(region) { return /time|ad|animation|avatar/.test(region.name); }
// 人工裁决后 -> 把 (filtered, 结论) 作为样本回流训练 model
```
