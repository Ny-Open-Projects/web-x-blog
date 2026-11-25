---
title: [HW-151] 手写 View Transitions API 列表重排——startViewTransition + view-transition-name 绑定实现元素移动动画
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-151：手写 View Transitions API 列表重排——startViewTransition + view-transition-name 绑定实现元素移动动画
**答**：列表拖拽重排的平滑动画（元素从旧位置滑到新位置）：View Transitions API——DOM 更新前调用 document.startViewTransition，给每个元素唯一 view-transition-name，浏览器自动插值旧位置→新位置（transform 动画合成器执行）。降级：不支持时直接更新（功能不受损）。

```javascript
async function reorderWithTransition(items, nextOrder, render) {
  if (!document.startViewTransition) { render(nextOrder); return; }   // 降级：直接更新
  // 每元素唯一名（key 稳定性前提，HW-106）
  const nameOf = (id) => `item-${id}`;
  const transition = document.startViewTransition(() => {
    render(nextOrder);                                  // DOM 更新（回调内同步完成）
  });
  await transition.finished;                            // 动画完成（浏览器自动插值）
}
```
```css
.item { view-transition-name: var(--vt-name); }        /* 每元素唯一（style="--vt-name: item-3"） */
::view-transition-group(*) { animation-duration: 240ms; }   /* 移动插值时长 */
@media (prefers-reduced-motion: reduce) { ::view-transition-group(*) { animation: none; } }
```
```javascript
// 注意：view-transition-name 必须唯一（重复名 = 动画错乱）；大量元素全命名有成本——只给动画涉及元素命名
// 完整降级链：View Transitions → FLIP 手写（测量旧位→更新→transform 反向→过渡）→ 直接更新
```

**评分点**：
- startViewTransition + 唯一 view-transition-name 的移动插值原理。
- 降级链三级（VT → FLIP → 直接更新）——功能不受损。
- name 唯一性与"只命名涉及元素"的成本意识。
- prefers-reduced-motion 尊重（PER-489 双视角）。
