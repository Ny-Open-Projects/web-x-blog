---
title: [MFW-542] 元框架可观测性：RSC 渲染的 trace 与慢查询归因
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-542：元框架可观测性：RSC 渲染 trace

**答**:
- RSC 渲染的 trace 结构（RBL-728 的框架版）：root span = 页面请求 → 子 span = 每个组件的渲染（async RSC 组件 = 数据获取+渲染合一——span 内含 fetch 子 span）；「组件级耗时」是 RSC 可观测的核心指标（哪个组件的 fetch 慢）。
- 实现机制：框架在渲染 async 组件时自动开 span（对 React 不可见层包裹）——OpenTelemetry 集成（Next 的 otel 支持：请求上下文传播）；dev 工具（React DevTools 的 server profiling）。
- 慢的归因路径：TTFB 慢 → trace 找最深的 span → 区分「数据慢」（fetch span 长）vs「渲染慢」（无 fetch 但 span 长——大组件树同步渲染）；瀑布检测（串行 fetch span——RBL-930 lint 的运行时验证）。
- 采样与开销（RBL-728 原则）：组件级 span 全开 = 每请求数十 span——生产采样（慢请求全采 + P95 采样）；span 属性只放 id 不放数据（隐私 RBL-679）。
- 追问钩子：为什么 RSC 的「组件即数据层」让可观测性比传统 SSR 更重要？——传统 SSR 的数据获取集中在页面入口（一处慢好定位）；RSC 的数据获取分散在每个组件（N 个组件 N 个数据源——慢点离散化）；「可观测性必须跟上架构的数据分散度」——组件级 trace 是 RSC 架构的配套基建而非可选优化，这解释了框架为什么内建 otel。

```javascript
// RSC 组件的自动 trace（框架内部概念）
async function traceComponent(name, fn) {
  return tracer.startActiveSpan(`rsc:${name}`, async (span) => {
    const t0 = performance.now();
    try {
      const result = await fn();
      span.setAttribute('rsc.duration', performance.now() - t0);
      return result;
    } catch (e) {
      span.recordException(e); throw e;
    } finally { span.end(); }
  });
}
// 组件内 fetch 的子 span
async function Product({ id }) {
  const product = await db.find(id);                     // 子 span: db.query
  const reviews = await getReviews(id);                  // 子 span: fetch
  // 串行瀑布可见：两个 span 顺序排列——优化为 Promise.all
}
```
