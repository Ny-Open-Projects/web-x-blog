---
title: [WCN-928] Islands 退化策略：JS 未加载或失败时如何让页面仍然可用
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-928：Islands 退化策略：JS 未加载或失败时如何让页面仍然可用

**答**：
- 结论先行：islands 必须遵循渐进增强——默认输出完整可用的 HTML，JS 只是增强；任何岛在 JS 失败时都应退化到「能用但体验降级」。
- 表单/导航：用原生 `<form action>`、`<a href>` 保证无 JS 可提交/跳转；JS 加载后拦截走 SPA，失败则自然回到原生行为。
- 交互组件：加购按钮无 JS 时退化为「跳到加购确认页」，轮播退化为纵向列表（CSS overflow），搜索退化为提交到服务端结果页。
- 错误隔离：单个岛 chunk 加载失败不应拖垮整页——用 `import().catch()` 包裹，失败时保留 SSR HTML 并打日志；监控水合失败率。
- 追问钩子：面试官问「怎么测退化路径」——答：用浏览器禁用 JS / 限速 + 阻断 chunk 请求做 E2E，验证核心转化路径仍可用。

```javascript
// 渐进增强：先有可用 HTML，再 try 水合增强
async function enhance(el, loader) {
  try {
    const mod = await loader();
    mod.hydrate(el);               // 成功：交互增强
  } catch (e) {
    el.dataset.degraded = 'true';  // 失败：保留 SSR HTML，走原生行为
    console.warn('island 水合失败，已降级', e);
  }
}
// SSR 中加购按钮本就是 <a href="/cart/add?id=1">，无 JS 可点
// JS 成功后拦截为 AJAX 加购：
enhance(document.querySelector('[data-island=buy]'), () => import('./buy.js'));
```
