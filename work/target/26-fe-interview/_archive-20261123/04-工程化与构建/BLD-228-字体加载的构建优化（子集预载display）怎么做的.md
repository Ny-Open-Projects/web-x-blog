---
title: [BLD-228] 字体加载的构建优化怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-228：字体构建优化怎么做？
**答**：
- 子集化：按实际字符集切分（unicode-range 分片，SCN-ENG-310 校验覆盖）——中文字体从 MB 级到 KB 级。
- 格式与降级：woff2 为主 + 系统字体降级栈；font-display（swap 闪动 vs block 隐藏——按场景选）。
- 加载编排：字体 preload（crossorigin！SCN-ENG-241）+ size-adjust（降级字体度量对齐，减少 CLS）。
- 构建产物：字体文件的 hash 命名 + 与 CSS 的引用对齐（CSS 引用字体 hash 变化联动）。
- 追问钩子：为什么 size-adjust 是解决 FOUT 的关键补充——font-display: swap 会先用降级字体渲染再切换（宽度不同导致布局跳动 CLS）；size-adjust/ascent-override 把降级字体的度量调整为与 webfont 一致——切换时布局不跳，这是子集化和 preload 之外最被忽视的一环。

```css
@font-face {
  font-family: 'Fallback';
  src: local('PingFang SC');
  size-adjust: 105%;                                  /* 度量对齐 webfont */
  ascent-override: 90%;
}
@font-face { font-family: 'Noto'; src: url(noto-4e00.woff2) format('woff2');
  unicode-range: U+4E00-9FFF; font-display: swap; }
/* preload with crossorigin (SCN-ENG-241) */
/* <link rel="preload" as="font" href="noto-4e00.woff2" crossorigin> */
```
