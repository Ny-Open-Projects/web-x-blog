---
title: [MFW-304] View Transitions 与 App Router 路由转场整合
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-304：View Transitions 整合

**答**:
- 语义匹配：VT 的 document 级转场与 App Router 导航天然契合（URL 变化即转场时机）——React 的 <ViewTransition>（实验）或手动 startViewTransition 包 router.push
- 元框架特有注意：转场快照捕获时机 vs RSC 流式到达（新页未水合完就截图会闪）——等 navigate 事件 + 首帧渲染完成再触发转场；Shared Element（列表图 → 详情主图）需要两页稳定 key（data-view-tag）
- 降级链：不支持 VT 的浏览器直接切换（无动画但不坏）——特性检测写法；减少动效偏好（prefers-reduced-motion）尊重
- 性能红线：转场动画期间禁止触发重数据 fetch（动画帧被 IO 挤掉帧）——转场窗口 ≤300ms 内只做视觉

```javascript
// 手动包装（兼容期方案）
async function navWithVT(to) {
  if (!document.startViewTransition) return router.push(to)
  document.startViewTransition(() => {
    router.push(to)                                  // flush 同步 DOM 更新后快照
  })
}
```
