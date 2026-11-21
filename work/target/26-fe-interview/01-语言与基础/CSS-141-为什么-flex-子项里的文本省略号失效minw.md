---
title: [CSS-141] 为什么 flex 子项里的文本省略号失效？min-width: 0 是怎么救场的？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-141：为什么 flex 子项里的文本省略号失效？min-width: 0 是怎么救场的？

**答**：
- flex 子项默认 `min-width: auto`：不能收缩到内容最小尺寸以下，长文本把子项撑开，ellipsis 永远不触发。
- `min-width: 0` 显式把下限归零，子项才被允许压到内容以下，`overflow: hidden` 才能生效。
- 常见组合：文本项 `flex: 1; min-width: 0` + 按钮项 `flex-shrink: 0`，形成“文本可截断、按钮不变形”的标准工具栏。
- 纵向同理是 `min-height: 0`（滚动容器失效的元凶）。

```css
/* 问题结构：.card-row > .title（要省略号） + .btn（固定宽） */
.card-row {
  display: flex;
  gap: 12px;
  align-items: center;
}
.card-row .title {
  flex: 1;
  min-width: 0;          /* 关键一行：把 auto 下限改回 0 */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.card-row .btn {
  flex-shrink: 0;        /* 按钮永远完整 */
}
/* 没写 min-width: 0 时，.title 被"标题很长很长..."撑到内容宽，
   父容器溢出，ellipsis 不出现 */
```
