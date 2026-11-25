---
title: [OPT-072] 字体加载的 CLS 怎么用 size-adjust / ascent-override 消除？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-072：字体加载的 CLS 怎么用 size-adjust / ascent-override 消除？

**答**：
- FOUT/FOIT 之外还有 FOIT-C（Fallback 字体与 Web 字体**度量不同**，加载完成后文字重排），是 CLS 的隐蔽来源。
- `@font-face` 的 `size-adjust`、`ascent-override`、`descent-override`、`line-gap-override` 把 fallback 字体的度量**调到与 Web 字体一致**，交换时文字位置不动。
- 配方：选一个系统近似字体作 fallback → 用工具（如 Fontaine/fontaine 或手动对照表）算出 override 值 → 只配 CSS，不改字体文件。
- 配合 `font-display: swap` 与预加载，先把 fallback 稳住，Web 字体加载中不再抖。

```css
/* 一一对应：fallback 度量对齐消除字体交换 CLS */
/* 原字体声明 */
@font-face {
  font-family: 'Harmony';
  src: url('/fonts/harmony.woff2') format('woff2');
  font-display: swap;
  unicode-range: U+4E00-9FFF; /* 按需声明，减少下载量 */
}

/* 关键：给 fallback 字体建一个"影子"声明，度量覆盖成与 Harmony 一致
   数值来源：fontaine 自动计算，或 FontForge 里对比两个字体的
   unitsPerEm / ascent / descent 换算 */
@font-face {
  font-family: 'Harmony Fallback';
  src: local('PingFang SC');      /* 系统近似字体 */
  size-adjust: 105%;              /* 基准的 x-height 缩放，使宽度对齐 */
  ascent-override: 90%;           /* 上伸部对齐，行首行高不变 */
  descent-override: 22%;          /* 下伸部对齐 */
  line-gap-override: 0%;
}

/* 使用：fallback 写在第一位，Web 字体就绪后无缝替换 */
.text {
  font-family: 'Harmony', 'Harmony Fallback', sans-serif;
}

/* 验证：DevTools Performance 录制加载过程，看 Layout 块是否消失；
   或 CLS 上报对比接入前后的 P75 */
```
