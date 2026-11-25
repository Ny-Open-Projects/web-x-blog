---
title: [NODE-271] SSR 服务的稳定性挑战全景？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-271：SSR 服务的稳定性挑战全景？
**答**：
- SSR 相比纯接口服务的三大风险：请求级内存放大（每请求渲染树+数据）、慢下游拖长渲染（尾部延迟敏感）、CPU 密集（renderToString 是纯 CPU）。
- 防线分层：渲染超时（兜底 CSR/骨架）→ 下游预算（NODE-207 组合取消）→ 渲染缓存（静态段/整页 SWR NODE-345）→ 容量（SSR 帧率预算/队列限流）。
- 全局指标：渲染耗时 P95、降级率（fallback 比例）、事件循环饱和度（SSR 是 CPU 密集，ELU 最敏感）。
- 与框架配合：React 18 流式（NODE-261 Suspense 分段）天然把"慢数据"与"整页失败"解耦——先流骨架再补内容。

```javascript
// SSR 渲染超时兜底
async function ssrHandler(req, res) {
  const signal = AbortSignal.any([AbortSignal.timeout(2000), req.abortSignal]);
  try {
    const { stream } = await renderApp(req, { signal });
    pipeStream(stream, res);                       // 流式：骨架先出
  } catch (e) {
    if (isTimeout(e)) return serveFallbackShell(res);   // 兜底：CSR 骨架 + 客户端接管
    throw e;
  }
}
// 指标：metrics.histogram('ssr.render', ms); metrics.inc('ssr.fallback');
```
