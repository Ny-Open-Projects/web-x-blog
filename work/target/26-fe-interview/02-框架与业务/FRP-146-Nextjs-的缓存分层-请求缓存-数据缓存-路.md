---
title: [FRP-146] Next.js 的缓存分层（请求缓存/数据缓存/路由缓存）各自在什么层面生效？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-146：Next.js 的缓存分层（请求缓存/数据缓存/路由缓存）各自在什么层面生效？

**答**：
- 四层缓存自上而下：**请求记忆化**（React `cache()`：同一次渲染 pass 内相同参数的 fetch/函数去重）、**数据缓存**（fetch 结果跨请求持久化，`next.revalidate` 控制）、**全路由缓存**（构建期/运行时把 RSC + HTML 静态化）、**客户端路由缓存**（浏览器缓存已访问路由的 RSC payload，`staleTimes` 控制）。
- 生效层次不同是理解关键：请求记忆化随渲染结束失效；数据缓存跨请求；路由缓存在构建产物层；客户端路由缓存在浏览器内存。
- 失效入口：`revalidatePath/revalidateTag` 精确打掉数据缓存与路由缓存；dynamic API（cookies/headers）会把路由降级为动态渲染。
- 典型陷阱：fetch 缓存默认行为随版本变化（Next15 起默认不缓存），要显式声明 `cache: 'force-cache'` 或用 `cache()` 记忆化。

```javascript
// 简化实现，帮助理解四层缓存的生效与失效
// —— 第 1 层：请求记忆化（同一次渲染去重） ——
const getUser = cache(async (id) => {
  console.log('真实执行一次');
  return db.user.find(id);
});
// 一次渲染里 getUser(1) 被三处调用 -> 只执行一次（map 按 参数+调用点 去重）

// —— 第 2 层：数据缓存（跨请求） ——
fetch(url, { next: { revalidate: 60, tags: ['posts'] } });
// 简化的缓存判断：
function shouldRefetch(entry, now) {
  if (!entry) return true;
  return now - entry.timestamp > entry.revalidate * 1000; // 过期则后台重取
}
// revalidateTag('posts')：直接删除打了该 tag 的条目 -> 下次请求必 miss

// —— 第 3 层：全路由缓存 ——
function routeCachePolicy(route) {
  if (usesDynamicAPI(route))  return 'dynamic';   // 用了 cookies/headers：不静态化
  if (route.revalidate != null) return 'isr';      // 定时再生
  return 'static';                                  // 构建期生成 RSC + HTML
}

// —— 第 4 层：客户端路由缓存 ——
// Router.push('/a') 后再返回 '/a'：直接用内存里的 RSC payload（staleTimes 内）
// revalidatePath('/a', 'page') 同时打掉服务端缓存与通知客户端失效

// —— 完整失效链示意 ——
// Server Action 里 revalidatePath('/posts')
//   -> 数据缓存中 path 关联条目失效
//   -> 路由缓存中 /posts 的静态产物失效
//   -> action 返回的 RSC 树带新数据
//   -> 客户端路由缓存被标记 stale
```
