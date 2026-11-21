---
title: [H5-003] DOCTYPE 的作用是什么？声明缺失会发生什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-003：DOCTYPE 的作用是什么？声明缺失会发生什么？
**答**：
- 声明文档类型，让浏览器以标准模式渲染；HTML5 以后简化为 `<!DOCTYPE html>`，不区分版本。
- 缺失或写错时进入怪异模式（quirks mode）：盒模型按 IE 旧模型计算（width 包含 padding/border）、行内元素高度处理不同、表格字体继承异常。
- 怪异模式的差异会导致同一份 CSS 表现不一致，必须避免；`document.compatMode` 可检测（`CSS1Compat` 标准模式）。
- `<!DOCTYPE html>` 必须位于文档最前面，前面的内容越少越好（前置注释/空白在旧 IE 会触发怪异模式）。

```html
<!DOCTYPE html>
<!-- 第一行必须是 DOCTYPE，触发标准模式 -->
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>标准模式</title>
  </head>
  <body></body>
</html>
```

```javascript
// 检测当前文档的渲染模式
console.log(document.compatMode);
// "CSS1Compat"  标准模式（有 DOCTYPE）
// "BackCompat"  怪异模式（缺 DOCTYPE），width 计算回退到 IE 盒模型
```
