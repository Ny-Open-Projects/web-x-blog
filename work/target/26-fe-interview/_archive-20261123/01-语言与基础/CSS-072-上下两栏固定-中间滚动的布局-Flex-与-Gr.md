---
title: [CSS-072] 上下两栏固定、中间滚动的布局，Flex 与 Grid 怎么写？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-072：上下两栏固定、中间滚动的布局，Flex 与 Grid 怎么写？

**答**：
- Flex：容器 `height: 100dvh` 纵向排列，header/footer `flex: none`，main `flex: 1; overflow: auto`。
- Grid：`grid-template-rows: auto 1fr auto`，main 自身滚动。
- 嵌套场景的坑：main 里再套 flex 纵向布局时，子项要 `min-height: 0` 才能正确收缩出滚动条。
- 页面级禁滚 `overflow: hidden`，把滚动收敛到 main，避免双层滚动条。

```css
/* 方案一：Flex */
.page-flex {
  display: flex; flex-direction: column;
  height: 100dvh;
  overflow: hidden;      /* 滚动只发生在 main */
}
.page-flex > header, .page-flex > footer { flex: none; }
.page-flex > main { flex: 1; overflow-y: auto; }

/* 方案二：Grid */
.page-grid {
  display: grid;
  grid-template-rows: auto 1fr auto;
  height: 100dvh;
  overflow: hidden;
}
.page-grid > main { overflow-y: auto; }

/* 嵌套时防收缩失效：中间层的纵向 flex 子项必须 min-height: 0 */
.page-grid > main > .inner { display: flex; flex-direction: column; min-height: 0; }
```
