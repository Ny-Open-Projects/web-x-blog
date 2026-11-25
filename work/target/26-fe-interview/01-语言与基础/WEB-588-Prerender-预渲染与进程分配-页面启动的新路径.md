---
title: [WEB-588] Speculation Rules 预渲染：独立进程与启动优化
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 浏览器架构]
type: 面试题
---

## WEB-588：Speculation Rules 预渲染：独立进程与启动优化

**答**：
- Speculation Rules API 允许声明式预渲染：浏览器在隐藏的后台状态提前加载/渲染目标页面（含 JS 执行），跳转时直接激活，近 0 ms 显示
- 进程层面：预渲染的页面跑在独立渲染进程中（与其他文档隔离），激活时切换前台——正因是完整进程级隔离，预渲染的安全边界与普通页面一致
- 前端要适配「预渲染激活语义」：`document.prerendering` 为 true 时延迟非关键逻辑（打点、动画、自动播放视频），`activationstart` 时间点是真实起始
- 资源消耗权衡：预渲染=提前花一个进程+流量，命中率高才划算——用推测规则限定高概率导航（链接 hover、列表第一项）
- 监控闭环：`PerformanceNavigationTiming.activationStart` 判断是否来自预渲染，与普通加载分开统计 Core Web Vitals

```html
<script type="speculationrules">
{"prerender":[{"source":"list","urls":["/next-page"],
  "eagerness":"moderate"}]}
</script>
```

```javascript
// 预渲染期间避免副作用, 激活后再执行
if (document.prerendering) {
  document.addEventListener('prerenderingchange', initOnce, { once: true });
} else {
  initOnce();
}
// 统计: nav.timing.activationStart > 0 即来自预渲染
```
