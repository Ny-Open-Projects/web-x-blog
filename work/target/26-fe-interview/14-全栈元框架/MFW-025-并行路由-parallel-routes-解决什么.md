---
title: [MFW-025] 并行路由（parallel routes）解决什么问题？@slot 与 children 怎么协作？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-025：并行路由（parallel routes）解决什么问题？@slot 与 children 怎么协作？
**答**：
- 并行路由允许**同一布局里同时渲染多个路由段**（目录名 `@analytics`、`@team`），各自独立加载/流式/错误边界——适合仪表盘的多面板结构。
- slot 目录名以 `@` 开头，作为**同名 prop** 传给父 layout；`children` 是隐式 `@children` slot。
- 每个 slot 可有自己的 loading.js/error.js，互不阻塞（一个面板慢不影响其他面板先出）。
- 导航粒度：`router.push` 只更新目标 slot；软导航时其他 slot 保持原状（不匹配时回退 default.js 或上次内容）。
- 典型场景：`@modal` 并行路由实现「URL 即弹窗」——点列表项 push 到 `/photo/1`，photo 段渲染在 @modal 里，刷新页面时又是完整详情页（可分享、可后退）。

```
app/dashboard/
  layout.tsx       // 接收 children + @revenue + @users
  @revenue/page.tsx
  @users/page.tsx
  page.tsx         // children slot
```

```jsx
// app/dashboard/layout.tsx
export default function Layout({ children, revenue, users }) {
  // 三个 slot 并行渲染，各自独立流式
  return (
    <main>
      {children}
      <section>{revenue}</section>
      <section>{users}</section>
    </main>
  );
}

// app/dashboard/@revenue/page.tsx —— 独立的数据获取与 Suspense
export default async function Revenue() {
  const data = await getRevenue(); // 只挂起 @revenue slot
  return <b>{data.total}</b>;
}
```
