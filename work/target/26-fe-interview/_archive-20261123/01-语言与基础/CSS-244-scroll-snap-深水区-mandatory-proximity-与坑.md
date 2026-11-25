---
title: [CSS-244] scroll-snap 深水区：mandatory/proximity 与常见坑
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 滚动]
type: 面试题
---

## CSS-244：scroll-snap 深水区：mandatory/proximity 与常见坑

**答**：
- scroll-snap-type 两档：mandatory（强制吸附，滚不进两卡之间）与 proximity（靠近才吸）——列表类用 proximity 防误吸，轮播用 mandatory
- 对齐方式：snap-align start/center/end 对应吸附点位置；scroll-padding 在容器侧留出（吸附点偏移）、scroll-margin 在子项侧
- 高频坑：mandatory + 内容高过视口的子项 → 无法浏览子项内部（解决：子项内层再开 snap 或用 proximity）；snap 容器与 sticky 组合的偏移
- 无障碍：mandatory 会「抢滚动权」，弱网低端机的惯性滚动被截断——内容型页面慎用 mandatory
- 配套：scroll-snap-stop: always 防一次惯性滑过多卡

```css
.carousel {
  display: flex; overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding-left: 16px;
}
.carousel > * {
  scroll-snap-align: start;
  scroll-snap-stop: always;
  scroll-margin-left: 16px;
}
```
