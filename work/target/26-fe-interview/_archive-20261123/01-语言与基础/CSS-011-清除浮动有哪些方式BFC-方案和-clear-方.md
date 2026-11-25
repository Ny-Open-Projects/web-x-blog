---
title: [CSS-011] 清除浮动有哪些方式？BFC 方案和 clear 方案的区别？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-011：清除浮动有哪些方式？BFC 方案和 clear 方案的区别？

**答**：
- 方式一：伪元素 `::after { content: ""; display: block; clear: both; }`，最经典。
- 方式二：父元素建立 BFC（flow-root / overflow: hidden）。
- 方式三：在末尾添加空标签 `clear: both`，已过时，产生无意义 DOM。
- 区别：clear 让浮动元素之后的盒子“下移让开”，BFC 让容器真正“包住”浮动，可继续利用浮动特性排版。
- 现代布局优先用 flex/grid，浮动只在文字环绕等场景使用。

```css
/* 方案一：伪元素清除（clear 思路） */
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

/* 方案二：BFC 包含浮动 */
.bfc-clear {
  display: flow-root;
}

/* 演示结构 */
/* <div class="clearfix">
     <div style="float:left; width:100px; height:100px;">浮动块</div>
   </div>
   <p>后续内容</p> */
```
