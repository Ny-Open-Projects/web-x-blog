---
title: [BAS-072] background 简写有什么陷阱？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-072：background 简写有什么陷阱？
**答**：
- 简写 `background: url(a.png) center / cover no-repeat` 会把未写出的子属性全部重置为默认值，之前单独设置的 background-color 会被悄悄清掉。
- 简写里 position 和 size 共用一段：size 必须写在 position 之后用 `/` 分隔，只写 size 不写 position 非法。
- 多背景用逗号分层，背景色只能写在最后一层。

```css
.box {
  background-color: #333;                          /* 会被下面的简写重置为 transparent */
  background: url(a.png) center / cover no-repeat;
}
/* 正确做法：颜色写进简写最后一层 */
.box2 { background: url(a.png) center / cover no-repeat, #333; }
```
