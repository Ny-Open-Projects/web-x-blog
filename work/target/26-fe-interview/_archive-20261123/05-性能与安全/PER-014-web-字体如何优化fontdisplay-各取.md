---
title: [PER-014] web 字体如何优化？font-display 各取值的行为是什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-014：web 字体如何优化？font-display 各取值的行为是什么？

**答**：
- 阻塞期：字体未加载时浏览器以"隐形文本"渲染（FOIT），最多等约 3s，造成白块。
- `font-display: swap`：阻塞期极短，立即用 fallback 字体渲染，字体就绪后替换（FOUT），推荐用于正文。
- `font-display: optional`：100ms 内没加载完就整段不换字体，下一轮导航才用，体验最稳。
- 配合手段：`<link rel="preload">` 字体文件且必带 `crossorigin`、woff2 压缩、`unicode-range` 按字符集分包、子集化中文字体。

```html
<!-- 提前预载首屏关键字体，crossorigin 必须带，否则会二次下载 -->
<link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
<style>
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter-var.woff2') format('woff2');
  /* swap：先用后备字体渲染，字体就绪后替换，避免长白屏 */
  font-display: swap;
  unicode-range: U+0000-00FF; /* 按需分包，只加载用到的字符集 */
}
body { font-family: Inter, system-ui, sans-serif; }
</style>
```
