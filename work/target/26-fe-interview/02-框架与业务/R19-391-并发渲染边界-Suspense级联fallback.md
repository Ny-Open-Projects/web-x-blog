---
title: [R19-391] 并发渲染边界：嵌套 Suspense 的级联 fallback
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, Suspense]
type: 面试题
---

## R19-391：并发渲染边界：嵌套 Suspense 的级联 fallback

**答**：
- 级联行为：嵌套 Suspense 中「父边界比子边界先就绪」→ 父先显示（子还在自己的 fallback）——不会重复显示父 fallback；但「父比子晚」→ 子树整体被父 fallback 遮住（已就绪的子内容被藏）——这是「粒度反直觉」点
- 设计原则：外层 Suspense 包「慢而不变的大区域」，内层包「独立快区域」——避免「快区域被慢父拖累」：把慢边界下沉而不是上提
- React 19 fallback 节流（fallbackThrottleMs）：阈值内来回切换 fallback/内容会被合并——网络抖动时 UI 稳定
- 实战模式：「关键路径无 Suspense + 增强区有」——核心内容同步渲染，推荐位/评论用 Suspense（渐进出现）
- 调试：React DevTools 的 Suspense 树高亮 pending 边界——看「谁在等谁」修正粒度

```jsx
<Suspense fallback={<PageShell />}>          // 大区域(整页壳)
  <Header />                                  // 同步
  <Suspense fallback={<FeedSkeleton />}>
    <Feed />                                  // 慢接口独立边界
  </Suspense>
  <Suspense fallback={<RecSkeleton />}>
    <Recommend />                             // 快区域独立
  </Suspense>
</Suspense>
```
