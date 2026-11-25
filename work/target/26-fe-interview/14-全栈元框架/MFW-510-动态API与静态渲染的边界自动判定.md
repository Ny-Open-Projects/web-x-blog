---
title: [MFW-510] 动态 API 与静态渲染的边界：框架如何判定一个路由可否静态化
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-510：动态 API 与静态渲染的边界：路由静态化判定

**答**:
- 判定机制：渲染期间访问「动态 API」即退出静态化——cookies()/headers()/searchParams（page）/未预生成的 dynamic params、`fetch cache:'no-store'`——框架在渲染时「捕获」这些访问（Proxy/上下文标记）→ 路由标记为 dynamic。
- 边界的显式控制：`export const dynamic = 'force-static' | 'force-dynamic' | 'auto'`——auto（默认：访问动态 API 才动态化）/force-dynamic（每请求渲染）/force-static（强制静态——动态 API 返回空值，编译期警告）。
- 边界的隐性陷阱：1) 深层组件隐式读 cookie（不明显的动态化——「为什么我的首页每请求渲染」排查第一站）；2) fetch 传染（一个 no-store fetch 让整路由动态——粒度是路由级不是组件级）；3) generateStaticParams 缺失的动态路由 → 按需 ISR 而非构建期全量。
- 追问钩子：为什么「动态化粒度是路由级」而不是组件级？——静态化单位 = Full Route Cache 的键（整条路由的 payload）；组件级动态化需要「payload 部分静态部分动态」——这正是 PPR（Partial Prerendering）的解法：静态壳构建期生成 + 动态洞流式填充；路由级粒度是当前实现，PPR 是粒度演进的终点——「缓存键的粒度演进」是元框架的主线矛盾（RBL-596 chunk 粒度同构）。

```javascript
// 动态化判定的调试（找出谁让路由动态了）
export const dynamic = 'auto';
import { cookies } from 'next/headers';
export default async function Page() {
  // 隐性动态源：深层组件的 cookies() 调用
  // 排查：next build 输出标记 ƒ(动态) 的路由 → 用 DEBUG 动态 API 追踪
  return <Suspense fallback={<Skeleton />}><UserGreeting /></Suspense>;
}
// PPR 形态（粒度演进终点）
// export const experimental_ppr = true;
// 页面静态壳构建期产出；<Suspense> 包裹的动态洞请求时流式
// async function UserGreeting() {
//   const c = cookies();   // 动态洞内部——不影响外壳静态化
//   return <span>Hi {c.get('name')}</span>;
// }
```
