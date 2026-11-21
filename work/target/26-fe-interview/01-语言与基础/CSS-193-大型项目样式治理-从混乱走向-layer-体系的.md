---
title: [CSS-193] 大型项目样式治理，从混乱走向 @layer 体系的路线是什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-193：大型项目样式治理，从混乱走向 @layer 体系的路线是什么？

**答**：
- 路线五步：审计现状（重复度/优先级战争/死代码）→ 建立 token → 用 @layer 建立层级框架 → 存量样式整体沉入 legacy 层 → 门禁固化（stylelint + CI）。
- @layer 的战略价值：层级顺序声明一次，全站覆盖关系可预期，`!important` 从机制上失去必要性。
- 存量迁移零风险：旧规则原样搬进 legacy 层（优先级最低），新体系天然赢，逐模块搬迁无需一次性重构。
- 终态：reset < base < legacy < components < utilities，utilities 放最外层保证工具类永远可覆盖。

```css
/* 1. 层级框架：顺序即优先级，全站只声明一次 */
@layer reset, base, legacy, components, utilities;

/* 2. reset 层：最低优先级 */
@layer reset {
  *, *::before, *::after { box-sizing: border-box; margin: 0; }
}

/* 3. base 层：元素级默认 */
@layer base {
  body { font: 14px/1.5 var(--font-sans); color: var(--fg); }
}

/* 4. legacy 层：存量样式原样搬入，优先级低于新体系，逐步退役 */
@layer legacy {
  .old-card { float: left; width: 220px; background: #eee; }
}

/* 5. components 层：只消费 token 的新组件 */
@layer components {
  .btn { padding: calc(var(--gap) / 2) var(--gap); border-radius: var(--radius); }
}

/* 6. utilities 层：最高，工具类永远能覆盖组件 */
@layer utilities {
  .p-4 { padding: var(--gap); }
  .hidden { display: none !important; }  /* 收敛后仅此一处允许 important */
}
```
