---
title: [XP-297] 跨端深链（Deep Link）的路由统一
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-297：跨端深链（Deep Link）的路由统一

**答**：
- 需求：App scheme/Universal Link/小程序码 跳转统一路由解析。
- 实现：路由表统一（path -> page），参数标准化（query 解析），未匹配兜底（首页/落地页）。
- 性能：深链直达页预取数据（解析参数即拉）。

```javascript
// 统一路由
const ROUTES = {
  '/product/:id': { page: 'detail', prefetch: id => prefetchDetail(id) },
  '/order/list': { page: 'orders' },
};
function resolveDeepLink(url) {
  const path = new URL(url).pathname;
  for (const [pattern, route] of Object.entries(ROUTES)) {
    const m = matchPattern(pattern, path);
    if (m) { route.prefetch?.(m.params.id); return { ...route, params: m.params }; }
  }
  return { page: 'home', params: {}, note: '未匹配兜底' };
}
function matchPattern(pattern, path) {
  const pp = pattern.split('/'), cp = path.split('/');
  if (pp.length !== cp.length) return null;
  const params = {};
  for (let i = 0; i < pp.length; i++) {
    if (pp[i].startsWith(':')) params[pp[i].slice(1)] = cp[i];
    else if (pp[i] !== cp[i]) return null;
  }
  return { params };
}
```
