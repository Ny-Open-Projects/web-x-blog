---
title: [RBL-303] 构建期的字体加载优化（子集化与 preload）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-303：构建期的字体加载优化（子集化与 preload）

**答**:
- 子集化：中文字体几 MB → 按实际字符集子集化（fonttools/pyftsubset）到几十 KB；动态内容（用户生成）用分片子集（unicode-range 分包按需）
- 构建期注入：`<link rel="preload" as="font" crossorigin>`（关键字体）、font-display: swap（防 FOIT 白块）
- 字体格式：woff2 为主（压缩率最高），老浏览器回退 woff——构建产物只输出 woff2（目标浏览器声明决定）
- 验证：CLS/FOIT 检测（Lighthouse 字体审计），preload 字体数 ≤3（过多挤占带宽）

```javascript
// asset 配置
{ test: /\.woff2$/, type: 'asset/resource', generator: { filename: 'fonts/[name].[contenthash:8][ext]' } }
// css
@font-face { font-display: swap; src: url(...) format('woff2'); }
```
