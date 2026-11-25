---
title: [CSS-196] CSS 命名冲突治理经历了哪几个阶段？最终如何收束？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-196：CSS 命名冲突治理经历了哪几个阶段？最终如何收束？

**答**：
- 阶段一全局裸类：必然冲突；阶段二 BEM 手工命名空间：靠约定，防冲突但选择器冗长。
- 阶段三 CSS Modules：构建期 hash 类名，import 即唯一，工程化主流；阶段四 Shadow DOM：运行时真隔离，成本最高。
- 收束（阶段五）：@layer 把“冲突解决”从命名层面转移到层级层面——同名类也能靠 layer 顺序裁决。
- 实践组合：Modules 管唯一性、layer 管覆盖关系、token 管值的一致性，三者互补而非互斥。

```css
/* 阶段一：全局裸类，谁后加载谁赢，冲突随机 */
.title { font-size: 20px; }

/* 阶段二：BEM 手工命名空间 */
.page-header__title--large { font-size: 28px; }

/* 阶段三：CSS Modules（构建期 hash）
   import styles from './header.module.css'
   .title 编译为 .Header_title__3xK，天然唯一 */
.header-title { font-size: 20px; }

/* 阶段四：Shadow DOM 运行时隔离（见 CSS-188） */

/* 阶段五：@layer 收束 —— 覆盖关系由层裁决，而非命名 */
@layer vendor, base, app;
@layer vendor  { .title { font-size: 20px; } }   /* 第三方样式 */
@layer base    { .title { font-size: 16px; } }
@layer app     { .title { font-size: 18px; } }   /* app 层必赢，无需更高优先级 */
```
