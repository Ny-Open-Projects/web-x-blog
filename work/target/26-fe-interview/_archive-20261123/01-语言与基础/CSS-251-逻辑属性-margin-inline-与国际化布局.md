---
title: [CSS-251] 逻辑属性 margin-inline 与国际化布局
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 国际化]
type: 面试题
---

## CSS-251：逻辑属性 margin-inline 与国际化布局

**答**：
- 物理属性（left/right）与「纸面方向」绑定；逻辑属性（inline/block 轴）与「书写方向」绑定——RTL（阿拉伯语）自动镜像
- 对照表：margin-left ↔ margin-inline-start、padding-right ↔ padding-inline-end、text-align: left ↔ text-align: start、border-left ↔ border-inline-start
- 收益：RTL/LTR 一套样式；vertical writing-mode（日文竖排）同样自动适配——物理属性在这些场景全错
- 迁移策略：新代码统一逻辑属性；存量用 postcss-logical 转换；图标类（不对称箭头）仍保留物理属性
- 面试话术：i18n 不是「多套样式表」，而是「属性层就把方向抽象掉」

```css
.card {
  padding-inline: 16px;          /* 左右（随方向镜像） */
  margin-block-end: 12px;        /* 下边距（竖排时为左侧） */
  text-align: start;             /* RTL 自动右对齐 */
  border-inline-start: 3px solid #4285f4;  /* 起始边强调线 */
}
[dir='rtl'] .icon-arrow { transform: scaleX(-1); } /* 不对称图标手动翻 */
```
