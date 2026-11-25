---
title: [VIZ-224] 3D LOD 系统：距离分级与切换平滑
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-224：3D LOD 系统：距离分级与切换平滑

**答**：
- LOD 三档：远（简化网格/聚合）、中（中等面数）、近（全细节）；切换阈值带滞后（hysteresis）防抖。
- 平滑切换：morph（两档网格顶点插值）或透明度交叉淡入——简单场景用滞后即可。
- 数据层 LOD：点云聚合（每档抽稀比 1/1, 1/4, 1/16）与几何 LOD 同理。

```javascript
class LODGroup {
  constructor(levels) { this.levels = levels.sort((a, b) => b.distance - a.distance);
    this.current = -1; }                                   // 按距离降序
  update(cameraPos, objPos) {
    const dist = distance(cameraPos, objPos);
    let target = this.levels.findIndex(l => dist <= l.distance);
    if (target < 0) target = this.levels.length - 1;
    // 滞后：距离阈值 ±10% 内不切换
    if (this.current >= 0) {
      const curTh = this.levels[this.current].distance;
      if (Math.abs(dist - curTh) / curTh < 0.1) return this.current;   // 滞后带内不动
    }
    if (target !== this.current) {
      this.levels.forEach((l, i) => l.object.visible = i === target);
      this.current = target;
    }
    return this.current;
  }
}
```
