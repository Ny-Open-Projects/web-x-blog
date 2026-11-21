---
title: [OPT-122] 首页接口瀑布（A→B→C 串行）如何优化成并行/预取/依赖编排？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-122：首页接口瀑布（A→B→C 串行）如何优化成并行/预取/依赖编排？

**答**：
- 先用 Network 面板确认瀑布：B 依赖 A 的 id、C 依赖 B，串行链路 = 各段 TTFB 之和。
- 三招：能并行的并行（Promise.all）、能预取的预取（路由切换前/接口前置到 HTML 内联）、必须依赖的编排前置（A 接口只返回 id，其余字段懒加载）。
- 后端配合：把"用户信息+推荐+角标"聚合为一个 BFF 接口，一次 RTT 替代三次。
- 兜底：依赖编排加超时降级，关键接口失败不阻塞整屏渲染。

```javascript
// 一一对应：接口依赖编排器——并行预取 + 依赖前驱 + 超时降级
async function fetchJSON(url, { timeout = 3000, signal } = {}) {
  const res = await fetch(url, { signal: AbortSignal.any([signal, AbortSignal.timeout(timeout)]) });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

async function loadHomeData() {
  // 1. 无依赖的接口立即并行发（含非关键数据，失败不阻塞）
  const userP = fetchJSON('/api/user');
  const bannersP = fetchJSON('/api/banners').catch(() => []); // 降级为空不阻塞
  // 2. 依赖编排：只等 user.id，不等 user 全量字段
  const user = await userP;
  // 3. 拿到最小依赖（id）后立刻发起下游请求，与 banners 下载重叠
  const ordersP = fetchJSON(`/api/orders?uid=${user.id}&fields=id,status,count`);
  const [_, banners, orders] = await Promise.all([userP, bannersP, ordersP]);
  return { user, banners, orders };
}
// HTML 中再加 <link rel="preconnect" href="//api.example.com"> 与
// <link rel="preload" as="fetch" href="/api/user"> 把首请求前置到解析期
```
