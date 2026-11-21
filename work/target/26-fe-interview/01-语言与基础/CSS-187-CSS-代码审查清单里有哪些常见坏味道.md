---
title: [CSS-187] CSS 代码审查清单里有哪些常见坏味道？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-187：CSS 代码审查清单里有哪些常见坏味道？

**答**：
- `!important` 超过个位数：优先级战争失控，应改用 @layer 与选择器结构治理。
- 深层后代选择器（4 层以上）：与 DOM 结构强耦合，复用为 0，应提取语义类。
- 魔法数字（负 margin 微调、离谱 z-index）：用 token 与白名单约束。
- 死代码：无人引用的类、注释掉的样式块、重复声明未使用的变量——靠 stylelint 与覆盖率工具清出。

```css
/* 坏味道 1：important 战争 */
.x { color: red !important; }
.x.y { color: blue !important; }

/* 坏味道 2：结构耦合的深嵌套 */
.sidebar .content ul li a span { font-size: 12px; }

/* 坏味道 3：魔法数字 */
.modal { margin-top: -37px; }        /* 为什么是 37 */
.z-fix { z-index: 99999; }

/* 坏味道 4：死代码与重复 token */
:root { --old-brand: #09f; }         /* 无人引用 */
.unused-legacy { float: left; }      /* 已无 DOM 使用 */

/* 对应的整改写法 */
.sidebar-link { font-size: var(--fs-sm, 12px); }      /* 语义类 + token */
.modal-offset { margin-top: calc(-1 * var(--header-h)); } /* 派生而非凑数 */
/* z-index 白名单交给 stylelint 约束（见 CSS-190） */
```
