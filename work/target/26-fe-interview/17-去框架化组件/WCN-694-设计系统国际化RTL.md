---
title: [WCN-694] 设计系统如何支持国际化与 RTL（从右到左）布局？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-694：设计系统如何支持国际化与 RTL（从右到左）布局？

**答**：
- 结论：用逻辑属性（margin-inline-start / padding-inline）替代物理属性（left/right）；图标与箭头按 dir 镜像；文案外置 i18n 资源；布局用 flex/grid 自然适配。
- 做法：CSS 用 :dir(rtl) 或 [dir=rtl] 钩子；组件内部避免硬编码 left/right；有方向性图标用 transform: scaleX(-1)。
- 追问钩子：数字与日期怎么处理？用 Intl API 按 locale 格式化——考察对「国际化不仅是翻译」的理解。

```javascript
// 逻辑属性：自动适配 LTR/RTL
const css = `
.ds-item { margin-inline-start: 8px; padding-inline-end: 12px; }
.ds-arrow { transform: scaleX(1); }
[dir="rtl"] .ds-arrow { transform: scaleX(-1); }
`;
function formatPrice(n, locale) {
  return new Intl.NumberFormat(locale, {
    style: 'currency', currency: locale === 'ar' ? 'AED' : 'USD',
  }).format(n);
}
console.log(formatPrice(1234.5, 'en-US'));
console.log(formatPrice(1234.5, 'ar-EG')); // 本地化数字与货币
```
