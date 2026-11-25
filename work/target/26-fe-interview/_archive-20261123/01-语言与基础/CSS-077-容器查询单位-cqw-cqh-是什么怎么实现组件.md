---
title: [CSS-077] 容器查询单位 cqw/cqh 是什么？怎么实现"组件级响应式"？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-077：容器查询单位 cqw/cqh 是什么？怎么实现"组件级响应式"？

**答**：
- `cqw/cqh/cqi/cqb` 相对最近的查询容器：1cqw = 容器宽度的 1%，与 vw 之于视口同理。
- 必须先有 `container-type: inline-size` 声明，单位才会解析；没有容器时回退为小视口值。
- 同一个卡片组件放进窄侧栏自动变紧凑，放进宽内容区自动展开，无需媒体查询。
- `cqi` 是逻辑内联轴方向，与 RTL 配合更稳。
- 配合 `@container` 一起构成组件级响应式的完整闭环。

```css
.widget-wrapper { container-type: inline-size; }

.widget {
  /* 字号与间距随容器宽度缩放，而非视口 */
  font-size: clamp(0.875rem, 2cqi + 0.5rem, 1.125rem);
  padding: 4cqi;
  display: grid;
  grid-template-columns: 1fr;
  gap: 2cqi;
}

@container (min-width: 480px) {
  .widget { grid-template-columns: auto minmax(0, 1fr); }
}
```
