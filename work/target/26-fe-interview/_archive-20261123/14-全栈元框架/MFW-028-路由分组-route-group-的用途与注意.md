---
title: [MFW-028] 路由分组（route group）的用途是什么？对 URL 有什么影响？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-028：路由分组（route group）的用途是什么？对 URL 有什么影响？
**答**：
- `(group)` 括号目录**不进 URL**，纯粹用来组织代码：给不同区域套不同 layout（如 `(marketing)` 有营销页头、`(app)` 有登录态侧栏）。
- 典型用法：一个项目里同一 URL 层级可以来自不同分组——`app/(site)/page.tsx` 和 `app/(admin)/page.tsx` 不能同时存在（路径冲突会构建报错）。
- 分组让多个根布局成为可能：`app/(marketing)/layout.tsx` 与 `app/(dashboard)/layout.tsx` 各自包含 `<html>`，互不影响。
- 注意事项：分组内创建根 layout 时分组外必须有统一入口；同 URL 只能落在一个分组，`page.tsx` 冲突是高频踩坑。
- 配合 loading/error/模板：每组可以有独立的 loading.js、error.js、template.tsx（每次导航重建）。

```
app/
  (marketing)/
    layout.tsx        // 根布局 A：营销头部 + footer
    page.tsx          // URL: /
    pricing/page.tsx  // URL: /pricing
  (app)/
    layout.tsx        // 根布局 B：登录态侧栏
    dashboard/page.tsx // URL: /dashboard
```

```jsx
// app/(marketing)/layout.tsx —— 分组根布局，包含自己的 <html>
export default function MarketingLayout({ children }) {
  return (
    <html lang="zh">
      <body>
        <MarketingHeader />
        {children}
        <Footer />
      </body>
    </html>
  );
}
```
