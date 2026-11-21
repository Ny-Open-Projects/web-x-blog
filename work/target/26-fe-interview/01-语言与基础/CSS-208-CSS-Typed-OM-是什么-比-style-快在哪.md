---
title: [CSS-208] CSS Typed OM 是什么，比 style 操作快在哪
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, Houdini]
type: 面试题
---

## CSS-208：CSS Typed OM 是什么，比 style 操作快在哪

**答**：
- Typed OM：`el.attributeStyleMap` / `el.computedStyleMap()` 返回「类型化的 CSS 值对象」（CSSUnitValue），不是字符串
- 快的原因：字符串每次读写都要解析/序列化；Typed OM 直接持有数值对象，省解析成本，且数值可直接参与运算
- API 示例：`el.attributeStyleMap.set('width', CSS.px(100))`、`get('width').value` 直接拿数字
- 单位运算：`CSS.px(100).add(CSS.px(20))`、`CSS.deg(45)` 等工厂函数
- 现状：Chromium 完整支持，Safari/Firefox 部分；生产中主要在 Houdini worklet 与动画库（motion one）内部使用

```javascript
const map = el.attributeStyleMap;
map.set('width', CSS.px(100));
const w = map.get('width');        // CSSUnitValue { value: 100, unit: 'px' }
console.log(w.value + 20);         // 数值运算，无需 parseFloat
map.set('opacity', CSS.number(0.5));
```
