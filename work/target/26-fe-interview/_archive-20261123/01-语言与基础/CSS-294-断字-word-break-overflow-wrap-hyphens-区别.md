---
title: [CSS-294] 断字：word-break / overflow-wrap / hyphens 的区别
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 排版]
type: 面试题
---

## CSS-294：断字：word-break / overflow-wrap / hyphens

**答**：
- overflow-wrap: break-word：**单词放不下时**才整体换行或断词——首选，语义最正确（尽量保词完整）
- word-break: break-all：任意字符处断（CJK 习惯影响英文场景）——长 URL/密钥串场景；keep-all：CJK 不内断
- hyphens: auto：连字符断词（需 lang 属性与字典支持）——排版最优但依赖多
- CJK 与西文混排默认行为：CJK 逐字可断、西文按词——多数「溢出」问题其实是 long string（URL/ID），用 overflow-wrap 解决
- 组合配方：正文 `overflow-wrap: anywhere`（最小宽度计算也考虑断点）+ 长串专用 break-all

```css
p { overflow-wrap: break-word; }        /* 通用正文 */
.code-snippet { word-break: break-all; overflow-wrap: anywhere; } /* 长串 */
article[lang='en'] p { hyphens: auto; } /* 英文连字排版 */
```
