---
title: [CSS-202] cqw / cqh 等容器单位怎么用？与 vw / rem 是什么关系？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-202：cqw / cqh 等容器单位怎么用？与 vw / rem 是什么关系？

**答**：
- 六个单位：`cqw/cqh`（容器宽/高的 1%）、`cqi/cqb`（行向/块向）、`cqmin/cqmax`（两者较小/较大值的 1%）；未命中任何容器祖先时**回退为小视口单位**（cqw → svw），不会失效成 0。
- 与 CSS-194 的单位体系对比：vw 跟随视口、rem 跟随根字号，容器单位**跟随最近的容器祖先**——嵌套容器里每层组件各用各的参照，这是"组件级流式排版"的基础。
- 常见误区：cqw 参照的是**最近的容器祖先**，与 `container-name` 无关——元素在 named 容器外时单位不会改去找同名容器。
- 典型用法：`clamp()` 做容器级流式字号，替代"靠媒体查询猜组件所在区域"的写法；配合 `@container` 查询，断点与排版共用同一容器参照。

```css
/* 容器级流式排版：标题随"卡片宽度"而非视口缩放 */
.card-slot {
  container-type: inline-size;
}

.card-title {
  /* 侧栏 240px：约 14px；主区 600px：被钳制在 22px */
  font-size: clamp(14px, 4cqw, 22px);
}

/* 嵌套容器：内层组件用自己的容器做参照，互不干扰 */
.page        { container-type: inline-size; }
.page .aside { width: 25cqw; }                /* 相对 page */
.aside       { container-type: inline-size; } /* aside 自己也是容器 */
.aside h4    { font-size: 5cqw; }             /* 相对 aside，不相对 page */

/* 无容器祖先时的回退：cqw 退化为 svw，页面兜底布局仍然成立 */
.orphan { padding: 2cqw; }                     /* 没有容器祖先 ≈ padding: 2svw */

/* 极小容器的防失控写法：cqmin 保证小尺寸下不爆炸 */
.badge { font-size: max(12px, 3cqmin); }
```
