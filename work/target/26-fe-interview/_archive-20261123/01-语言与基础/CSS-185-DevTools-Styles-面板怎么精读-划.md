---
title: [CSS-185] DevTools Styles 面板怎么精读（划线规则、继承链、层叠视图）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-185：DevTools Styles 面板怎么精读（划线规则、继承链、层叠视图）？

**答**：
- 被划线的属性三种来源：被更高优先级/更后规则覆盖、缩写属性展开后被单项覆盖、继承值被更近祖先拦截——排查“样式不生效”先看划线。
- Computed 面板看最终值与继承链（inherited from ... 逐层上溯），Styles 面板看声明与来源文件。
- `:hov` 按钮强制伪类状态，Filter 按属性过滤，`@layer` 分组标题显示层级归属——层叠视图把“谁赢了”讲清楚。
- element.style 是内联优先级区，顶部还有 UA 样式与 user-agent shadow 部分，优先级链路完整可见。

```css
/* Styles 面板表现对照 */
.card { color: #333; }              /* 与后续规则同优先级，按书写顺序 */
.card {
  color: #666;                      /* 覆盖上一条，上一条被划线 */
  font-size: 14px;
}
.card {
  font-weight: bold;                /* 单属性声明在前 */
}
.card {
  font: 14px/1.5 sans-serif;        /* 后写的缩写把 font-weight 重置为 normal，上一条被划线 */
}

/* 继承链示例：Computed 面板中 .card 的 color
   显示 inherited from .wrap —— .card 未声明 color 时生效 */
.wrap { color: #999; }

/* 层叠视图：面板按 layer 分组显示 */
@layer base { .card { padding: 8px; } }
@layer components { .card { padding: 12px; } }  /* 后声明的层胜出 */
```
