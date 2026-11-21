---
title: [ARC-029] Design Token 体系如何做三层设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-029：Design Token 体系如何做三层设计？
**答**：
- 三层：基础 Token（原子值：色板/字号阶梯）→ 语义 Token（意图：`color-bg-primary`、`space-md`）→ 组件 Token（`button-bg-primary`）。
- 关键是组件只允许消费组件 Token 或语义 Token，禁止直连基础 Token——换主题/换品牌只改语义层映射。
- Token 源用 JSON/TS 单一事实源，构建时生成 CSS 变量、SCSS、TS 常量与小程序/Flutter 映射。

```typescript
// tokens/seed.ts —— 第一层：基础 Token（原子值，无语义）
export const base = {
  'blue-6': '#1677ff', 'blue-7': '#0958d9',
  'gray-1': '#ffffff', 'gray-3': '#f5f5f5', 'gray-9': '#434343',
  'size-4': '16px', 'radius-2': '4px', 'font-size-1': '12px',
};

// tokens/semantic.ts —— 第二层：语义 Token（意图层，主题切换只动这里）
export const semantic = {
  light: { 'color-bg-primary': base['gray-1'], 'color-text-primary': base['gray-9'],
           'color-brand': base['blue-6'], 'space-md': base['size-4'] },
  dark:  { 'color-bg-primary': '#141414', 'color-text-primary': '#e8e8e8',
           'color-brand': base['blue-6'], 'space-md': base['size-4'] },
};

// tokens/button.ts —— 第三层：组件 Token（组件只消费这一层）
export const buttonToken = {
  'button-bg': semantic.light['color-brand'],
  'button-radius': base['radius-2'],
  'button-font-size': base['font-size-1'],
};
```
