---
title: [SCN-152] 外卖骑手 App 需要地理围栏：进入/离开指定区域要触发提醒，如何实现？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-152：外卖骑手 App 需要地理围栏：进入/离开指定区域要触发提醒，如何实现？
**答**：
- 围栏判断是几何问题：圆形围栏算距离，多边形围栏用射线法（ray casting）判断点在内。前端只做即时提醒，围栏进出的事实上报由后端复核（防止端上丢点误判）。
- GPS 是 1s 级采样，骑手快速穿越小围栏可能两个采样点都在外——对高速移动目标要做轨迹线段与围栏相交检测，而不是只看点。
- 进入/离开要防抖：在边界附近漂移会反复触发，用"连续 N 次在内才报进入、连续 N 次在外才报离开"消抖。
- App 内置围栏列表随区域下发，判断在 Worker 或本地做，避免每秒一次主线程重算。

```javascript
// 地理围栏：射线法 + 线段穿越检测 + 进出消抖
export function pointInPolygon(pt, poly) {
  let inside = false;
  for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
    const [xi, yi] = poly[i], [xj, yj] = poly[j];
    const intersect = (yi > pt.lat) !== (yj > pt.lat) &&
      pt.lng < ((xj - xi) * (pt.lat - yi)) / (yj - yi) + xi;
    if (intersect) inside = !inside;                   // 射线法：穿越边次数奇偶
  }
  return inside;
}

export class GeoFenceMonitor {
  insideCount = 0; outsideCount = 0; isInside = false;
  constructor(fences, { onChange, debounce = 3 }) { this.fences = fences; this.onChange = onChange; this.debounce = debounce; }

  onLocation(loc, prevLoc) {
    const hit = this.fences.some(f => pointInPolygon(loc, f.polygon));
    // 轨迹线段穿越检测：两采样点在外但线段穿过围栏 = 短暂进入
    const crossed = !hit && prevLoc &&
      this.fences.some(f => segmentIntersectsPolygon(prevLoc, loc, f.polygon));

    hit || crossed ? this.insideCount++ : this.outsideCount++;
    if (this.insideCount >= this.debounce && !this.isInside) {
      this.isInside = true; this.outsideCount = 0;
      this.onChange({ type: 'ENTER', fence: hit ? locateFence(this.fences, loc) : null });
    } else if (this.outsideCount >= this.debounce && this.isInside) {
      this.isInside = false; this.insideCount = 0;
      this.onChange({ type: 'LEAVE' });
    }
  }
}

function segmentIntersectsPolygon(a, b, poly) {
  return poly.some((p, i) => segIntersect(a, b, p, poly[(i + 1) % poly.length]));
}
```
