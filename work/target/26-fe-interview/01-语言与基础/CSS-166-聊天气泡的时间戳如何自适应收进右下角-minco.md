---
title: [CSS-166] 聊天气泡的时间戳如何自适应收进右下角（min-content 技巧）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-166：聊天气泡的时间戳如何自适应收进右下角（min-content 技巧）？

**答**：
- 目标：短消息时时间戳贴在文本右侧同一行，长消息换行后收进气泡右下角。
- 经典手法：文本末尾放一个与时间戳同宽的隐形浮动占位（`float: right; height: 0`），最后一行文字自动绕开右下角，时间戳 absolute 定位到该空位。
- `visibility: hidden` 占位必须用与时间戳相同的字号内容，宽度才一致。
- 本质是利用 float 的避让规则给 absolute 元素腾位置，比 JS 测量行数稳定得多。

```css
/* 结构：.msg > .text + .time */
.msg {
  position: relative;
  width: fit-content;
  max-width: 72%;
  padding: 8px 12px;
  border-radius: 12px;
  background: #f2f3f5;
  overflow-wrap: anywhere;
}
/* 隐形占位：内容与时间戳完全一致，宽度即时间戳宽度 */
.msg .text::after {
  content: "08:30";
  visibility: hidden;
  float: right;              /* 最后一行文字自动绕开右下角 */
  height: 0;
  margin-left: 8px;
  font-size: 12px;
}
.msg .time {
  position: absolute;        /* 落在占位腾出的空位上 */
  right: 12px;
  bottom: 6px;
  font-size: 12px;
  color: #999;
  white-space: nowrap;
}
```

## 二十七、主题与设计系统落地
