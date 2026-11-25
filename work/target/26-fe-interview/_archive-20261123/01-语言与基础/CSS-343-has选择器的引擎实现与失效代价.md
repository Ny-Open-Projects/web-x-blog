---
title: [CSS-343] :has() 选择器的引擎实现与失效代价
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-343：:has() 选择器的引擎实现与失效代价

**答**：
- 匹配语义：`.a:has(.b)` 对每个候选 .a 做子树反查——引擎用「反向依赖标记」实现：.b 出现/消失时向上通知所有 :has 依赖祖先重算
- 失效代价结构：:has 的匹配结果取决于「别的元素」，所以删/插一个 .b 影响面是「其祖先链上所有 :has 规则」+ 这些祖先的样式失效——比普通后代选择器失效面大
- 性能规范：限制 :has 查询深度与范围（`.card:has(img)` OK，`body:has(.x)` 全页反查危险）；避免 :has 与 :nth-child 组合的高频变动列表；列表项内部局部 :has 是安全区
- 强力场景仍值得用：表单前置校验样式（`form:has(:invalid) button`）、卡片任意子元素态驱动容器态——这些过去要 JS，现在纯 CSS，省 JS 失效面其实更小
- 嵌套限制：:has 内不能嵌 :has（规范禁止，防止组合爆炸）；不支持 :has 的内核优雅降级（整条规则丢弃）

```css
/* 安全: 局部反查 */
.card:has(img) { grid-template-columns: 1fr 2fr; }
/* 危险: 全页反查, 任何 .x 变动都全页通知 */
body:has(.x) .layout { --x: 1; }
/* 强力场景: 表单态驱动按钮 */
form:has(input:user-invalid) .submit { opacity: .5; pointer-events: none; }
```
