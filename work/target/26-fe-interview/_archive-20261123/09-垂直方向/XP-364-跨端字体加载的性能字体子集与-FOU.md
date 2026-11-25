---
title: [XP-364] 跨端字体加载的性能（字体子集与 FOUT）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-364：跨端字体加载的性能（字体子集与 FOUT）

**答**：
- 子集：中文按使用字符子集化（unicode-range 分片），全量中文字体 3MB -> 分片 100KB 级。
- 加载：font-display swap + 尺度覆盖（PER-972 思路跨端）。
- 跨端：RN/Flutter 字体打包进 bundle（体积预算内）。

```javascript
// 字体分片
function fontChunks(usedChars) {
  const ranges = groupUnicodeRanges(usedChars);      // 聚合连续区间
  return ranges.map(r => ({
    range: r,
    css: `@font-face { src: url(font-${r.start}.woff2);
      unicode-range: U+${r.start.toString(16)}-${r.end.toString(16)}; }`,
  }));
}
// 只加载页面实际用到的分片（浏览器按 unicode-range 匹配）
```
