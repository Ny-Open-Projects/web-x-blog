---
title: [CSS-341] 字体渲染深水：shaping、亚像素与提层文本模糊
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-341：字体渲染深水：shaping、亚像素与提层文本模糊

**答**：
- 文本 shaping：字形选择（ligature 连字/kerning 字距/OpenType 特性 font-feature-settings）在文本 shaping 阶段完成——改变这些属性触发该文本块重新 shaping + layout，代价高于普通样式改动
- 亚像素与提层模糊：元素提升为合成层后，文本按层位图栅格化——非整数 transform 位移/缩放会让文本模糊（栅格后再几何变换）；修复是保持整数像素定位、动画结束回位后移除 will-change 让文本回到普通栅格
- text-rendering：optimizeLegibility 会开启 kerning/ligature 全量计算（大文本性能差），移动端默认 geometricPrecision 在部分内核更贵——长文正常不设或用 auto
- 抗锯齿差异：-webkit-font-smoothing: antialiased 让细字更细（macOS 设计稿常见诉求），Windows 无效；中文字体灰阶渲染 vs ClearType 心智差异是设计还原争议源
- 可变字体：font-variation-settings 动画触发重新 shaping（比 weight transition 更贵但可插值），中轴 wght 动画用 font-weight 过渡（现代内核可合成）

```css
/* 文本模糊修复 */
.blurry {
  transform: translate(0.5px, 0);           /* 非整数 → 提层栅格模糊 */
}
.blurry-fixed {
  transform: translate(0, 0);               /* 整数像素 */
  will-change: auto;                        /* 动画后释放, 文本回普通栅格 */
}
/* OpenType 特性 */
.num { font-feature-settings: 'tnum' 1; }   /* 等宽数字, 表格场景 */
```
