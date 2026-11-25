---
title: [DP-325] 笔试题：手写热力图采集（点击坐标聚合）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-325：笔试题：手写热力图采集（点击坐标聚合）？
**答**：实现点击热力采集：1) 点击事件按 (页面路径, 10% 网格坐标) 聚合计数；2) resize 后坐标归一化（相对视口百分比）不漂移；3) 批量上报（beacon）；4) 移动端 touch 兼容。
**评分点**：
- 网格 key 计算正确（Math.floor(x/grid)）。
- 坐标相对百分比归一化（抗 resize）。
- 批量聚合 Map 结构与 flush。
- pointerdown 兼容触摸。
```javascript
const grid = 10;   // 10% 网格
const heat = new Map();   // 'path|gx|gy' → count
function collect(e) {
  const x = e.clientX / innerWidth, y = e.clientY / innerHeight;    // 2) 百分比归一
  const key = `${location.pathname}|${Math.floor(x * grid)}|${Math.floor(y * grid)}`;   // 1)
  heat.set(key, (heat.get(key) ?? 0) + 1);
}
document.addEventListener('pointerdown', collect, { passive: true });   // 4) 触摸兼容
setInterval(() => {                                      // 3) 批量上报
  if (!heat.size) return;
  const batch = { path: location.pathname, vw: innerWidth, vh: innerHeight,
    points: [...heat.entries()].map(([k, n]) => { const [, gx, gy] = k.split('|');
      return { gx: +gx, gy: +gy, n }; }) };
  heat.clear();
  navigator.sendBeacon('/heatmap', JSON.stringify(batch));
}, 10000);
// 服务端回放：x = (gx + 0.5) / grid * vw
```
