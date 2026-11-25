---
title: [BAS-001] DOCTYPE 的作用是什么？standards 模式和 quirks 模式有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-001：DOCTYPE 的作用是什么？standards 模式和 quirks 模式有什么区别？
**答**：
- `<!DOCTYPE html>` 告诉浏览器用标准模式渲染；声明缺失或写错会退回 quirks 怪异模式。
- quirks 模式下：盒模型退化为 IE 模型（width 包含 padding 和 border）、行内元素宽高部分生效、图片底部出现空隙、部分百分比高度行为异常。
- 现代页面必须以 `<!DOCTYPE html>` 开头，它不需要区分 HTML4/5，写任何合法 DOCTYPE 都会进入标准模式。

```html
<!DOCTYPE html>
<!-- 标准模式：width:100px + padding:10px + border:1px = 实际占宽 122px -->
<html>
  <head><meta charset="utf-8"></head>
  <body>
    <!-- 若删掉上面的 DOCTYPE 进入 quirks 模式：
         同样的样式总宽变为 100px，内容区被挤压，布局整体与标准模式不一致 -->
    <div style="width:100px;padding:10px;border:1px solid #000;">122px or 100px</div>
  </body>
</html>
```
