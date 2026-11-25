---
title: [R19-258] Suspense 更新在 transition 中的「保持旧 UI」行为是怎么回事？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-258：Suspense 更新在 transition 中的「保持旧 UI」行为是怎么回事？
**答**：
- 在 startTransition 中触发会进入新 Suspense 边界的更新：React 保持旧内容显示（不切 fallback），isPending 标记进行中——这就是「已有内容时不闪骨架」的内建行为。
- 未包 transition 的同步更新：立即切 fallback（闪骨架）。
- 应用：Tab 切换、列表筛选这类「内容替换」用 transition 包裹，体验连贯。
- 边界细节：不同边界的切换独立处理；新内容 resolve 后一次性提交（避免半新半旧）。
- 与 useDeferredValue 配合：输入驱动 + 数据等待场景二者常组合使用。
