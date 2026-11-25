---
title: [MFW-767] 软导航的错误处理
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-767：软导航的错误处理

**答**:
- 软导航的错误层次：1) **payload 请求失败**（网络断/404/500——router 的 error 处理：显示 error UI + URL 回退或不回退（URL 已变——回滚策略 RBL-676）；2) **流中断**（payload 流式传输中断——部分内容已渲染 → 错误段 fallback（RBL-652 流中错误）；3) **水合错误**（payload 渲染成功但水合失败——hydration error（client 重渲染整树——降级为 CSR）；4) **error.tsx 的软导航语义**（软导航的错误段 → 段级 error.tsx；导航失败 → 路由级 error）。
- 错误的用户体验设计：1) **重试按钮**（error.tsx 的 reset()——重新请求 payload RBL-536）；2) **返回导航**（error UI 的「返回上一页」——history.back 的语义）；3) **URL 保持 vs 回滚**（404 页 = URL 保持（用户看到 404 页面）；网络错误 = URL 回滚或保持（回滚 = 丢失导航意图；保持 = 用户可重试））。
- 追问钩子：为什么「软导航的网络错误」的 URL 处理比「硬导航」更复杂？——硬导航：浏览器处理（URL 变 → 404 页显示——浏览器原生行为）；软导航：JS 控制（URL 已 pushState → payload 失败 → 决定「保持 URL 显示错误」or「back() 回滚」——两种策略的权衡）；「保持」= 用户可重试（刷新 payload——URL 不变重试语义清晰）；「回滚」= 用户回到原页面（不丢失上下文——但导航意图丢失）——框架选择「保持 URL + 显示错误 + 重试按钮」（Next 的默认）。

```tsx
// app/error.tsx —— 软导航错误的 UI
'use client';
export default function Error({ error, reset }) {
  return (
    <div role="alert">
      <h2>页面加载失败</h2>
      <p>{error.message}</p>
      <button onClick={reset}>重试</button>               {/* 重新请求 payload */}
      <button onClick={() => window.history.back()}>返回</button>
    </div>
  );
}
// app/not-found.tsx —— 404 的软导航
export default function NotFound() {
  return <h2>404 - 页面不存在</h2>;                       {/* URL 保持——404 语义 */}
}
// Router 的错误处理层
// 1. payload fetch 失败 → router error → error.tsx
// 2. 流中断 → 部分 fallback + error 段
// 3. 水合失败 → client 重新渲染（CSR 降级）
```
