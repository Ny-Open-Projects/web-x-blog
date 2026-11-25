---
title: [NODE-756] 笔试题——实现 SSR 渲染服务（缓存 + 降级 + 超时）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-756：手写 SSR 渲染

**需求与边界**：
- 需求：SSR 渲染服务（SCN-NODE-711）——① 渲染缓存（URL+数据版本键——全维度，SCN-NODE-718）；② 渲染预算（200ms 超时——降级 CSR）；③ 流式渲染（shell 先行——TTFB 提前）；④ 内存治理（每次渲染后检查——泄漏哨兵，SCN-NODE-727 联动）。
- 边界：① 降级 CSR 的标记（响应头——监控 SSR 健康度）；② 渲染错误隔离（ErrorBoundary——部分渲染不整页失败）；③ 缓存的失效（数据版本变更——SCN-FIN-688 删缓存）。

**答**：
```javascript
async function renderPage(req) {
  const key = hash([req.url, req.dataVersion, req.grayBucket]);   // 全维度键（SCN-NODE-718）
  const cached = cache.get(key);
  if (cached) return { html: cached, cached: true };
  const signal = AbortSignal.timeout(200);             // 200ms 渲染预算
  try {
    const stream = renderToPipeableStream(<App data={req.data} />, {
      onShellReady() { stream.pipe(res); },            // 流式（TTFB 提前）
      onError(e) { report({ type: 'SSR_ERROR', err: e }); },   // 组件级隔离
    });
    const html = await waitForStream(stream, signal);  // 预算超时 → 降级
    cache.set(key, html);
    return { html };
  } catch (e) {
    report({ type: 'SSR_DEGRADE', reason: e.name });   // 超时/错误 → 降级 CSR
    res.setHeader('X-SSR', 'DEGRADED');
    return csrFallback(req);                           // CSR 兜底（可用性保底——SCN-NODE-711）
  } finally {
    if (heapGrew()) heapdumpOnce();                    // 泄漏哨兵（SCN-NODE-672 SSR 版）
  }
}
```

**评分点**:
- 全维度缓存键（URL+数据版本+灰度——SCN-NODE-718）。
- 渲染预算 + 流式 shell（TTFB 与超时并存）。
- 降级 CSR 通道（SSR 故障 → 性能问题——SCN-NODE-711）。
- 泄漏哨兵（渲染服务内存治理——SCN-NODE-672 联动）。
