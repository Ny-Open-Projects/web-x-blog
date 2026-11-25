---
title: [CSS-380] CSS 解析容错进阶：错误恢复规则与新语法降级
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-380：CSS 解析容错进阶：错误恢复规则与新语法降级

**答**：
- 声明级容错：属性名未知/值非法 → 丢弃该声明，继续解析同块其他声明——vendor 前缀与实验属性天然安全
- 规则级容错：选择器列表中任一选择器非法 → 整条规则丢弃（不是跳过该选择器）——`:has()` 在老内核之所以「整条失效」，若想部分降级要拆分规则
- 块级容错：不匹配的 {} 块、引号未闭合按规范恢复点跳过——压缩器错误换行可能触发大段丢失（构建产物要 lint 校验）
- @ 规则容错：未知的 at-rule 整块跳过到匹配结束；@supports/@media 内规则正常解析（条件不匹配不生效）——渐进增强的语法基础
- 新语法发布策略：全新属性（oklch）老内核丢声明可用 fallback 双写；新选择器（:has）老内核丢整条要用 @supports 包裹重写降级版本

```css
/* fallback 双写: 老内核保留前者 */
.badge { color: #1677ff; color: oklch(0.62 0.19 255); }
/* :has 降级: JS 兜底 */
.card--has-img { grid-template-columns: 1fr 2fr; }
@supports selector(:has(img)) {
  .card:has(img) { grid-template-columns: 1fr 2fr; }  /* 支持时用标准写法 */
}
```
