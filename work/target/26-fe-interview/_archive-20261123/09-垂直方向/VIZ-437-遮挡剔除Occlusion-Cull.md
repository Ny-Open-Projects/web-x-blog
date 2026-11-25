---
title: [VIZ-437] 遮挡剔除（Occlusion Culling）在 Web 端的实现
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-437：遮挡剔除（Occlusion Culling）在 Web 端的实现

**答**：
- 原理：视锥剔除只删视野外，遮挡剔除删视野内被挡住的——室内场景收益大（80% 物体被墙挡）。
- 实现：硬件查询（WebGL EXT_occlusion_query_boolean）或软件：深度金字塔（HZB）粗判遮挡。
- 简化：入口小孔剔除（portal）、房间图（每个房间可见房间列表预计算）。

```javascript
// HZB 遮挡测试
function hzbOccluded(bbox, depthPyramid) {
  const uv = projectBBox(bbox);                     // 包围盒投影
  const maxDepth = sampleMaxMip(depthPyramid, uv);  // 取 mip 链上最大深度
  return bbox.minZ > maxDepth + 0.001;              // 完全在已渲染深度之后
}
// 逐 mip 建 depth pyramid：每 mip 取 2×2 最大值
function buildPyramid(depthTex, levels) {
  const mips = [depthTex];
  for (let l = 1; l < levels; l++)
    mips.push(maxFilter2x2(mips[l - 1]));
  return mips;
}
```
