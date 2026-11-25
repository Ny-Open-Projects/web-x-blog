---
title: [CSS-329] CSSOM 构建与样式解析流水线
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-329：CSSOM 构建与样式解析流水线

**答**：
- 解析流水线：字节 → 字符 → 词法 token（at-rule/选择器/声明）→ 规则对象（CSSOM）→ 按 origin/importance/specificity 分桶备用——CSS 解析不阻塞 DOM 解析，但阻塞渲染（FOUC 防护靠关键 CSS 内联）
- 阻塞语义：浏览器会阻塞渲染直到「所有可能影响首屏的 CSS」就绪（media 匹配的样式表），media=print 的 CSS 不阻塞渲染但仍会下载（低优先级）
- 解析失败容错：CSS 天然容错——非法声明整条丢弃、非法选择器整条规则丢弃（@media 内外都如此），这保证了新语法在老内核优雅降级
- @import 的串行坑：@import 在样式表内触发串行请求链（CSS→CSS），构建期应全部替换为 link 或打包合并
- 与 JS 的关系：script 执行前会等待前面的 CSS 完成（脚本可能查询样式），所以 CSS 阻塞的是「JS 执行 + 首次渲染」双重时机

```html
<!-- 关键 CSS 内联 + 非关键异步化 -->
<style>/* 首屏样式 */</style>
<link rel="stylesheet" href="non-critical.css" media="print" onload="this.media='all'">
<!-- 避免 -->
<style>@import url('a.css'); /* 串行链: 主css完成后才请求a.css */</style>
```
