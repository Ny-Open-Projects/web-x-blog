---
title: [ENG-239] 横切关注点（埋点/权限/监控）的工程化组织（AOP 思路）怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-239：横切关注点怎么组织？
**答**：
- 反模式：每个组件手写埋点/权限判断——横切逻辑散落导致漏埋/漏鉴权且难统计。
- 落地手法：路由级（loader 守卫统一鉴权）、组件级（高阶包装 withTracking）、请求级（拦截器统一鉴权头与埋点）、编译级（构建时注入埋点标记）——按注入成本递增选择。
- 声明式优于命令式：埋点用配置驱动（页面声明 exposure 事件 schema，SDK 自动挂 IntersectionObserver），而非手写回调。
- 统一语义：横切层的通用模型（TrackEvent/Permissioncheck）单源定义，跨层复用。
- 追问钩子：为什么「编译级注入埋点」通常过度——编译时转换让埋点逻辑不可见不可调试，与 JSX 里显式 track 组件相比排查成本高；编译注入只适合全站统一的超高频事件（如路由 PV）。

```jsx
// 路由级守卫 + 组件级包装 + 请求拦截 三层
<Route loader={requireAuth(loader)} element={<TrackedPage event="detail_pv" />} />
api.interceptors.request.use(injectAuth);
api.interceptors.response.use(trackApiPerf);
// 声明式埋点：配置驱动
{ page: 'detail', exposure: { event: 'sku_expose', schema: exposureSchema } }
```
