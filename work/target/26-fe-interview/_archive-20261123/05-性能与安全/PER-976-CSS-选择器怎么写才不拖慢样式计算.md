---
title: [PER-976] CSS 选择器怎么写才不拖慢样式计算
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-976：CSS 选择器怎么写才不拖慢样式计算

**答**：
- 现代引擎匹配从右向左且高度优化，"后代选择器慢"的老结论已弱化，真正的问题是：失效范围与匹配元素数。
- 避免：* 通配 + 复合伪类（:is 嵌套深）、属性选择器在大容器上的后代匹配、频繁变更的父级类名驱动大量后代样式。
- 偏好：class 直接命中、CSS 变量做主题切换、@layer 组织优先级减少级联重算。
- 度量：DevTools "Recalculate Style" 的 affected 元素数是唯一可信依据，凭感觉优化常是伪优化。

```javascript
/* 反模式：父类切换导致全列表失效 */
.theme-dark .card .title span em { color: #eee; }
/* 改良：变量切换，无结构级失效 */
.card { color: var(--text); background: var(--bg); }
:root { --text: #222; --bg: #fff; }
:root.theme-dark { --text: #eee; --bg: #111; }
/* :is 的代价示例：匹配集合大时慎用 */
/* 反 */ :is(#app, #root) :is(.a, .b) :is(x, y, z) { ... }
```
