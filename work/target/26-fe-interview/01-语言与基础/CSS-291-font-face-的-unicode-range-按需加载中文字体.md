---
title: [CSS-291] @font-face 的 unicode-range：按需加载中文字体
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 排版]
type: 面试题
---

## CSS-291：@font-face 的 unicode-range：按需加载中文字体

**答**：
- unicode-range：声明「该字体文件覆盖哪些码位」——页面用到对应字符才下载该文件
- 中文方案：全量字体拆成 100+ 分片（Google Fonts 中文模式），每个分片数千字，按需命中——中文字体从 5MB 降到实际使用几百分 KB
- 生成工具：fontmin、cn-font-split 按字频/范围切包
- 配合 font-display: swap：分片加载期间显示回退字体，几乎无感
- 面试话术：说出「拆包 + unicode-range + 按需命中」三件套与「为什么全量中文字体不可接受」

```css
/* cn-font-split 生成的典型产物（示意） */
@font-face {
  font-family: 'CNFont';
  src: url('/fonts/cn-0.woff2') format('woff2');
  font-display: swap;
  unicode-range: U+4E00-4E7F; /* 一小段区间的字 */
}
/* 再定义数十上百个分片，浏览器按页面实际字符命中下载 */
```
