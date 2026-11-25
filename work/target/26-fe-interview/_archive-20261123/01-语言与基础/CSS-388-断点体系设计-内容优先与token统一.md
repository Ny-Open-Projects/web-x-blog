---
title: [CSS-388] 断点体系设计：内容优先与 token 统一
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 适配]
type: 面试题
---

## CSS-388：断点体系设计：内容优先与 token 统一

**答**：
- 内容优先断点：断点由「内容可容纳宽度」决定（卡片双列的最小合理宽度）而不是设备清单——设备会变，内容约束稳定
- 断点数量纪律：3~4 个主断点 + 组件级容器查询分摊——全局断点越多，窗口 resize 的重匹配成本与设计维护成本越高
- token 统一：断点值与栅格/间距同源管理（Tailwind theme/自研 token 表），JS 侧（JS-in-CSS 或 CSS.supports 读取）与 CSS 侧共用——JS 判断「当前档位」用 matchMedia 监听与 CSS 断点严格对齐
- 区间语义：min-width 渐进（mobile-first）为主；避免 max-width 混用造成规则交叉——必须用 max 时配合 @layer 收敛优先级
- 测试矩阵：断点边界 ±1px 截图（临界值最容易错）、旋转屏、折叠屏中间态——断点边界是视觉回归必测点

```css
:root {
  --bp-sm: 480px; --bp-md: 768px; --bp-lg: 1200px;
}
@media (min-width: 768px) { .layout { grid-template-columns: 2fr 1fr; } }
/* JS 侧对齐 */
const mq = matchMedia('(min-width: 768px)');   // 与 token 同值
mq.addEventListener('change', syncLayoutMode);
```
