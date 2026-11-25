---
title: [CSS-276] caret-color 与输入体验
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 细节]
type: 面试题
---

## CSS-276：caret-color 与输入体验

**答**：
- caret-color：输入框光标（插入符）颜色——深色主题里黑色光标不可见的修复
- 相关细节：caret-color: transparent 隐藏光标（数字键盘场景防闪烁，但要给替代焦点指示）
- 配合主题：跟随 color-scheme 自动适配；品牌色光标与 accent-color 统一
- 与 selection 的组合：::selection + caret-color 一起构成输入控件的品牌化细节
- 冷知识：光标动画/宽度不可定制（caret-shape 提案未落地），只有颜色

```css
.dark-input {
  caret-color: #4fc3f7;      /* 暗底可见 */
  color: #eee;
}
.dark-input::selection { background: #1565c0; color: #fff; }
```
