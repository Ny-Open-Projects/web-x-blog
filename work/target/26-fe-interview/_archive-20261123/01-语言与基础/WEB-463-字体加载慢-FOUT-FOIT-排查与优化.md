---
title: [WEB-463] 字体加载慢（FOUT/FOIT）的排查与优化
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-463：字体加载慢（FOUT/FOIT）的排查与优化

**答**：
- 现象定义：FOUT=先显示后备字体再切换（闪动），FOIT=空白期等字体（白闪）；由 font-display 决定
- 排查顺序：字体文件多大（中文字体动辄数 MB 是主因）→ 是否阻塞（preload/提前 DNS）→ font-display 策略 → 是否每次都重新下载（缓存头）
- 中文字体治本方案：子集化（fontmin/pyftsubset 按用字裁剪）、按需分包（unicode-range 拆片）、动态子集服务（如 Google Fonts 中文模式）
- 策略建议：正文用 `swap`（体验优先），图标/品牌字用 `block` 短暂等待或直接给 fallback
- 监控：PerformanceObserver 监控 FontFaceSet load 事件，把字体加载耗时纳入性能看板

```css
@font-face {
  font-family: 'Brand';
  src: url('/fonts/brand-subset.woff2') format('woff2');
  font-display: swap;
  unicode-range: U+4E00-9FFF; /* 只在命中区间才下载 */
}
```
