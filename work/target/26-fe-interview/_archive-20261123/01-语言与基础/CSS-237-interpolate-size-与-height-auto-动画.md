---
title: [CSS-237] interpolate-size 与 height auto 动画
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-237：interpolate-size 与 height: auto 动画

**答**：
- 历史痛点：height: auto ↔ 具体值不能过渡（auto 无法插值），手风琴都要 JS 量高度或 max-height hack
- interpolate-size: allow-keywords：让 auto/fit-content 等关键字参与插值——过渡时浏览器自动计算目标高度
- 配合 grid 0fr/1fr 方案：不声明 interpolate-size 时，`grid-template-rows: 0fr → 1fr` 是兼容性最好的 auto 高度动画（已有广泛支持）
- 优先级：新代码可直接 interpolate-size（Chromium 129+）；兼容场景用 0fr/1fr
- 面试话术：说出三个方案（max-height hack → 0fr/1fr → interpolate-size）体现演进认知

```css
/* 方案 A：现代 */
html { interpolate-size: allow-keywords; }
.details { height: 0; transition: height .3s; }
.details.open { height: auto; } /* 可动画了 */

/* 方案 B：兼容网格方案 */
.acc-body { display: grid; grid-template-rows: 0fr; transition: grid-template-rows .3s; }
.acc-body.open { grid-template-rows: 1fr; }
.acc-body > div { overflow: hidden; }
```
