---
title: [PER-254] SSR 与 CSR 页面的 CWV 表现差异在哪里？各自的优化重点是什么？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-254：SSR 与 CSR 页面的 CWV 表现差异在哪里？各自的优化重点是什么？

**答**：
- LCP：SSR 天然占优（HTML 直出内容，无需等 JS 渲染），优化重点在 TTFB 与流式下发；CSR 的 LCP 依赖 JS 下载执行，优化重点在 bundle 减量、预取数据与骨架屏策略。但 SSR 的注水长任务会伤 INP——SSR 页面常见"LCP 快、INP 慢"。
- INP：CSR 交互链路简单；SSR 页面注水（hydration）是长任务大户，注水期间点击会排队。优化重点：选择性注水/渐进注水（ islands 架构）、注水切片、避免注水期重三方脚本并发。
- CLS：SSR 要防"注水替换"（服务端与客户端渲染结果不一致导致二次渲染位移）；CSR 要防异步数据插入顶开内容。
- 结论：没有"SSR 一定快"，是权衡——SSR 快 LCP 但可能伤 INP；验收永远看四指标整体 + p75。

```jsx
// SSR 注水切片：React 18 的 startTransition 让注水不再阻塞交互
// 服务端流式输出 + 客户端 hydrateRoot：
import { hydrateRoot } from 'react-dom/client';
hydrateRoot(document.getElementById('root'), <App />);
// React 18 默认对首次注水做并发分段，但注水期间的高频事件仍可能排队。
// 补充手段：注水完成的组件才注册昂贵 handler（条件注册），注水期用轻量委托：
document.addEventListener('click', (e) => {         // 注水前的兜底委托
  if (!window.__hydrated) e.preventDefault();       // 防止注水期误触发半初始化交互
}, true);
```
