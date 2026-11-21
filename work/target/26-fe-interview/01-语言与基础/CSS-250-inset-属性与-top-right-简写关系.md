---
title: [CSS-250] inset 属性与 top/right/bottom/left 的关系
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 基础]
type: 面试题
---

## CSS-250：inset 属性与 top/right/bottom/left 的关系

**答**：
- inset 是 top/right/bottom/left 的简写：`inset: 0` = 四边为 0；`inset: 10px 20px` = 上下 10、左右 20（顺时针两值规则同 margin）
- 逻辑属性对应：inset-inline-start（对应 left，写作方向敏感）、inset-block-start（对应 top）——国际化布局用逻辑属性
- 实用场景：遮罩层 `inset: 0`、全屏 fixed、绝对定位四边拉伸
- 与 transform 的分工：inset 决定「定位盒」，transform 做「动画位移」——动画用 transform 不改 inset（避免重排）
- 面试钩子：inset 只是简写糖，但搭配逻辑属性（inset-inline）后能写出方向无关的组件

```css
.overlay { position: fixed; inset: 0; background: rgb(0 0 0 / .5); }
.stretched { position: absolute; inset: 8px; }        /* 四边贴 8px */
[dir='rtl'] .badge { inset-inline-start: 8px; }        /* RTL 自动翻到右侧 */
```
