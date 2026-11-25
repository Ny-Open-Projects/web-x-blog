---
title: [CSS-270] background-clip: text 渐变文字与兼容
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 效果]
type: 面试题
---

## CSS-270：background-clip: text：渐变文字与兼容

**答**：
- 配方：`background: linear-gradient(...); -webkit-background-clip: text; color: transparent;`——背景只在文字形状内显示
- 标准化：Chrome 120+ 已支持无前缀 background-clip: text，但 -webkit- 前缀仍需保留（Safari）
- 动态化：配合 @property 动画渐变角度 = 流动渐变文字；配合 background-position 动画做扫光
- 坑：color: transparent 后 text-shadow 会穿透显示——阴影用 filter: drop-shadow 替代；不可选中区域问题（selection）
- 面试钩子：知道「前缀与标准的双写」和「text-shadow 失效」两个细节是实战标志

```css
.gradient-text {
  background: linear-gradient(90deg, #4285f4, #ea4335, #4285f4);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: flow 3s linear infinite;
}
@keyframes flow { to { background-position: 200% 0; } }
```
