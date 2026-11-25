---
title: [CSS-195] @supports 渐进增强的实战实例集？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-195：@supports 渐进增强的实战实例集？

**答**：
- 总范式：基线样式写在 @supports 外保证可用，每个增强分支独立成块、独立失效、互不依赖。
- 增强 1：backdrop-filter 毛玻璃降级为半透明纯色；增强 2：:has 父级联动（表单校验态）；增强 3：animation-timeline 滚动驱动。
- 选择器检测 `@supports selector(:has(*))` 与属性检测组合使用；JS 侧用 CSS.supports 保持同一判断。
- 降级分支必须有 QA 覆盖：增强失效时的页面就是大量老用户看到的页面。

```css
/* 基线：所有目标浏览器可用 */
.glass { background: rgba(255, 255, 255, .9); }
.form .submit { opacity: 1; }

/* 增强 1：毛玻璃，不支持则保持基线半透明 */
@supports (backdrop-filter: blur(8px)) {
  .glass {
    background: rgba(255, 255, 255, .6);
    backdrop-filter: blur(8px);
  }
}

/* 增强 2：:has 表单联动，不支持时按钮永远可点 */
@supports selector(:has(*)) {
  .form:has(input:invalid) .submit {
    opacity: .5;
    pointer-events: none;
  }
}

/* 增强 3：滚动驱动动画，不支持则回到 JS/普通动画 */
@supports (animation-timeline: scroll()) {
  .progress-bar {
    animation: grow linear;
    animation-timeline: scroll();
  }
  @keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }
}

/* JS 侧同一套检测，行为对齐 */
if (CSS.supports('backdrop-filter', 'blur(8px')) initGlass();
```
