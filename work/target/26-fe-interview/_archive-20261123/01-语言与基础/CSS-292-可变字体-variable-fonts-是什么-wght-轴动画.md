---
title: [CSS-292] 可变字体（variable fonts）：wght 轴与动画
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 排版]
type: 面试题
---

## CSS-292：可变字体：wght 轴与动画

**答**：
- 可变字体：一个文件包含连续可调的轴（wght 字重、wdth 宽度、slnt 斜度、ital、opsz 光学尺寸）——替代多档字体文件
- font-variation-settings 直接设轴（低级 API）；推荐高级属性：font-weight/font-stretch/font-optical-sizing 自动映射轴
- 独有玩法：字重动画（wght 过渡 300→600）、悬停加粗呼吸——字重可以插值是可变字体独占能力
- 性能：单文件多字重总体积小于多个静态字体；但解析成本略高
- 兼容：全主流支持多年，可生产；动画需浏览器支持 variation 插值（现代均支持）

```css
.title {
  font-family: 'InterVar';
  font-weight: 400;
  transition: font-weight .3s;  /* 字重动画 */
}
.title:hover { font-weight: 600; }
.display {
  font-variation-settings: 'opsz' 48, 'wdth' 75; /* 低级轴控制 */
}
```
