---
title: [VIZ-446] SVG 大规模节点性能与 Canvas 化边界
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-446：SVG 大规模节点性能与 Canvas 化边界

**答**：
- SVG 优势：DOM 事件/无障碍/样式级交互；节点 > 2000 或高频重绘时布局/合成崩。
- 边界判定：节点数 × 更新频率打分，超阈值切 Canvas（保留 SVG 层做交互覆盖层）。
- 折中：SVG 分层（静态层 + 动态层），动态节点最小化。

```javascript
// SVG/Canvas 切换判定
function svgVsCanvas(nodeCount, updatesPerSec) {
  const score = nodeCount * updatesPerSec;
  return { score, verdict:
    score > 50000 ? 'canvas（或分层）' :
    score > 10000 ? 'svg 分层：动态节点 canvas、静态 svg' : 'svg 可用' };
}
console.log(svgVsCanvas(3000, 30));   // -> canvas
```
