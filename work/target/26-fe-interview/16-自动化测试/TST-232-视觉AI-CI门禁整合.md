---
title: [TST-232] 视觉回归如何在 CI 门禁里定位（阻塞还是建议）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-232：视觉回归如何在 CI 门禁里定位（阻塞还是建议）？
**答**：
- 组件级 diff：阻塞（粒度小、可归因、误报可控）。
- 整页/AI 分类：建议级（附 diff 图评论到 PR），人确认后才更新基线。
- 基线更新本身要走 PR——「接受新样式」是显式决策，禁止 CI 自动改基线。
- 紧急逃生：hotfix 场景可用「跳过视觉门禁」标签，但记录审计。

```javascript
# PR 门禁策略
visual-gate:
  component-level: blocking
  full-page: comment-only
  baseline-update: requires-human-approval
r
```
