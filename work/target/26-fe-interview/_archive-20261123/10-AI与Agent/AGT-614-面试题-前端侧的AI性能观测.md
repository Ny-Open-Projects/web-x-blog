---
title: [AGT-614] 前端要采集哪些 AI 特有性能指标（与常规 Web Vitals 的互补）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-614：前端要采集哪些 AI 特有性能指标（与常规 Web Vitals 的互补）

**答**：
- AI 特有前端指标：TTFT 感知（用户看到首字）、流速率感知（token/s 渲染 vs 网络）、渲染卡顿（流式期间长任务数）、输入到提交延迟（输入框卡顿）、错误恢复时长（从报错到用户重试成功）。
- 与 Web Vitals 互补而非重复：LCP/INP 照常采集，AI 指标挂在 turn 维度（同一 traceId 关联），这样能回答"是页面慢还是模型慢"。
- 采集要轻：performance.observe + turn 事件埋点，流式高频事件不逐条上报（本地聚合轮次结束时一次上报）。

```javascript
function collectTurnPerf(turn) {
  return {
    webVitals: { inp: lastINP(), lcp: lastLCP() },       // 常规照采
    ai: {
      ttftPerceived: turn.firstPaintDelta,               // 用户看到首字
      renderStalls: turn.longTasksDuringStream,          // 流式卡顿
      inputLag: turn.inputToSubmitMs,
      recoveryMs: turn.errToRetryOkMs,
    },
  };  // 同一 traceId，可回答"页面慢还是模型慢"
}
```

