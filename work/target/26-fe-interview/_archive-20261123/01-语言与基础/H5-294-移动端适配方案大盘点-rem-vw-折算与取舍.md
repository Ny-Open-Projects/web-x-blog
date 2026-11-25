---
title: [H5-294] 移动端适配方案大盘点：rem/vw 与折算取舍
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 移动端]
type: 面试题
---

## H5-294：移动端适配方案大盘点：rem/vw 与折算取舍

**答**：
- rem 方案：设计稿宽度换算成 rem（750 稿 / 10rem 基准），JS 动态设 html font-size 或用 postcss-pxtorem；兼容性最好，老项目主流
- vw 方案：设计稿尺寸直接换算成 vw（100vw=750px→1px=0.1333vw），纯 CSS 无 JS；精度更好（rem 有舍入误差），新项目主流
- 折算取舍：vw 的小屏文字会过小——文字仍用 px/rem，只有布局用 vw，混合策略最实用
- 现代补充：clamp() 夹逼（最小/理想/最大），兼顾桌面与移动，容器查询流行后「组件级适配」逐渐替代「页面级适配」
- 1px 问题与 safe-area 独立处理，不要塞进适配方案

```scss
// 设计稿 750px，px→vw 换算
$vw: 100 / 750 * 1vw;
.header { height: 88 * $vw; padding: 24 * $vw; }
.title { font-size: 28px; } /* 文字固定 px 防过小 */
.mid { font-size: clamp(14px, 28 * $vw, 28px); } /* 夹逼防极端 */
```
