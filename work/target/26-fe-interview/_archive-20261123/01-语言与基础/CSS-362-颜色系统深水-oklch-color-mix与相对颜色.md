---
title: [CSS-362] 颜色系统深水：oklch、color-mix 与相对颜色
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-362：颜色系统深水：oklch、color-mix 与相对颜色

**答**：
- 色彩空间演进：sRGB(hex/rgb) → Display-P3（广色域，屏幕支持时更鲜艳）→ oklch（感知均匀：亮度 L 独立于色相，同 L 值视觉等亮）——token 色阶用 oklch 生成的阶差人眼一致
- oklch 的工程价值：程序化生成色阶（固定 L 调 C/H）替代人工调色；对比度可预测（L 直接相关）；color(display-p3 ...) 与 sRGB 回退双轨声明
- color-mix()：运行时混色（透明度变体/悬停加深不再需要预设 token）——`color-mix(in oklab, var(--primary) 85%, black)`；派生色统一走 mix 保证一致性
- 相对颜色语法（relative color syntax）：`--hover: oklch(from var(--primary) calc(l*0.9) c h)` 从现有色派生——主题系统从「每组色手工配」转向「单一基色派生」
- 注意 srgb 线性与显示色域：转换发生在计算时，渐变插值空间（in oklab）决定中间色是否发灰——渐变默认 sRGB 插值在两侧饱和色间会灰，改 in oklch 解决

```css
:root {
  --primary: oklch(0.62 0.19 255);
  --primary-hover: oklch(from var(--primary) calc(l * 0.9) c h);
  --primary-bg: color-mix(in oklab, var(--primary) 12%, white);
}
.grad {
  background: linear-gradient(in oklch, var(--primary), #ff8a00); /* 避免中段发灰 */
}
@supports (color: color(display-p3 1 1 1)) {
  :root { --primary: color(display-p3 0.2 0.45 1); }
}
```
