---
title: [CSS-055] 容器查询 @container 是什么？和媒体查询相比解决什么问题？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-055：容器查询 @container 是什么？和媒体查询相比解决什么问题？

**答**：
- 媒体查询看的是**视口**，容器查询看的是**最近容器祖先的尺寸**，实现真正的组件级响应式。
- 先用 `container-type: inline-size` 声明容器，再用 `@container (min-width: 400px)` 查询。
- 查询单位 cqw/cqh 相对容器尺寸（1cqw = 容器宽的 1%）。
- 典型场景：同一个卡片组件在侧栏窄、在主区宽时展示不同密度，无需业务方传 prop。

```css
/* 声明容器 */
.card-slot {
  container-type: inline-size;
  container-name: card;
}

/* 容器内响应式 */
.card {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
@container card (min-width: 420px) {
  .card {
    flex-direction: row;
    align-items: center;
  }
  .card .thumb { width: 96px; height: 96px; }
}

/* cqw 单位：标题随容器缩放 */
.card h3 { font-size: clamp(14px, 5cqw, 22px); }
```
