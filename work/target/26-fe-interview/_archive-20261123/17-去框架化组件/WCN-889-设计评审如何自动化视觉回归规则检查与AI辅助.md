---
title: [WCN-889] 设计评审如何「自动化」：视觉回归 + 规则检查 + AI 辅助？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-889：设计评审如何「自动化」：视觉回归 + 规则检查 + AI 辅助？

**答**：
- 结论先行：自动化评审的目标是「把机器能判的交给机器，把人的时间留给设计取舍」——视觉回归查像素差异、规则检查查规范符合度、AI 辅助查可疑问题，三者分层协作。
- 视觉回归：用 Storybook/Chromatic 等对每个组件的多状态（默认/hover/disabled/暗色/RTL）截图，与基线比对，差异高亮供人确认——注意「语义优先」，减少无意义像素快照数量（只测关键状态）。
- 规则检查：自动检测 token 裸值、间距是否符合刻度、圆角/阴影是否用规范值、a11y 对比度——这些是确定性规则，机器判定可靠。
- AI 辅助：用视觉模型判断「这个布局是否明显错位」「这个文案是否溢出」「与设计稿的整体相似度」，给出提示而非硬性结论（AI 有误判，需人复核）。
- 闭环：评审结果进看板，差异需人工 approve 才能更新基线；自动评审不通过则 CI 阻断，倒逼贡献者自查。
- 追问钩子：面试官会问「视觉回归误报多怎么办」——答：设置合理的差异阈值、固定渲染环境（字体/DPR/时区）、只快照稳定状态（禁用动画/随机数据），并把「语义等价」的差异（如抗锯齿）加入白名单。

```javascript
// 自动化设计评审：规则检查 + 视觉差异阈值判定
function autoReview({ bareValues, visualDiff, a11yIssues }, { threshold = 0.02 } = {}) {
  const problems = [];
  if (bareValues.length) problems.push(`发现 ${bareValues.length} 处 token 裸值`);
  if (a11yIssues.length) problems.push(`${a11yIssues.length} 处 a11y 问题`);
  if (visualDiff > threshold) problems.push(`视觉差异 ${(visualDiff * 100).toFixed(1)}% 超阈值`);
  return { passed: problems.length === 0, problems };
}
console.log(autoReview({ bareValues: ['#fff'], visualDiff: 0.01, a11yIssues: [] }));
console.log(autoReview({ bareValues: [], visualDiff: 0.08, a11yIssues: [] }));
```
