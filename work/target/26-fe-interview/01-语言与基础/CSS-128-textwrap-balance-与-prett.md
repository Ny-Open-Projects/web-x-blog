---
title: [CSS-128] text-wrap balance 与 pretty 解决什么问题？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-128：text-wrap balance 与 pretty 解决什么问题？

**答**：
- `text-wrap: balance`：让多行文本各行长度的差距最小化，标题不再"头重脚轻"（第一行爆满、第二行孤字）。
- `text-wrap: pretty`：避免段落末行出现过短孤行，优化段落排版节奏。
- balance 建议只用于 ≤6 行的标题/按钮文案，行数多时有计算成本；正文段落用 pretty。
- 两者都是渐进增强：不支持时回退默认换行，页面完全正常。
- 配合 `text-box-trim`（块首尾裁空）可进一步精修排版。

```css
/* 标题平衡换行 */
h1, h2, .hero-copy {
  text-wrap: balance;
}

/* 正文防孤行 */
.article p {
  text-wrap: pretty;
  max-width: 65ch;   /* 每行 60~75 字符的最佳阅读宽度 */
}

/* 按钮/标签文案：不支持时无副作用 */
.btn { text-wrap: balance; }
```
