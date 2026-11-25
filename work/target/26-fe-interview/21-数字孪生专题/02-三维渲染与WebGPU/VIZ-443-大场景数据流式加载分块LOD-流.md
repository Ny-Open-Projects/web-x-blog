---
title: [VIZ-443] 大场景数据流式加载（分块/LOD 流）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-443：大场景数据流式加载（分块/LOD 流）

**答**：
- 分块：场景切块（quadtree tile），按相机位置预加载半径 2 圈、卸载半径 4 圈外。
- 策略：加载优先级 = 屏幕投影面积 × 视线夹角权重；LOD 流（近处高模远处低模）。
- 防止卡顿：解码/上传在 idle 切片执行，纹理上传分帧（每帧预算 2MB）。

```javascript
// 流式加载调度
function streamScheduler(tiles, camPos, { loadR = 2, unloadR = 4, perFrameMB = 2 } = {}) {
  const want = tiles.filter(t => dist(t, camPos) < loadR)
    .sort((a, b) => priority(b) - priority(a));
  const drop = tiles.filter(t => dist(t, camPos) > unloadR && t.loaded);
  let budget = perFrameMB;
  const queue = [];
  for (const t of want) {
    if (t.loaded || budget - t.sizeMB < 0) continue;
    budget -= t.sizeMB; queue.push(t);
  }
  return { load: queue, unload: drop };
}
function priority(t) { return t.screenArea * t.angleWeight; }
function dist(t, p) { return Math.hypot(t.x - p[0], t.y - p[2]); }
```
