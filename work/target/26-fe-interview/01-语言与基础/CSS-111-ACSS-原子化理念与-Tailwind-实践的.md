---
title: [CSS-111] ACSS/原子化理念与 Tailwind 实践的取舍是什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-111：ACSS/原子化理念与 Tailwind 实践的取舍是什么？

**答**：
- ACSS：每个类一个职责（.mt-4、.text-sm），样式零冲突、产物可按需、删除模板即删除样式。
- 代价：HTML 类名冗长、语义丢失、复杂选择器（如兄弟联动）表达困难。
- Tailwind 实践取舍：原子类做"原子"，重复组合用组件抽象（React 组件/@apply）收口，而非无限复制。
- 动态拼接类名必须整串出现（白名单/safelist），否则 JIT 扫描不到。
- 适合中大型团队统一 token 与视觉节奏；小项目或强主题换肤场景成本收益需评估。

```javascript
// tailwind 配置：token 即配置，团队视觉一致性来源
export default {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  safelist: [{ pattern: /^bg-(blue|red|green)-(100|500|900)$/ }], // 动态类白名单
  theme: {
    extend: {
      spacing: { 18: '4.5rem' },
      colors: { brand: { DEFAULT: '#409eff', dark: '#2b7fd4' } },
    },
  },
};
```

```html
<!-- 原子类组合，重复组合交给组件抽象 -->
<button class="inline-flex items-center gap-1 rounded bg-brand px-4 py-2
               text-white text-sm font-medium hover:bg-brand-dark
               disabled:opacity-50">
  确定
</button>
```
