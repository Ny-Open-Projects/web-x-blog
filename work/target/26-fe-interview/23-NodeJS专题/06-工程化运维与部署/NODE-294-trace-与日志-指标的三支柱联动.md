---
title: [NODE-294] trace 与日志、指标的三支柱联动？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-294：trace 与日志、指标的三支柱联动？
**答**:
- 三支柱关系：指标（聚合告警，低成本低基数）→ 定位到时间段；trace（单请求全景）→ 定位到具体链路；日志（细节）→ 定位到具体原因。联动靠 traceId 串联。
- 日志侧：每条日志带 traceId/spanId（ALS 自动 NODE-292）→ 从 trace 跳日志、从日志跳 trace。
- 指标侧：span 属性转指标维度（route/status）——RED 指标（Rate/Errors/Duration）按 route 聚合。
- 实践：告警规则先看指标 → 附带该时段慢 trace 样例 → 一键跳转日志检索。

```javascript
// 日志自动带 trace（OTel + pino 集成）
const log = pino({
  mixin() {
    const span = trace.getActiveSpan();
    const ctx = span?.spanContext();
    return ctx ? { traceId: ctx.traceId, spanId: ctx.spanId } : {};
  },
});
// 指标（span → RED）
app.use((ctx, next) => {
  const end = histogram.startTimer();
  await next();
  end({ route: ctx.path, status: ctx.status });        // 低基数维度
});
// 告警 → trace 联动：alert 带 trace 检索链接（traceId from error log）
```
