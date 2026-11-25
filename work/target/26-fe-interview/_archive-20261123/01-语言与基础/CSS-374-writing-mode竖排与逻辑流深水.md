---
title: [CSS-374] writing-mode 深水：竖排、逻辑流与旋转布局
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-374：writing-mode 深水：竖排、逻辑流与旋转布局

**答**：
- writing-mode 三态：horizontal-tb（默认）、vertical-rl（竖排从右到左，中文/日文）、vertical-lr——它改变的不只是方向，是整个「内联轴/块轴」定义，逻辑属性全部随之旋转
- 应用场景：竖排标题（中式设计）、侧边标签文字、日历周标题竖排——配合 text-orientation（upright 中文直立/mixed）与 text-combine-upright（数字竖排压缩）
- 与 transform 旋转的区别：writing-mode 是真排版（文本可选/可搜索/换行正确），rotate 只是视觉旋转（布局仍占横排盒子）——需要文本语义的竖排必须 writing-mode
- 布局影响：竖排容器内 flex/grid 轴向旋转（row 变竖向），绝对定位逻辑 inset 变化——竖排组件内继续用逻辑属性保证一致性
- 性能：竖排文本 shaping 与换行计算走不同代码路径，大量竖排文本（整页）在中端机有可感知成本，局部装饰性使用无碍

```css
.vertical-title {
  writing-mode: vertical-rl;
  text-orientation: upright;
  letter-spacing: 0.2em;
}
.v-date {
  writing-mode: vertical-rl;
  text-combine-upright: all;   /* "31" 压缩为单字符宽 */
  font-size: 12px;
}
/* 竖排内逻辑属性自动旋转 */
.vertical-nav { writing-mode: vertical-rl; }
.vertical-nav li { margin-block-end: 16px; }  /* 实际是竖向间距 */
```
