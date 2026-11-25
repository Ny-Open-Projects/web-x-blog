---
title: [H5-009] 浏览器解析 HTML 遇到非法嵌套会怎样？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-009：浏览器解析 HTML 遇到非法嵌套会怎样？
**答**：
- HTML 解析器容错性极强：未闭合标签、错位标签会被自动纠正，不会像 XML 那样报错中断。
- 典型纠错规则：`<p>` 中不能再嵌套块级元素，浏览器会把后续的 div 提到 p 外面（闭合 p）。
- 自动纠错会产生意料之外的 DOM 结构，导致 CSS 选择器失效；用 `document.body.innerHTML` 打印或 DevTools Elements 面板可看到纠正后的真实结构。
- table 内直接写文本、ul 内写 div 等都是常见翻车点。

```html
<!-- 书写的源码 -->
<p>
  第一段
  <div>段落里的块级内容</div>
</p>
```

```javascript
// 浏览器实际解析出的 DOM（自动纠错）：
// <p>第一段</p>
// <div>段落里的块级内容</div>
// <p></p>
console.log(document.body.querySelector('p').nextElementSibling.tagName); // DIV

// p 被提前闭合，选择器 p div 永远匹配不到
console.log(document.querySelectorAll('p div').length); // 0
```

## 二、表单增强与校验
