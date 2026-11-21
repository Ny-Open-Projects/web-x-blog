---
title: [BAS-176] 字体加载的 FOIT 和 FOUT 是什么？font-display 怎么选？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-176：字体加载的 FOIT 和 FOUT 是什么？font-display 怎么选？
**答**：
- FOIT：字体加载期间文字隐形（不渲染），用户看到空白闪一下；FOUT：先用后备字体渲染，字体到了再切换，产生布局跳动。
- font-display：block（短 FOIT）、swap（直接 FOUT，最常用）、fallback（100ms 隐形 + 短暂后备窗口）、optional（超时不加载，交给浏览器决定）。
- 正文文字一般选 swap 保证可见性；装饰性字体可接受 optional 避免闪动。

```css
@font-face {
  font-family: Brand;
  src: url('/brand.woff2') format('woff2');
  font-display: swap;   /* 先用后备字体渲染 FOUT，字体到了再换 */
}
h1 { font-family: Brand, system-ui, sans-serif; }
/* block 短暂隐形 FOIT；optional 超时直接放弃，交给浏览器 */
```
