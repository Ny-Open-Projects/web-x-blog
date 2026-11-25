---
title: [AGT-870] 实时链路（WS/SSE）问题 AI 辅助排查：如何把时序数据变成 AI 可用的证据？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-870：实时链路（WS/SSE）问题 AI 辅助排查：如何把时序数据变成 AI 可用的证据

**答**：
- 证据结构化：WS 排查的关键是时序证据（消息序列/间隔/重连点），工具先把流量录制成结构化时间线（带 seq/方向/延迟），AI 消费时间线而不是原始日志——"重连前最后 3 条消息"这类模式 AI 才能识别。
- 模式库驱动：常见故障模式（慢消费者积压/心跳丢失/seq gap/乱序）先程序化检测（快且确定），AI 负责"模式库没有的异常"的开放分析——确定问题程序管，未知问题 AI 管。
- 输出可行动：AI 结论必须附"验证方法"（复现步骤/抓包位置），不接受不可验证的断言。

```javascript
async function wsDiagnose(session) {
  const timeline = recordToTimeline(session.frames);  // 结构化时序
  const known = PATTERNS.detect(timeline);            // 程序先检
  if (known) return { cause: known, fix: FIXES[known] };
  return llm.analyze(timeline, {
    require: '结论附验证步骤与抓包位置',              // 可验证性
    forbid: '不得给出无法验证的断言',
  });
}
```

