---
title: [CSS-280] print 样式 @media print 的工程要点
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 输出]
type: 面试题
---

## CSS-280：print 样式 @media print 的工程要点

**答**：
- 打印适配三件事：去交互（导航/按钮/广告 display:none）、改布局（grid/flex 改块级、深色背景转白、去掉 fixed）、补分页控制
- 分页控制：break-inside: avoid（卡片不拦腰断）、break-before: page（章节起新页）、orphans/widows（段落孤行）
- 隐性坑：fixed 定位打印时每页重复或丢失——打印态改为 static；超长表格分页丢表头——用 thead + `display: table-header-group`
- 链接可见性：打印后 URL 丢失，正文链接用 ::after 显示 href（可选）
- 调试技巧：DevTools 的 Rendering 面板模拟 print 媒体，不用真打印预览

```css
@media print {
  nav, aside, .no-print { display: none; }
  body { background: #fff; color: #000; }
  .card, tr { break-inside: avoid; }
  h2 { break-before: page; }
  a[href^='http']::after { content: ' (' attr(href) ')'; font-size: 10px; }
}
```
