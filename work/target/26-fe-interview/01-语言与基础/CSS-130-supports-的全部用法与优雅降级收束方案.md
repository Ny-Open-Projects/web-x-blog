---
title: [CSS-130] @supports 的全部用法与优雅降级收束方案？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-130：@supports 的全部用法与优雅降级收束方案？

**答**：
- 基本形：`@supports (display: grid)`；否定：`not`；组合：`and / or` 括号分组。
- 选择器检测：`@supports selector(:has(a))` / `selector(::part(x))`，判断新选择器可用性。
- 工程模式：默认写"基线样式保证可用"，`@supports` 内只放增强分支——所有增强都是增益而非依赖。
- 与 caniuse/Browserslist 联动：构建期决定 polyfill 与前缀，运行期 @supports 处理"能检测到的能力"。
- 收束原则：能力检测优先于 UA 嗅探；降级路径必须有 QA 验证；文档化每个增强分支的最低版本。

```css
/* 1. 增强分支：Grid 可用才上 Grid，否则默认块级布局兜底 */
.layout { display: block; }
@supports (display: grid) {
  .layout {
    display: grid;
    grid-template-columns: 240px minmax(0, 1fr);
  }
}

/* 2. 组合与否定 */
@supports not (backdrop-filter: blur(1px)) {
  .glass { background: var(--bg-surface); } /* 降级：不透明底 */
}
@supports (color: oklch(0.7 0.1 200)) and (selector(:has(*))) {
  .next-gen { /* 新能力组合生效区 */ }
}

/* 3. JS 侧同一套能力检测，行为与 CSS 对齐 */
if (CSS.supports('display', 'grid')) initGridLayout();
```

## 二十二、经典布局题全解
