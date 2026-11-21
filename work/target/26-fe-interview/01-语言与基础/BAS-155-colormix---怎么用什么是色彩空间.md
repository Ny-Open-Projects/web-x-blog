---
title: [BAS-155] color-mix() 怎么用？什么是色彩空间？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-155：color-mix() 怎么用？什么是色彩空间？
**答**：
- color-mix(in 空间, 颜色A 百分比, 颜色B)：按指定插值空间混合两个颜色，省去手算 hover/边框色值。
- in 后面是插值空间：srgb 传统混色、oklch/oklab 感知均匀（过渡更自然）、hsl 常用于调饱和度。
- 色彩空间决定"两点之间怎么连线"，不同空间同样配比混出的颜色不同。

```css
.btn {
  color: color-mix(in srgb, teal 70%, white);   /* 七成 teal 掺白 */
  border: 1px solid color-mix(in oklch, crimson, black 20%); /* 感知更均匀的暗色 */
  background: color-mix(in oklch, currentColor, transparent 85%); /* 弱化底色 */
}
```
