---
title: [V3-362] Suspense 与 Transition 配合时进出场有哪些细节？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-362：Suspense 与 Transition 配合时进出场有哪些细节？
**答**：
- 标准结构：`<Suspense><Transition><Content/></Transition><template #fallback><Skeleton/></template></Suspense>`——Transition 在内部，内容 resolve 后带动画进场。
- 注意顺序：Transition 包 Suspense 会导致 fallback 也走 transition，视觉混乱；正确做法是 Transition 在 Suspense 内。
- 切换等待：Suspense 在切换新内容时会等待旧内容的 leave 动画完成（内置机制），避免新旧内容重叠。
- fallback → 内容的切换可用 mode="out-in" 让骨架先退场再进内容，代价是总时长增加。
- 性能提示：长列表进场动画用 CSS transform 类动画而非触发 layout 的属性。
