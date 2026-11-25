---
title: [BAS-079] line-height 写 1.5、1.5em、150% 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-079：line-height 写 1.5、1.5em、150% 有什么区别？
**答**：
- 无单位 1.5：子元素继承的是"比例"，按子元素自己的 font-size 计算，推荐写法。
- 1.5em 或 150%：父元素先算成具体 px 再被继承，子元素 font-size 更大时行高不跟随，出现文字重叠。
- 结论：行高永远用无单位数字。

```css
.parent { font-size: 16px; line-height: 150%; }   /* 计算值 24px 被继承 */
.child  { font-size: 32px; line-height: inherit; }/* 行高仍 24px，文字重叠 */
/* 若父级写 line-height: 1.5，子级行高 = 32 * 1.5 = 48px，正常 */
```
