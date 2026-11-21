---
title: [CSS-201] 容器查询进阶：container-type 两种模式与 @container 完整语法怎么用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-201：容器查询进阶：container-type 两种模式与 @container 完整语法怎么用？

**答**：
- `container-type: inline-size` 是默认推荐：只对行向尺寸建立容器，元素高度仍由内容撑开；`size` 模式对宽高同时建立 containment，**元素尺寸不能再依赖内容**（高度必须显式给定，否则塌陷），只在确需按高度查询时使用。
- 语法全景：范围比较写法 `@container (400px <= width <= 800px)`；未命名的 `@container (...)` 查询**最近**的祖先容器，命名 `container-name` 后用 `@container card (...)` 精确指向，避免被外层容器"截胡"。
- style 查询 `@container style(--theme: dark)`：按容器上的自定义属性值切换子孙样式（无需给容器换 class）。2025-2026 口径：Chrome/Edge 111+、Safari 18+ 支持，**Firefox 尚未支持**——只能当渐进增强；尺寸容器查询才是 Baseline（CSS-055）。
- 核心价值：查询条件从"页面级断点"变成"组件自带的布局状态"，同一组件放进侧栏、主区、弹层自动适配，业务方不再传 `size` prop。

```css
/* container-type 两种模式：size 会切断"高度由内容决定" */
.side-item {
  container-type: inline-size;   /* 推荐：高度仍由内容撑开 */
}
.stage {
  container-type: size;          /* 宽高都参与查询，但必须显式给尺寸 */
  height: 300px;                 /* 不给高度会塌陷为 0，内部查询永远不命中 */
}

/* 范围语法 + 命名容器精确指向 */
.page { container-type: inline-size; container-name: page; }
.widget { container-type: inline-size; container-name: widget; }

@container widget (400px <= width <= 800px) {
  .widget .body { display: grid; grid-template-columns: 1fr 1fr; }
}
/* 写 widget 就查 widget，不会被最近的 page 容器命中 */

/* style 查询：容器换自定义属性，子孙自动联动（Firefox 不支持，渐进增强） */
.card-slot { --theme: dark; }
@container style(--theme: dark) {
  .card { background: #1f2937; color: #f9fafb; }
}
```
