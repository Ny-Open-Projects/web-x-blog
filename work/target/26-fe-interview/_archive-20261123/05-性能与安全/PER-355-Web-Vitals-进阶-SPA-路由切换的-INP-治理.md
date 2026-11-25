---
title: [PER-355] SPA 路由切换卡顿（点击菜单到新页面可交互）怎么治理？软导航 INP 专项？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-355：SPA 路由切换卡顿（点击菜单到新页面可交互）怎么治理？软导航 INP 专项？

**答**：
- 路由切换卡顿三段：点击响应（menu click → 视觉反馈，input delay）→ 加载（chunk/数据请求）→ 新页面可交互（注水/handler 绑定完成）。标准 CWV 只测硬导航，软导航要自定义口径（PER-253 的 SPA-NT + 交互就绪）。
- 点击响应段：路由 click handler 里做重活（权限校验、埋点同步）→ 切片；菜单先视觉反馈（active 态）再异步路由——"点击即变化"保 INP。
- 加载段：路由级 code splitting（PER-088 懒加载+空闲预取）、数据预取（hover/触摸菜单时 prefetch 接口）、Suspense 分块渲染（先出骨架区块）。
- 可交互段：注水切片（React 并发）、延迟绑定非关键 handler、避免路由后大量同步计算（排序/格式化挪 Worker 或 idle）。
- 度量：自定义 SPA-NT（路由起点→内容稳定）+ 交互就绪（路由起点→首 handler 可响应），按路由出 p75，与硬导航指标分开看板。

```javascript
// 路由切换的点击反馈优先（保 INP）与预取联动
menu.addEventListener('click', (e) => {
  const route = e.target.dataset.route;
  setActive(route);                                  // 1. 同步视觉反馈（INP 优先）
  requestIdleCallback(() => preloadRoute(route));    // 2. 空闲时预取 chunk+数据
  setTimeout(() => navigate(route), 0);              // 3. 下一宏任务再导航（让反馈先渲染）
});
// 指标：SPA-NT = navigateStart → DOM 稳定（PER-253）；交互就绪 = navigateStart → 首次 click 无排队
```
