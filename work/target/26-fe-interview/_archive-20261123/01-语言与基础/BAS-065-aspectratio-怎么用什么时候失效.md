---
title: [BAS-065] aspect-ratio 怎么用？什么时候失效？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-065：aspect-ratio 怎么用？什么时候失效？
**答**：
- `aspect-ratio: 16 / 9` 让元素按宽高比自动计算另一边，替代 padding-top 百分比占位的 hack。
- 宽高都被显式指定（非 auto）时比例被忽略；内容撑高也会破坏比例，必要时配合 overflow 或 min-height: 0 约束。
- 常用于视频容器、封面图占位、卡片缩略图。

```css
.video-box {
  width: 100%;
  aspect-ratio: 16 / 9;   /* 高度自动算出 */
}
.avatar {
  width: 48px;
  height: 48px;           /* 宽高都写死，aspect-ratio 失效 */
  aspect-ratio: 1;
}
```
