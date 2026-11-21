---
title: [CSS-272] mix-blend-mode 与 isolation：常见效果
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 效果]
type: 面试题
---

## CSS-272：mix-blend-mode 与 isolation：常见效果

**答**：
- mix-blend-mode：元素与下层像素做合成运算（multiply 正片叠底、screen 滤色、difference 差值、overlay 叠加…）
- 经典效果：深色文字穿过彩色背景自动反色（difference）、图片与色块混合调色、发光叠加（screen）
- isolation 的问题：blend 影响的是「整个层叠上下文」——子元素 blend 会穿透到祖先背景；父元素 isolation: isolate 圈定混合范围
- 排障高频：blend「没生效/乱生效」九成是上下文范围问题——先找最近的 stacking context
- 性能：blend 触发合成，大面积使用耗 GPU；避免每帧变化的 blend 区域过大

```css
.hero { position: relative; isolation: isolate; } /* 圈定混合域 */
.hero-title {
  mix-blend-mode: difference; color: white; /* 与背景差值，自动可读 */
}
.tint img { mix-blend-mode: luminosity; }    /* 上色滤镜效果 */
```
