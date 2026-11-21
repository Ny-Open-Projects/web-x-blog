---
title: [CSS-309] 笔试：CSS 实现瀑布流（columns 方案）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 布局]
type: 笔试题
---

## CSS-309：笔试：CSS 实现瀑布流

**题目**：纯 CSS 实现图片瀑布流（响应式列数：手机 2 列、平板 3 列、桌面 4 列），卡片高度不定且不被拆分；说明该方案的顺序局限与替代。

**答**：
```css
.gallery {
  columns: 4;           /* 列数基准 */
  column-gap: 16px;
}
@media (max-width: 1024px) { .gallery { columns: 3; } }
@media (max-width: 640px)  { .gallery { columns: 2; } }

.gallery .card {
  break-inside: avoid;          /* 卡片不被跨列拆分 */
  margin-bottom: 16px;
  display: inline-block;        /* 兼容老渲染模式 */
  width: 100%;
}
.gallery img { width: 100%; display: block; border-radius: 8px; }

/* 断点防抖：cols 随断点变化时内容会重排（列优先），需接受 */
```

**评分点**：
- columns + break-inside: avoid 的组合（核心）
- 响应式列数切换
- inline-block/width:100% 的兼容细节
- 关键认知：columns 是「列优先」填充，视觉顺序 ≠ DOM 顺序（搜索引擎/读屏顺序受影响）；行序敏感时改用 grid dense 或 JS
