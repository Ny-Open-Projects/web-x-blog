---
title: [CSS-095] filter 与 backdrop-filter 毛玻璃怎么用？性能上要注意什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-095：filter 与 backdrop-filter 毛玻璃怎么用？性能上要注意什么？

**答**：
- `filter` 作用于元素自身渲染结果；`backdrop-filter` 作用于元素"背后的内容"，毛玻璃即 blur + 半透明背景。
- backdrop-filter 会截取背后区域并逐帧重采样，大面积使用或放在滚动容器内代价显著。
- 控制成本：限定小面积（导航、弹窗头部），加 `border-radius` 与 `contain` 减少重采样范围，避免与 fixed 大背景叠加。
- backdrop-filter 会为元素创建合成层，多个实例叠在长列表滚动区是最常见的卡顿来源。
- 提供无模糊降级：`@supports not` 时加深背景透明度保证可读性。

```css
/* 毛玻璃导航：限定高度的小面积使用 */
.glass-nav {
  position: sticky; top: 0;
  background: color-mix(in srgb, var(--bg-surface) 65%, transparent);
  backdrop-filter: blur(12px) saturate(1.4);
  -webkit-backdrop-filter: blur(12px) saturate(1.4);
}

@supports not (backdrop-filter: blur(1px)) {
  .glass-nav { background: var(--bg-surface); } /* 降级：不透明背景保证对比度 */
}

/* 反例警示：不要在长列表每一项上用 backdrop-filter
.list-item { backdrop-filter: blur(8px); }  ← 滚动时逐项重采样，必然掉帧 */
```

## 十七、文字排版
