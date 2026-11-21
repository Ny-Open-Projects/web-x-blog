---
title: [CSS-138] flex 多列等间距换行时最后一行不靠左怎么办？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-138：flex 多列等间距换行时最后一行不靠左怎么办？

**答**：
- 病灶：`flex-wrap` + `justify-content: space-between` 时，最后一行元素不足会两端撑开，间距错乱。
- 解法一（首选）：改 grid `repeat(auto-fill, minmax(220px, 1fr))`，空位由网格轨道天然占住，完全无 JS。
- 解法二：flex + `gap`，item 宽度用 `calc((100% - (n-1) × gap) / n)` 精确算出，最后一行自然靠左。
- 解法三（补位法）：往列表尾部塞 n 个 `visibility: hidden` 占位元素撑住 space-between，适合不便换 grid 的存量代码。

```css
/* 问题复现：最后一行只剩 2 个时被 space-between 推到两端 */
.bad {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
.bad .item { width: 220px; }

/* 解法一：grid auto-fill，空轨道自动占位（首选） */
.good-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 16px;
}

/* 解法二：flex + gap + calc 宽度，每行固定 4 个 */
.good-flex {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
.good-flex .item {
  /* (100% - 3 × 16px) / 4，gap 实际参与宽度分配 */
  flex: 0 1 calc((100% - 48px) / 4);
}
```

## 二十三、Flex 深水区
