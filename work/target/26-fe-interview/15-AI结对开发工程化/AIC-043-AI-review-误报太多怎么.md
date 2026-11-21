---
title: [AIC-043] AI Review 误报太多把工程师搞烦了怎么办？误报治理有哪些具体手段？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-043：AI Review 误报太多把工程师搞烦了怎么办？误报治理有哪些具体手段？
**答**：
- 先定北极星指标：意见采纳率（人工点了「有用」的比例）。低于 20~30% 时工程师会开始无视 AI 意见，门禁就名存实亡。
- 手段一：置信度过滤——只展示高置信意见，低置信进「折叠区」；宁缺毋滥。
- 手段二：误报回流——每条被标记「误报」的意见记录下来，分析共性后改 prompt（加反例、加上下文、收窄清单项）。
- 手段三：按路径降级——对生成类目录（如 ai-generated/、原型代码）降阈值，对核心目录（支付、权限）提阈值。
- 手段四：消重与聚焦——同一问题在多个文件重复报只报一次；每 PR 意见总数设上限（如 10 条），超出自动收敛为摘要。
- 追问钩子：治理的终点不是 0 误报，而是「意见信噪比」稳定在团队愿意读的水平。

```javascript
// 意见过滤与采纳率统计
function filterFindings(findings, { minConfidence = 0.7, maxCount = 10 } = {}) {
  const passed = findings
    .filter(f => f.confidence >= minConfidence)
    .sort((a, b) => b.confidence - a.confidence);
  const dedup = new Map();
  for (const f of passed) {
    const key = f.issue.split(' ').slice(0, 8).join('|'); // 相似问题只留一条
    if (!dedup.has(key)) dedup.set(key, f);
  }
  return [...dedup.values()].slice(0, maxCount);
}
function adoptionRate(findings, thumbsUp) { return thumbsUp / findings.length; }
```
