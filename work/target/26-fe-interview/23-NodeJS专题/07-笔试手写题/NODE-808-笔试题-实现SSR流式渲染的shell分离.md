---
title: [NODE-808] 笔试题——实现 SSR 流式渲染（shell 先行 + Suspense 分段）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-808：手写流式 SSR

**需求与边界**：
- 需求：React 流式 SSR（SCN-NODE-756 延伸）——① shell 先行（onShellReady——TTFB 提前，SCN-NODE-756）；② Suspense 边界分段（慢组件后补流式插入）；③ 超时降级（慢 Suspense 降级 fallback——SCN-NODE-756 降级链）；④ 客户端断开中断渲染（SCN-NODE-744 取消传播）。
- 边界：① 分段插入的语法（React 流式注释标记——客户端 hydrate 兼容）；② shell 后错误的处理（已发 shell 无法改状态码——错误标记注入）；③ 渲染预算（shell < 50ms——预算分解）。

**答**：
```javascript
app.get('/page', (req, res) => {
  const signal = AbortSignal.any([clientGone(req), AbortSignal.timeout(200)]);   // 双源（SCN-NODE-744）
  const { pipe } = renderToPipeableStream(<App />, {
    onShellReady() {                                   // shell 先行（TTFB）
      res.setHeader('Content-Type', 'text/html');
      pipe(res);
    },
    onShellError(e) { res.status(500).end(csrFallback()); },   // shell 失败 → CSR（SCN-NODE-756）
    onError(e, info) {                                 // 分段错误：Suspense fallback 降级
      if (info?.componentStack) telemetry.push({ type: 'SSR_SEGMENT_ERR' });
      else if (!res.headersSent) res.status(500);
    },
  });
  req.on('close', () => abortRender(signal));          // 客户端断开中断（SCN-NODE-744）
});
// shell 预算 < 50ms（SCN-NODE-756 200ms 总预算的分解）
```

**评分点**:
- shell 先行 TTFB + Suspense 分段（流式 SSR 核心）。
- onShellError CSR 兜底（SCN-NODE-756 降级链）。
- 客户端断开取消渲染（SCN-NODE-744 取消传播）。
- shell 预算分解（总预算分层）。
