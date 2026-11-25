---
title: [CSS-097] word-break、overflow-wrap、white-space 三件套的适用矩阵是什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-097：word-break、overflow-wrap、white-space 三件套的适用矩阵是什么？

**答**：
- `white-space` 控制"是否换行与折叠空白"：nowrap 不换行、pre 保留原样、pre-wrap 保留且换行。
- `word-break: break-all` 任意字符处断（CJK/长数字串），`keep-all` 禁止 CJK 内断。
- `overflow-wrap: break-word` 仅在单词放不下时才断；`anywhere` 额外把断点计入 min-content，容器可收缩更彻底。
- 场景矩阵：长 URL 用 overflow-wrap anywhere；中英混排默认即可；代码块 pre-wrap；数字串防溢出 break-all。
- 三者可叠加使用，先由 white-space 决定换不换，再由 word-break/overflow-wrap 决定在哪断。

```css
/* 长英文单词/URL：放不下才断，且参与最小宽度计算 */
.long-url { overflow-wrap: anywhere; }

/* 长数字串/验证码：任意位置断开防溢出 */
.otp-code { word-break: break-all; }

/* 代码块：保留空格与换行，超长仍可断 */
pre.code {
  white-space: pre-wrap;
  overflow-wrap: break-word;
}

/* 单行展示 + 悬停看全文 */
.tag { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* CJK 标点禁则 + 不在单词内断 */
.article { word-break: normal; overflow-wrap: break-word; line-break: strict; }
```
