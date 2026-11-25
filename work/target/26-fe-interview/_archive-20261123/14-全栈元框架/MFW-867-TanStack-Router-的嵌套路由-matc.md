---
title: [MFW-867] TanStack Router 的嵌套路由 match 与 Suspense 边界怎么对应
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-867：TanStack Router 的嵌套路由 match 与 Suspense 边界怎么对应

**答**：
- 结论：每个路由匹配（match）对应一个 Suspense 边界；子路由 loader 挂起时只降级该子区域，父布局保持已渲染状态。
- 落地：matches.map 渲染 Match 并包 Suspense，pendingMatch 显示该路由的 pending component。
- 追问钩子：父路由 loader 挂起会怎样？——整棵子树降级到父级 fallback，所以父 loader 要快且稳定。

```javascript
function RouterView() {
  const matches = useRouterState({ select: s => s.matches });
  return matches.reduceRight(
    (child, match) => (
      <Suspense fallback={<match.pendingComponent/>}>
        <Match match={match}>{child}</Match>
      </Suspense>
    ),
    null
  );
}
// __root → /posts → /posts/$id 三层 Suspense
// /posts/$id 的 loader 挂起 → 只显示它的 pendingComponent
```
