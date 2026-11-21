---
title: [CSS-239] View Transitions 的命名与分组约束
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-239：View Transitions 的命名与分组约束

**答**：
- view-transition-name 必须页面内唯一——重复时报错（AbortError）或动画异常；列表项可用内容 ID 动态赋值
- 分组机制：同名元素新旧状态配对成一组，独立于全局默认组（root）做动画；无名元素全部落入 root 组整体渐变
- 动态命名：JS 设置 `el.style.viewTransitionName = 'item-' + id`，切换后移除——避免常驻名称冲突
- 快照约束：被命名元素在过渡期间被快照替换（原元素 visibility:hidden），期间不响应交互——长动画要限时
- 面试加分：说出「同屏两列表互相跳转时的命名冲突」与「name 只在 transition 期间存在」的实践细节

```javascript
async function goToDetail(card, id) {
  card.style.viewTransitionName = `cover-${id}`;   // 临时命名
  await document.startViewTransition(() => renderDetail(id)).finished;
  card.style.viewTransitionName = '';               // 用完移除
}
```
