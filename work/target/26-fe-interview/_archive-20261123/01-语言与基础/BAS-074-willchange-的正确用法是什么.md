---
title: [BAS-074] will-change 的正确用法是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-074：will-change 的正确用法是什么？
**答**：
- 提前告知浏览器某属性将要变化，让它预先做合成层等优化；只对 transform/opacity 等合成属性有明显收益。
- 应在动画前加上、结束后移除（如 hover 父级预告、JS onstart/onend 控制），常驻大量 will-change 反而耗内存、造成层爆炸。
- 不能当性能万能药：先测量再优化，多数场景 transition 本身已够。

```css
.card { transition: transform 0.3s; }
.card-parent:hover .card {
  will-change: transform;   /* 动画触发前预告 */
}
.card-parent:not(:hover) .card {
  will-change: auto;        /* 结束后释放 */
}
```
