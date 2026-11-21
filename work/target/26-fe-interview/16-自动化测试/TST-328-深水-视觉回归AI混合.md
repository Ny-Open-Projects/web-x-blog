---
title: [TST-328] 视觉回归「规则 + AI」混合判定的完整流水线？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-328：视觉回归「规则 + AI」混合判定的完整流水线？
**答**：
- 第一层确定性：像素 diff < 阈值 → pass（99% 用例到此结束，零成本）。
- 第二层规则：diff 命中已知动态模式（时间/轮播位）→ 自动 mask 重比对。
- 第三层 AI：剩余 diff 喂 VLM 分类（回归/可接受/噪声），高置信自动判，低置信转人工。
- 反馈闭环：人工判定样本回写 AI 提示词与 mask 配置。

```javascript
async function visualGate(baseline, actual) {
  const ratio = await pixelDiffRatio(baseline, actual);
  if (ratio < 0.005) return 'pass';
  const masked = await autoMask(baseline, actual);
  if (await pixelDiffRatio(masked.b, masked.a) < 0.005) return 'pass';
  return aiClassify(diffImage, { confidence: 0.8 }) ?? 'human-review';
}
r
```
