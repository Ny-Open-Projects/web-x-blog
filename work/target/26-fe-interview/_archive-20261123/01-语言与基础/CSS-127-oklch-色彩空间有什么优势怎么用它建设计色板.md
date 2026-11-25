---
title: [CSS-127] oklch 色彩空间有什么优势？怎么用它建设计色板？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-127：oklch 色彩空间有什么优势？怎么用它建设计色板？

**答**：
- oklch 三轴：L 感知亮度、C 彩度、H 色相；同 L 值的颜色"看起来一样亮"，这是 sRGB/hsl 做不到的。
- 等亮度性让无障碍对比度可预测：L 固定阶梯生成色阶，WCAG 对比度控制从试错变成计算。
- 广色域：可表达 P3 范围颜色，过渡插值更平滑不发灰。
- 工程实践：主色定 oklch(L C H)，同 C/H 变 L 生成 50~900 色阶，语义 token 引用色阶。
- 需要兼容 sRGB 时由浏览器自动映射降级，无需手动双写。

```css
/* 品牌主色与等亮度色阶：只动 L，C/H 不变 */
:root {
  --brand-500: oklch(0.62 0.19 255);   /* 主色 */
  --brand-100: oklch(0.92 0.05 255);   /* 同色相提亮 */
  --brand-700: oklch(0.45 0.17 255);   /* 同色相压暗，文字可读 */
  --brand-900: oklch(0.3 0.12 255);
}

/* 语义 token：白字按钮用 700 保证对比度 */
.btn-primary {
  background: var(--brand-500);
  color: white;
}
.btn-primary:hover { background: var(--brand-700); }

/* 互补色/邻近色：只转 H */
:root {
  --accent-complement: oklch(0.62 0.19 calc(255 + 180));
}
```
