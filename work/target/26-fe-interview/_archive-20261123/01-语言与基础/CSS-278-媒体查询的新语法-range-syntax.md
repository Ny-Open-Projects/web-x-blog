---
title: [CSS-278] 媒体查询的新语法：range syntax
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 兼容]
type: 面试题
---

## CSS-278：媒体查询的新语法（range syntax）

**答**：
- 新写法：`@media (400px <= width <= 768px)`——数学不等式风格，替代 (min-width)/(max-width) 的「min/max 反直觉」
- 优点：区间语义直读、杜绝「min 768 与 max 767.98 的边界缝隙」类 bug
- 兼容：Chrome 104+/Safari 16.4+/Firefox 102+；构建期可用 postcss 转旧语法
- 配套新特性：@custom-media 提案（命名断点）仍在草案；现实替代是 CSS 变量存断点值 + 预处理器
- 面试话术：能写出两端闭区间语法并说出「边界缝隙」问题即为熟悉

```css
/* 旧 */
@media (min-width: 768px) and (max-width: 1023px) { … }
/* 新 */
@media (768px <= width < 1024px) { … }

/* 断点全表 */
@media (width < 640px) { … }        /* 小屏 */
@media (640px <= width < 1024px) { … } /* 中屏 */
```
