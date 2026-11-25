---
title: [NODE-367] Node 服务的 SSR 服务端性能治理如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-367：SSR 服务端性能治理
**答**:
- 成本模型：每次渲染 = CPU（组件树执行）+ 数据获取（下游 RTT）+ 序列化；峰值 QPS 决定容量（ARC-446 前端容量模型的服务端版本）。治理主线：少渲染（缓存）+ 快渲染（并行取数）+ 稳渲染（降级）。
- 缓存分层：整页缓存（URL + 关键 cookie 维度，TTL 短）、组件级缓存（ARC-315）、数据缓存（渲染前 fetch 缓存复用）、HTML 微缓存（1~5s 窗口削峰——牺牲一点时效换容量）。
- 流式渲染：Suspense 分段 flush，首段尽早输出（TTFB 改善）；回填顺序与 hydration 对齐。
- 降级链：渲染超时（> 800ms）→ 降级 CSR（返回壳 + 客户端渲染）或缓存旧版 HTML；下游挂 → 组件级兜底（ARC-299）。
- 资源隔离：SSR 进程与 API 进程分部署（渲染 CPU 尖刺不影响接口 P95）；渲染池大小与事件循环延迟监控联动（NODE-350）。
```javascript
// SSR 渲染预算控制
async function renderWithBudget(ctx) {
  return Promise.race([
    renderApp(ctx),                                              // 正常渲染
    renderTimeout(800).then(() => renderCSRShell(ctx))            // 超时降级壳
  ]);
}
// 微缓存：key = url + cookieHash(用户维度)；TTL 3s + stale-while-revalidate
```
