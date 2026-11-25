---
title: [CSS-349] Grid 布局深水：隐式轨道与自动放置算法
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-349：Grid 布局深水：隐式轨道与自动放置算法

**答**：
- 自动放置算法：dense 模式会回填空洞（重排性能代价 + 视觉顺序与 DOM 不一致可访问性问题），sparse（默认）顺序前进留洞——大列表用 sparse，编辑器类布局才用 dense
- 隐式轨道：超出显式定义的网格自动生成 implicit track，grid-auto-rows/columns 控制其尺寸——masonry 类布局靠 auto-rows: min-content + span 动态行数
- fr 与 minmax 交互：1fr 实为 minmax(auto, 1fr)——内容最小尺寸（min-content）会撑破 fr 分配，导致「1fr 不等分」；正确等分用 minmax(0, 1fr)
- subgrid：子网格继承父网格轨道定义（对齐跨嵌套组件的行/列），解决「卡片标题行高对齐」这类跨层对齐；浏览器支持已广
- 布局失效：改一个 grid item 内容 → 该 item 所在轨道尺寸重算 → 同轨道其他 item 重排——轨道共享是 Grid 失效传播的主要来源（比 Flex 更广泛）

```css
/* 等分陷阱修复 */
.row { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); }
/* masonry 近似 */
.masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: 8px;                     /* 细行 + span 动态跨行 */
}
.masonry > .item--tall { grid-row: span 12; }
/* subgrid: 卡片内部与外层轨道对齐 */
.card { display: grid; grid-template-rows: subgrid; grid-row: span 3; }
```
