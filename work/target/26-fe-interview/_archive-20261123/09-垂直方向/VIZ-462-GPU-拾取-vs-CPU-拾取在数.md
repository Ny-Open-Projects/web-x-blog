---
title: [VIZ-462] GPU 拾取 vs CPU 拾取在数据可视化大屏的选型
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-462：GPU 拾取 vs CPU 拾取在数据可视化大屏的选型

**答**：
- 大屏场景：上万个图形元素，鼠标 hover 高频——CPU 每次射线全场景太贵。
- GPU 方案：ID pass 按需渲染（鼠标事件触发一次小 pass），读取 1px 异步。
- 混合：静态层 CPU 空间索引（网格预建），动态层 GPU ID。

```javascript
// 大屏拾取决策
function pickStrategy(itemCount, hoverHz) {
  if (itemCount < 2000) return { mode: 'cpu-index',
    note: '网格索引查询 <0.1ms' };
  if (hoverHz > 60) return { mode: 'gpu-id-async',
    note: '按需 ID pass + 异步读回' };
  return { mode: 'cpu-bvh', note: 'BVH 加速射线' };
}
```
