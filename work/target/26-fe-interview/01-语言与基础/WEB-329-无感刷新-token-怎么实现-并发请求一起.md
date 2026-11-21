---
title: [WEB-329] 无感刷新 token 怎么实现？并发请求一起 401 怎么办？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 笔试题
---

## WEB-329：无感刷新 token 怎么实现？并发请求一起 401 怎么办？
**答**：
- 拦截器收到 401 → 暂存后续请求 → 用 refresh 换新 token → 重放暂存请求 → 继续原流程；用户无感。
- 并发竞态：多个请求同时 401，必须保证只发起一次刷新，其余等待同一个 Promise；刷新失败则登出。
- 细节：重放要保留原 header/取消器；刷新接口自身失败要清登录态并跳登录页，防止死循环。

```javascript
let refreshing = null;
async function request(config) {
  const res = await send(config);
  if (res.status !== 401) return res;
  refreshing ??= doRefresh().finally(() => (refreshing = null)); // 只刷一次
  const ok = await refreshing.catch(() => null);
  if (!ok) return logout();
  return send(config);   // 重放
}
async function doRefresh() { const t = await api('/token/refresh'); setToken(t.access); return t; }
console.log('单飞（single-flight）+ 重放 = 无感刷新骨架');
```

**评分点**：
- 结论先行，能一句话说清核心机制
- 要点覆盖主流程与关键分支（异常/并发/边界）
- 代码可运行且体现安全或性能意识
- 能主动说出"工程上怎么选"与常见坑
