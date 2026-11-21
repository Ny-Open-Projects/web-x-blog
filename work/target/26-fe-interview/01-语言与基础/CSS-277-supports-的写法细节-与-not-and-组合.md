---
title: [CSS-277] @supports 的写法细节与 not/and 组合
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 兼容]
type: 面试题
---

## CSS-277：@supports 的写法细节与 not/and 组合

**答**：
- @supports (属性: 值) 检测「声明是否被理解」；selector() 检测选择器支持——`@supports selector(:has(*))`
- 组合运算：not/and/or 可嵌套但每层条件要括号包裹——`@supports ((display: grid) and (not (display: inline-grid)))`
- 常用范式：正向渐进（新特性块内写增强）与反向降级（not 块内写回退）二选一，别两处都写全量
- 检测对象陷阱：检测的是「解析支持」不是「行为正确」——有些属性老版本「认得但实现有 bug」，@supports 防不住
- CSS.supports() JS API：运行时分支（加载 polyfill、切换实现）

```css
@supports selector(:has(*)) {
  .card:has(img) { grid-template-columns: 1fr 2fr; }
}
@supports not (backdrop-filter: blur(1px)) {
  .navbar { background: rgb(0 0 0 / .85); } /* 无毛玻璃时加深背景保证可读 */
}
```
```javascript
if (!CSS.supports('backdrop-filter', 'blur(1px)')) loadFallbackStyles();
```
