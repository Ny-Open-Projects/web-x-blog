---
title: [TST-763] AI 分析混沌实验失败日志——根因推荐的边界
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-763：AI 分析混沌实验失败日志——根因推荐的边界

**答**：
- 结论：AI 把海量日志聚合成「可疑根因候选」很高效，但最终根因要人确认，因为混沌实验常有多重并发故障，AI 易把相关性当因果。
- 输入要给时间线对齐的日志 + 注入事件标记，让 AI 理解「哪个异常在注入之后」。
- 推荐必须附证据链（日志片段 + 时间点），无证据的推测降级为「待验证假设」。
- 追问钩子：AI 连续多次推荐同一个错误根因，如何识别它在“钻牛角尖”？

```javascript
// 日志时间线对齐注入事件，标记因果方向
function alignTimeline(logs, injectAt) {
  return logs.map(l => ({
    ...l,
    phase: l.at < injectAt ? 'before' : 'after',
    suspicious: l.at >= injectAt && l.level === 'ERROR',
  }));
}
console.log(alignTimeline([
  { at: 100, level: 'ERROR', msg: 'old' },
  { at: 300, level: 'ERROR', msg: 'new' },
], 200));
```
