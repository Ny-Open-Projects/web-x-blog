---
title: [CSS-235] text-wrap: balance 与 pretty 排版新特性
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 排版]
type: 面试题
---

## CSS-235：text-wrap: balance 与 pretty：排版新特性

**答**：
- balance：让多行文字行宽均衡——标题两行不再「第一行撑满、第二行孤字」；仅对 ≤6 行（Chromium）生效，标题专用
- pretty：优化段落末行，避免孤字（最后一行只有一两个字）；给正文段落用
- wrap 默认值 vs nowrap 之外的新中间态：stable（编辑器防抖动）
- 组合惯例：`h1 { text-wrap: balance }` + `p { text-wrap: pretty }` 全站一行配置
- 兼容：balance 全主流；pretty Chromium 117+——装饰性增强，降级无副作用

```css
h1, h2 { text-wrap: balance; }
article p { text-wrap: pretty; }
```
