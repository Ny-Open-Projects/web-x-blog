---
title: [BAS-076] user-select 和 caret-color 有什么用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-076：user-select 和 caret-color 有什么用？
**答**：
- user-select 控制文本可选中性：none 防误选（按钮、仿 App 界面），all 点击整段选中，text 恢复可选。
- caret-color 自定义输入光标颜色，none 隐藏光标，可与主题色统一。
- 体验细节考点：user-select: none 只是不可选，内容仍在 DOM 里，不是"禁复制"的安全手段。

```css
.btn, .tab { user-select: none; }       /* 控件文字不可拖选 */
.snippet { user-select: all; }          /* 点一下整段选中，方便复制 */
.dark-input { caret-color: #38bdf8; }   /* 光标与主题同色 */
```
