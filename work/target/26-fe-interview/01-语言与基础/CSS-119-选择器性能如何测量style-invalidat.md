---
title: [CSS-119] 选择器性能如何测量？style invalidation 是什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-119：选择器性能如何测量？style invalidation 是什么？

**答**：
- 测量入口：DevTools Performance 录制中看 Recalculate Style 事件时长与影响元素数；Style 面板的 selector 统计可看各选择器匹配耗时。
- 匹配方向：选择器从右向左匹配，`.a .b .c .d` 最右的 `.d` 命中数决定扫描起点。
- 真正的现代瓶颈是"样式失效"（style invalidation）：DOM/类名一变，浏览器要算哪些节点受影响，宽泛选择器（`div *`、深层后代链）扩大失效范围。
- 收敛手段：缩短选择器深度、用 class 直击目标、把状态写在近邻（data 属性）而非祖先链。
- 没有证据不优化：先测量再动手，多数页面样式计算 <2ms，过早优化无意义。

```css
/* 1. 反例：深层后代链，失效范围大 */
/* .page .content .list .item .meta .time { color: var(--fg-secondary); } */

/* 2. 正解：单一类直击，失效范围最小 */
.meta-time { color: var(--fg-secondary); }

/* 3. 状态联动写在近邻，而非祖先扫描 */
.item[data-active] .meta-time { color: var(--brand); }

/* 4. 属性选择器窄域：限定在组件根内，避免全文档属性扫描 */
.card[data-collapsed] .card-body { display: none; }
```
