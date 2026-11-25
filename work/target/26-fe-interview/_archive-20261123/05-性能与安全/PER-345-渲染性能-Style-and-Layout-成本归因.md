---
title: [PER-345] 渲染性能：Style/Layout/Paint/Composite 四阶段成本如何归因与优化？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-345：渲染性能：Style/Layout/Paint/Composite 四阶段成本如何归因与优化？

**答**：
- 四阶段流水线：Style（样式计算：选择器匹配 + 计算样式）→ Layout（布局：几何计算，改宽高/位置触发）→ Paint（绘制：填充像素，改颜色/阴影触发）→ Composite（合成：图层拼合，transform/opacity 触发，GPU）。改动的属性决定走多深：layout < paint < composite 依次便宜。
- 归因工具：Performance 面板 Main 轨道看紫色 Recalculate Style / Layout 块（其右上角的三角提示"Layout invalidated"）；3D 视图与 Layers 面板看合成层划分；Rendering 面板的 Paint Flashing（重绘区域高亮）与 Layout Shift Regions。
- 优化手段按阶段：Style——选择器扁平（避免深层后代选择器）、减少样式失效面（改 class 而不是 style 对象大面积写）；Layout——避免强制同步布局（读写交错）、用 transform 替代 top/left 动画、content-visibility 跳过屏外布局；Paint——减少大面积重绘（will-change 提升层、阴影用 filter）、缩小重绘区域；Composite——控制层数量（层爆炸内存与上传成本）。
- 系统性检查：Recalculate Style 的 Elements Affected 数量异常大 → 样式失效面过大；连续 Layout 块交替出现 → 强制同步布局。

```javascript
// 强制同步布局反例与修复
// 反例：读写交错，每轮 layout 后又读
for (const el of items) {
  const h = el.offsetHeight;            // 读（触发 layout）
  el.style.height = h + 1 + 'px';       // 写（使 layout 失效）→ 下一轮读再触发
}
// 修复：读写分离——先批量读，再批量写
const heights = items.map((el) => el.offsetHeight);   // 一轮 layout
items.forEach((el, i) => { el.style.height = heights[i] + 1 + 'px'; });  // 一次写
// 动画改 transform：.card:hover { transform: translateY(-2px); } —— 只走 Composite
```
