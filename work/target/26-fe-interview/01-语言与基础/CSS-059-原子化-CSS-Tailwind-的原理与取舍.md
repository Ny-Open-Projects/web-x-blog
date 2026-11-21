---
title: [CSS-059] 原子化 CSS（Tailwind）的原理与取舍？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-059：原子化 CSS（Tailwind）的原理与取舍？

**答**：
- 每个工具类只包含一条 CSS 声明（如 .flex、.pt-4），页面里按需组合，类名即样式。
- JIT 按需生成：扫描模板字符串中出现过的类名，只产出用到的 CSS，产物极小。
- 优点：无命名负担、样式一致性强（设计 token 约束）、删组件即删样式。
- 缺点：HTML 侵入性强、复杂状态类名冗长、团队需适应“不再写语义化 class”。

```html
<!-- Tailwind：类名组合 -->
<button class="inline-flex items-center gap-2 rounded-md bg-blue-500
               px-4 py-2 text-sm font-medium text-white
               hover:bg-blue-600 disabled:opacity-50">
  提交
</button>

<!-- 复杂状态可用 @apply 收敛到组件层 -->
<style>
  .btn-submit {
    @apply inline-flex items-center rounded-md bg-blue-500 px-4 py-2 text-white hover:bg-blue-600;
  }
</style>
```

```javascript
// tailwind.config.js：设计 token 约束
export default {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: { brand: '#409eff' },
      spacing: { 4.5: '18px' },
    },
  },
};
```
