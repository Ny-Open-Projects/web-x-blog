---
title: [CSS-023] flex-grow、flex-shrink、flex-basis 分别如何工作？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-023：flex-grow、flex-shrink、flex-basis 分别如何工作？

**答**：
- `flex-basis` 定义分配剩余空间前项目的主轴基准尺寸，auto 时取 width/height。
- `flex-grow` 按“份数”分配正剩余空间：各项目分得 剩余 × 自身份数 / 总份数。
- `flex-shrink` 在空间不足时按“份数 × 基准尺寸”加权收缩，默认 1，0 表示不收缩。
- 面试常考计算题：总份数、加权收缩的权重是 grow×basis 而不是单纯份数。

```css
/* grow 示例：容器 600px，两项 basis 各 200px，剩余 200px */
.bar { display: flex; }
.bar .a { flex: 2 0 200px; } /* 分 2/3 → 多拿 133.3，最终 333.3 */
.bar .b { flex: 1 0 200px; } /* 分 1/3 → 多拿 66.7，最终 266.7 */

/* shrink 示例：容器 400px，两项 basis 各 300px，超 200px */
.shrink-bar { display: flex; width: 400px; }
.shrink-bar .x { flex: 1 1 300px; } /* 权重 300 */
.shrink-bar .y { flex: 1 2 300px; } /* 权重 600 */
/* x 收缩 200 × 300/900 ≈ 66.7 → 233.3；y 收缩 133.3 → 166.7 */
```
