---
title: [PER-217] 字体加载的 FOUT/FOIT 如何影响 CLS 与 LCP？size-adjust 度量对齐怎么用？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-217：字体加载的 FOUT/FOIT 如何影响 CLS 与 LCP？size-adjust 度量对齐怎么用？

**答**：
- FOIT（不可见闪烁）：`font-display: block` 下文本先隐形等字体（最多 3s），文本不可见拖累 LCP（文本也可能是 LCP 元素）；FOUT（无样式闪烁）：`swap` 下先用 fallback 字体渲染，字体到达后替换——替换瞬间文本重排，若 fallback 与目标字体度量差异大，直接产生 CLS。
- 度量对齐（font-metrics-overrides）：给 fallback 字体声明 `size-adjust`（缩放 x 高度匹配主字体）、`ascent-override/descent-override/line-gap-override`，让两个字体占位几乎一致，替换时基本不位移。可用工具（如 fontaine）自动计算。
- 加载策略：主字体 preload + `font-display: swap`（或 `optional` 对非关键字体）；用 `document.fonts.load('1em MyFont')` 在合适时机预热；子集化（unicode-range 按需分包）把中文字体从几 MB 压到几十 KB。
- 验证：DevTools Rendering 的 Layout Shift Regions + Network 字体时序，确认替换瞬间无位移。

```css
/* 度量对齐：让 Arial 占位匹配 PingFangSC 的度量，替换时几乎不跳动 */
@font-face {
  font-family: 'Arial-Adjusted';
  src: local(Arial);
  size-adjust: 105%;            /* 自动工具算出的比例 */
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}
body { font-family: 'PingFangSC', 'Arial-Adjusted', sans-serif; font-display: swap; }
```
