---
title: [NODE-300] trace 与 SSR 首屏联合分析？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-300：trace 与 SSR 首屏联合分析？
**答**:
- 联合分析场景："LCP P75 慢 300ms"→ RUM 定位慢页面/档位 → 按关联 traceId 拉 SSR trace → 树内看"数据预取 span 占 800ms"→ 下游归因。
- SSR trace 的关键 span：数据 loader（getServerSideProps 类）、renderToString、HTML 传输——每段独立计时才能定位"慢在数据还是渲染"。
- 自动关联：RUM 上报带 traceId（NODE-295）+ 后端 trace 存 traceId → 平台按 traceId join。
- 输出物：首屏耗时瀑布图（前端指标 + 后端 span 树对齐同一时间轴）——一次看全"网络+渲染+数据"。

```javascript
// 联合查询（平台侧伪代码）
async function analyzeSlowLCP(page, hour) {
  const rums = await rum.query({ page, hour, metric: 'LCP', percentile: 75, slow: true });
  const traceIds = rums.map(r => r.traceId).filter(Boolean);
  const traces = await traceStore.batchGet(traceIds);
  const breakdown = traces.map(t => ({
    dataFetch: spanDuration(t, 'loader'),       // 数据预取
    render: spanDuration(t, 'renderToString'),  // 渲染
    transfer: spanDuration(t, 'http.send'),     // 传输
  }));
  return topContributor(breakdown);             // 归因最大段 → 转优化任务
}
```
