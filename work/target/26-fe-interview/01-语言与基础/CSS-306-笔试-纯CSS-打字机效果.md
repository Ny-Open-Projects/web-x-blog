---
title: [CSS-306] 笔试：纯 CSS 打字机效果
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-306：笔试：纯 CSS 打字机效果

**题目**：实现打字机逐字显现：文字逐个出现（带光标闪烁），打完停顿后循环重来。要求纯 CSS，并说明「为什么必须等宽字体或定宽方案」。

**答**：
```css
.typewriter {
  font-family: monospace;               /* 等宽：每字符宽度一致，宽度才能对应字数 */
  overflow: hidden;
  white-space: nowrap;
  border-right: 2px solid #333;         /* 光标 */
  width: 0;
  animation:
    typing 2s steps(12) 1s infinite alternate,
    blink .8s step-end infinite;
}
@keyframes typing {
  from { width: 0; }
  to { width: 12ch; }                   /* ch 单位 = 一个「0」的宽度 */
}
@keyframes blink { 50% { border-color: transparent; } }
```
```html
<p class="typewriter">Hello World!</p>
```
```css
/* 非等宽文字的替代方案：clip-path 按步进揭示 */
.typewriter-2 {
  animation: reveal 2s steps(30) infinite alternate;
  clip-path: inset(0 100% 0 0);
}
@keyframes reveal { to { clip-path: inset(0 0 0 0); } }
/* clip 方案不需要等宽，但「逐字」感稍弱（按步进揭示而非字符边界） */
```

**评分点**：
- steps() 逐帧跳跃（不是平滑过渡）——打字机的核心
- ch 单位 + 等宽字体 = 宽度与字数对应；能解释为什么
- 光标 blink 用 step-end（硬切）而非平滑
- 非等宽场景的 clip-path 替代认知
