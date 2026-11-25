---
title: [ENG-211] 前端 DevEx（开发者体验）度量怎么设计？哪些指标有效哪些是虚荣指标？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-211：DevEx 度量怎么设计？
**答**：
- 有效指标来自三个维度：反馈回路（构建时长/热更新时长/CI 时长/失败重试率）、认知负担（新人上手时长/文档完备度/工具命令数量）、心流（被打断次数/等待时间总和）——SPACE 框架的工程化落地。
- 量化与定性结合：客观指标（秒表数据）+ 开发者调查（满意度/摩擦点）——只看客观会优化错方向（build 快 2s 但查日志要 10 分钟）。
- 虚荣指标识别：代码行数/提交数/「工具数量」——不反映效率；替代性指标（PR 从提交到合入时长、回滚率）才关联真实效率。
- 改进闭环：度量 → 定位 Top 摩擦点 → 专项改进 → 复测验证——度量本身不产生价值，闭环才有。
- 追问钩子：为什么 CI 时长不是越短越好作为唯一目标——压缩 CI 常牺牲覆盖（跳过重测试）；正确目标是「按风险分级的 CI 时长」——小 PR 快、大 PR 全，而不是全局最短。

```javascript
const devexMetrics = {
  feedback: { buildMs: p95, hmrMs: p95, ciMinutes: p50, retryRate: true },
  cognition: { onboardingDays: 'new-hire survey', docCoverage: true, toolCmds: count },
  flow: { interruptPerDay: 'survey', waitSum: buildWait + ciWait },
  vanity: ['loc', 'commits', 'tool-count'],          // 明确剔除
  loop: 'measure → top-friction → fix → re-measure',
};
```
