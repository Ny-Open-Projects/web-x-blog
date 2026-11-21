---
title: [CSS-123] :has() 的兼容策略与渐进增强怎么做？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-123：:has() 的兼容策略与渐进增强怎么做？

**答**：
- Baseline 2023：Chrome 105+ / Safari 15.4+ / Firefox 121+ 均已支持，主要缺口在老旧国内内核。
- 检测：`@supports selector(:has(*))` 精确判断（注意 `@supports (:has(a))` 写法跨浏览器有坑，用 selector() 包裹最稳）。
- 增强模式：无 :has() 时功能正常但缺少"联动美化"；有 :has() 时增强为纯 CSS 联动。
- 关键交互（显隐/校验）不要只依赖 :has()，用 JS 加 data 属性双保险。
- 降级思路与 :focus-visible、容器查询一致：能力检测 + 基础可用 + 增强分支。

```css
/* 增强：表单错误联动（支持 :has 的浏览器） */
@supports selector(:has(*)) {
  .field:has(input:user-invalid) { border-color: var(--color-danger); }
}

/* 基础：所有浏览器都保留 JS 驱动的 data-state 通道 */
.field[data-invalid] { border-color: var(--color-danger); }
```

```javascript
// JS 兜底：不支持 :has 的环境监听事件改 data 属性
if (!CSS.supports('selector(:has(*))')) {
  input.addEventListener('input', () => {
    field.dataset.invalid = String(!input.checkValidity() && input.matches(':user-invalid'));
  });
}
```
