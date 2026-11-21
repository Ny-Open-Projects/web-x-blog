---
title: [CSS-026] flex 子项内容过长把容器撑爆怎么办？min-width: 0 的作用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-026：flex 子项内容过长把容器撑爆怎么办？min-width: 0 的作用？

**答**：
- flex 子项默认 `min-width: auto`，即不允许收缩到内容最小宽度以下，长文本/长表格会撑破容器。
- 解决：给需要收缩的子项设置 `min-width: 0`（垂直方向对应 `min-height: 0`）。
- 文本溢出配合 `overflow: hidden` + `text-overflow: ellipsis` 才能生效。
- 这是“flex + ellipsis 不生效”类 bug 的标准答案。

```css
/* HTML: <div class="chat"><div class="side">侧栏</div><div class="msg">超长的消息文本超长的消息文本…</div></div> */
.chat {
  display: flex;
  width: 100%;
}
.chat .side { flex: none; width: 120px; }
.chat .msg {
  flex: 1;
  min-width: 0;              /* 关键：允许收缩到内容以下 */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;   /* 没有 min-width:0 时这行不生效 */
}
```
