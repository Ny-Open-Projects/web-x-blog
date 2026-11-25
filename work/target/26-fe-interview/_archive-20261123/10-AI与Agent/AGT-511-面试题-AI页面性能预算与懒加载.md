---
title: [AGT-511] AI 对话页体积大（markdown 渲染/高亮/图表/公式），如何做性能预算与按需加载？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-511：AI 对话页体积大（markdown 渲染/高亮/图表/公式），如何做性能预算与按需加载

**答**：
- 把重组件全部动态化：markdown 渲染器、语法高亮、KaTeX、Mermaid 都用 import() 懒加载，首屏只发核心对话链路（目标 <150KB gzip）。
- 高亮/公式在「消息进入视口」时才加载并渲染（IntersectionObserver），配合占位防止 CLS。
- 建立性能预算门禁：bundle 超预算 CI 失败；运行时关注首字延迟（感知性能）与长任务，AI 页卡顿大头往往在渲染而非网络。

```javascript
// 视口内才加载重组件
const MarkdownLazy = defineAsyncComponent(() =>
  inViewport(ref) ? import('./HeavyMarkdown') : placeholder);
const io = new IntersectionObserver((es) => {
  es.forEach(e => { if (e.isIntersecting) loadHeavy(e.target); });
}, { rootMargin: '200px' });           // 提前 200px 预加载
io.observe(messageEl);
```

