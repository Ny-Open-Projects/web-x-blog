---
title: [CSS-112] 运行时 CSS-in-JS 与 zero-runtime 方案的原理与趋势？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-112：运行时 CSS-in-JS 与 zero-runtime 方案的原理与趋势？

**答**：
- 运行时方案（styled-components/emotion）：组件渲染时拼出类名、注入 `<style>`，能力最强（props 驱动样式、主题上下文）。
- 代价：包体与运行时开销、SSR 需要样式抽取配合、React Server Components 场景受限（序列化不了闭包样式）。
- zero-runtime（vanilla-extract/linaria/panda）：构建期求值产出静态 CSS + 类型化类名/变量，运行时零成本。
- 趋势：React 官方明确建议 RSC 场景避免运行时 CSS-in-JS，社区向 zero-runtime 与 Tailwind 迁移。
- 选型：强动态主题/设计系统用 zero-runtime 类型化 token；轻量交互页面 Tailwind 或原生 @layer 足够。

```javascript
// zero-runtime 示例（vanilla-extract）：构建期执行，产物是静态 CSS
import { style, createVar } from '@vanilla-extract/css';

export const accentVar = createVar(); // 类型化 CSS 变量

export const button = style({
  background: accentVar,
  padding: '8px 16px',
  borderRadius: 8,
  selectors: {
    '&:hover': { filter: 'brightness(0.95)' },
    '&[data-disabled]': { opacity: 0.4, pointerEvents: 'none' },
  },
});
// 运行时拿到的 button 就是一个类名字符串，无任何运行时 CSS 引擎
```
