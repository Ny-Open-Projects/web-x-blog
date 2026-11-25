---
title: [CSS-377] ComputedStyle 共享：命中条件与破坏因素
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-377：ComputedStyle 共享：命中条件与破坏因素

**答**：
- 共享机制：相同 tag/class/id/属性集/继承状态的兄弟元素可复用同一份 ComputedStyle 对象——样式重算时未失效的共享元素直接跳过，是列表渲染快的关键
- 破坏因素：任何「区分度」都会破坏共享——不同 class、style 内联差异、:hover/:focus 等状态（一个 hover 状态使该元素独立）、nth-child 相关规则、属性选择器匹配差异、animation 不同步
- 实战含义：列表项保持 class 集一致（状态类挂在包装层而不是列表项）、列表样式避免 nth-child 与属性选择器、hover 效果加在少量元素——千行列表的重算从 O(n) 降到 O(1) 的原理
- 验证方式：Performance 面板 Recalculate Style 的「Elements Affected」，对比改动前后的受影响元素数；Chrome 还可看 style sharing 命中（内部 trace）
- 与 CSS-in-JS/原子化的关系：原子化 class 稳定集合利于共享；运行时 styled 随机 class + 动态 style 内联会大面积破坏共享——引擎视角是选型硬指标

```css
/* 破坏共享: 列表项用 nth-child */
li:nth-child(odd) { background: #fafafa; }
/* 保持共享: 斑马纹挂容器或用表格原生 */
/* hover 状态: 只加在交互元素而非全部列表项 */
li:hover .btn { color: red; }  /* li 本身保持无状态 → 共享不破坏 */
```
