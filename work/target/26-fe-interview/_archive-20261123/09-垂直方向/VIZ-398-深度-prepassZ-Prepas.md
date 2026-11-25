---
title: [VIZ-398] 深度 prepass（Z-Prepass）什么时候值得做
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-398：深度 prepass（Z-Prepass）什么时候值得做

**答**：
- 原理：先只写深度渲染一遍，主 pass 片元提前深度剔除——复杂片元着色器（PBR 多光源）省大量像素成本。
- 条件：片元着色器贵 + overdraw 严重（场景重叠多）才划算；简单场景两遍渲染反而更慢。
- 移动端：tile-based GPU 上 prepass 收益有限（HSR 已做 hidden surface removal）。

```javascript
// prepass 收益估算
function prepassWorth({ fragCostUs, overdraw, drawCostUs }) {
  const saved = fragCostUs * (overdraw - 1);       // 省下的重复片元
  const extra = drawCostUs;                        // 多一遍几何成本
  return { saved: +saved.toFixed(2), extra,
    worth: saved > extra,
    note: 'overdraw < 2 时不值得（移动端 HSR 自动处理）' };
}
// overdraw 用渲染重叠计数 pass 实测
```
