---
title: [CSS-236] field-sizing: content：输入框自适应内容
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 组件]
type: 面试题
---

## CSS-236：field-sizing: content：输入框自适应内容

**答**：
- textarea/输入框自适应内容高度——以前要 JS 监听 input 重设 height，现在一行 CSS
- 语法：`textarea { field-sizing: content; }`；配合 `min-height/max-height` 约束范围
- 典型场景：评论框随内容长高、标签输入的自适应宽度、搜索框随内容伸缩
- 细节：初始为空时按 placeholder 宽度；rows 属性在 content 模式下不再生效
- 兼容：Chromium 123+；Safari/Firefox 未支持——生产保留 JS 方案或接受固定高度降级

```css
.comment-box {
  field-sizing: content;
  min-height: 44px;
  max-height: 300px;   /* 超过滚动 */
  width: 100%;
}
```
