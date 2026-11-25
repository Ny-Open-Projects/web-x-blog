---
title: [CSS-358] CSS 架构演进：BEM、原子化与层级的失效视角
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-358：CSS 架构演进：BEM、原子化与层级的失效视角

**答**：
- 评估框架的新维度是「引擎失效面」：样式改动影响多少元素重算、ComputedStyle 共享命中率多少——BEM 单类名命中共享、深层嵌套选择器破坏共享
- BEM 优劣：命名隔离清晰、选择器短（单 class 匹配快）；代价是类名冗长、组合状态靠 BEM 修饰符堆叠
- 原子化（Tailwind/uno）：class 数量固定有限集 → 引擎 StyleSharing 高命中、无 CSS 体积增长（按需生成）；代价 HTML 冗长与语义弱——用 @apply/组件封装收敛
- 级联层 + 架构：@layer 治理「reset/base/utilities」优先级，配合任一命名方案；现代方案 = 原子化 or BEM + layers + CSS 变量 token
- 团队落地：样式架构要写进 ADR（命名方案/层顺序/token 分层/禁用模式如深层嵌套选择器），lint 强制（stylelint 规则）

```text
失效面对比:
  .card__title            单类 → 命中共享, 最便宜
  .card .card__title.is-a 后代+状态 → 失效面大
  .p-4.text-sm            原子类固定集 → 共享命中极高
  内联 style              跳过匹配但每元素独立, 无共享
结论: 短选择器 + 稳定类名集 = 引擎友好
```
