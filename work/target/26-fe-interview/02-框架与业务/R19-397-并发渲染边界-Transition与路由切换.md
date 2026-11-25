---
title: [R19-397] 并发渲染边界：Transition 与路由切换的配合
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 路由]
type: 面试题
---

## R19-397：并发渲染边界：Transition 与路由切换的配合

**答**：
- react-router/Next 的 transition 集成：导航 setState 包 transition——旧页面保持显示直到新页面可渲染（无空白闪烁）；这是 React Router 6.4+ / Next App Router 的默认行为
- Suspense 协同：新页面数据未就绪（loader/use）→ transition 保持旧页 + 新页 Suspense fallback 已开始渲染——「旧页 + 局部加载指示」的最佳体验
- 路由切换的取消语义：用户快速连点导航——前一个 transition 被打断（未 commit），只有最后一次导航 commit——导航防抖天然获得
- 回退（popstate）：浏览器返回走同步导航（discrete）——不进 transition（用户预期立即返回）
- 实战坑：transition 期间禁用导航 UI（防止用户不知道当前在哪）——用 router 的 transition pending 状态显示进度条

```jsx
function useNavigationTransition() {
  const [isPending, start] = useTransition();
  const navigate = (to) => start(() => router.navigate(to));  // 旧页保持
  return { navigate, isPending };   // pending → 顶部进度条
}
```
