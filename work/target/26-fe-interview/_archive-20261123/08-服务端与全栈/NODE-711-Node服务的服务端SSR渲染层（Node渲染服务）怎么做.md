---
title: [NODE-711] SSR 渲染层（Node 渲染服务）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-711：SSR 渲染层怎么做？
**答**：
- 渲染服务架构：渲染池（V8 isolate 池/worker——SCN-NODE-634 并行）+ 渲染缓存（同 URL 同数据版本缓存——SSR 缓存层）、流式渲染（shell 先行——TTFB 提前）。
- 渲染性能：渲染耗时预算（SSR 渲染 P95 < 200ms——超预算降级 CSR——渲染降级链）；组件级缓存（静态部分缓存——模板缓存）。
- 稳定性：渲染超时（CSR 兜底——SSR 挂了页面仍可用——SPA fallback）、渲染错误隔离（ErrorBoundary SSR 侧——整页不白屏）、内存治理（每次渲染释放——SCN-NODE-672 泄漏检查 SSR 版）。
- 与 BFF 的关系：渲染服务消费 BFF 数据（数据层与渲染层分离——渲染服务不直连业务 DB）。
- 追问钩子：为什么 SSR 渲染服务要有「降级 CSR」通道——SSR 是 Node 进程（可能 OOM/渲染崩溃/数据接口挂），SSR 挂了不能让页面白屏；超预算/失败 → 返回 CSR 壳（客户端渲染兜底）——「SSR 是加速手段不是依赖」——降级让 SSR 故障降级为性能问题而非可用性事故。

```javascript
async function render(req) {
  const cached = renderCache.get(url); if (cached) return cached;
  const signal = timeout(200);                         // 200ms 渲染预算
  try { const html = await renderToString(app, { signal });
    return html;
  } catch { return csrFallback(req); }                 // 降级 CSR（可用性保底）
}
```
