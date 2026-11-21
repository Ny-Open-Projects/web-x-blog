---
title: [DP-278] 源码识别：SuspenseList 源码中的揭示策略？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-278：源码识别：SuspenseList 源码中的揭示策略？
**答**:
- 策略（核心）：revealOrder（together 全部就绪一起揭示 / forwards 顺序揭示 / backwards）——同一组 Suspense 边界的揭示编排策略。
- tail 选项：collapsed（只保留第一个 fallback）控制等待期显示多少骨架。
- 状态协调：SuspenseList 是"边界协调者"，内部收集子边界状态（就绪数）驱动揭示时机——观察者聚合。
- 识别要点：能说清"together 防止列表逐个跳入造成布局抖动"的真实动机。

```tsx
// SuspenseList 揭示策略（心智模型）
<SuspenseList revealOrder="together" tail="collapsed">
  <Suspense fallback={<Skel/>}><Profile userId="1"/></Suspense>
  <Suspense fallback={<Skel/>}><Profile userId="2"/></Suspense>
  <Suspense fallback={<Skel/>}><Profile userId="3"/></Suspense>
</SuspenseList>
// together：三个数据都 resolve 后统一替换骨架（防逐个跳变）
// forwards：按顺序揭示（2 未就绪则 3 也等）；backwards 反之
// tail="collapsed"：只显示第一个 Skel，其余高度占位
// 实现心智：协调者收集边界 → 计数 → 达到策略条件才统一切换 children
```
