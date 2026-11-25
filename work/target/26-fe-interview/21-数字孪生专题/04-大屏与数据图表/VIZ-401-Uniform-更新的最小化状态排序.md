---
title: [VIZ-401] Uniform 更新的最小化：状态排序减少切换
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-401：Uniform 更新的最小化：状态排序减少切换

**答**：
- 切换成本：program 切换 > 纹理切换 > uniform 更新；按 program 分组排序 draw，组内按纹理排。
- 工具：每帧统计 switch 次数（Spector/自记）；目标 program 切换 < 20/帧。
- 实现：渲染队列（透明度/材质/深度分组）+ 排序键（programId, textureId, depth）。

```javascript
// 渲染队列排序
function sortDraws(draws) {
  return draws.sort((a, b) =>
    a.programId - b.programId ||
    a.textureId - b.textureId ||
    a.z - b.z);   // 不透明从前到后（early-z），透明从后到前
}
// 统计：
function frameStats(draws) {
  let pswitch = 0, tswitch = 0;
  for (let i = 1; i < draws.length; i++) {
    if (draws[i].programId !== draws[i-1].programId) pswitch++;
    if (draws[i].textureId !== draws[i-1].textureId) tswitch++;
  }
  return { pswitch, tswitch };
}
```
