---
title: [VIZ-450] Instanced 拾取的精度与实例剔除
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-450：Instanced 拾取的精度与实例剔除

**答**：
- 实例化后拾取：ID pass（415）天然支持；CPU 侧需实例变换逆矩阵转换射线到局部空间。
- 剔除：实例级视锥/遮挡剔除每帧做（instance buffer 只发可见实例）——减少顶点与拾取开销。
- 数据结构：实例排序按剔除结果重建（每帧 bufferSubData）。

```javascript
// 实例剔除与重建
function cullInstances(instances, planes) {
  const visible = [];
  for (const it of instances) {
    const c = transformPoint(it.pos, it.mat);
    if (sphereInFrustum(c, it.radius, planes))       // 343
      visible.push(it);
  }
  return visible;
}
// 每帧：visible -> packInstances（358）-> bufferSubData；万实例剔除后通常 < 3k
```
