---
title: [TST-564] AI 辅助视觉回归测试的判定框架
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-564：AI 辅助视觉回归测试的判定框架

**答**：
- 结论：像素 diff 给「哪里有差异」，AI 给「差异是否语义重要」——先像素/结构过滤掉抗锯齿与动态数据噪声，再由视觉模型对有效差异分类（文案/布局/样式/无关）。
- 做法：mask 动态区域（时间/广告）→ 像素差超阈值才送 AI → AI 输出差异类型与严重度 → 高严重度阻塞、低严重度进审核队列；持续用人工反馈微调阈值与模型。
- 追问钩子：AI 判定也会错（把真实 bug 判成噪声）怎么办？——保留人工复核通道 + 定期抽样审计 AI 判定，用「漏判率」作为模型质量指标持续监控。

```javascript
// 视觉判定：像素层过滤 + AI 语义分类 + 严重度路由
function visualVerdict(pixelDiff, aiClass) {
  if (pixelDiff.ratio < 0.001) return { action: 'pass', why: '差异低于噪声阈值' };
  const severityMap = { 'text-change': 'high', 'layout-shift': 'high', 'color-drift': 'low', 'dynamic-data': 'ignore' };
  const severity = severityMap[aiClass] || 'medium';
  return { action: severity === 'ignore' ? 'pass' : severity === 'high' ? 'block' : 'review',
    severity, why: `AI 分类=${aiClass}` };
}
console.log(visualVerdict({ ratio: 0.02 }, 'text-change')); // block
console.log(visualVerdict({ ratio: 0.0005 }, 'color-drift')); // pass
```
