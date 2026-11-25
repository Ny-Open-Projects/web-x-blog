---
title: [CSS-223] @scope 是什么，与 BEM 的关系
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## CSS-223：@scope 是什么，与 BEM 的关系

**答**：
- @scope：把选择器的生效范围限制在某个 DOM 子树内，且有「就近优先」——距离根越近的样式权重越高
- 语法：`@scope (.card) to (.card-content)`——from 限定根、to 排除子树（坑边界）
- 对比 BEM：BEM 用命名约定防冲突（人肉），@scope 用语言机制防冲突（结构化）；scoped 样式随 DOM 结构走，重命名成本为零
- 就近优先实战：组件嵌套组件时，内层组件样式天然赢过外层的「全局穿透视」——解决深层选择器污染
- 兼容：Chrome 118+，其余浏览器推进中；Shadow DOM 是功能重叠的替代方案

```css
@scope (.article) to (.ad) {
  p { line-height: 1.8; }  /* 只影响 .article 内、.ad 外的 p */
}
@scope (.card) {
  :scope .title { font-weight: 600; }  /* :scope 指 scope 根 */
  img { border-radius: 8px; }
}
```
