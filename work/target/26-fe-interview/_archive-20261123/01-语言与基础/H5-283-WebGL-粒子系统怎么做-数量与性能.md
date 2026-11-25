---
title: [H5-283] WebGL 粒子系统怎么做：数量与性能
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-283：WebGL 粒子系统怎么做：数量与性能

**答**：
- 数据结构：所有粒子的位置/速度/生命值放在一个大 TypedArray（Float32Array）里，SOA 布局利于批量更新
- 更新位置三档选择：CPU 每帧写 buffer（几千个粒子够用）→ GPU shader 内算（把时间 uniform 传入，粒子位置由公式生成，10 万级）→ transform feedback/GPU 模拟（WebGL2 百万级）
- 渲染：gl.POINTS 最省；想要圆点/纹理用点大小 varying + 片元纹理；或小面片 instancing
- 性能红线：每帧 bufferData 全量上传（CPU→GPU 拷贝）是主要开销，尽量 shader 内算或只更新变化的区间
- 面试话术：能说出「CPU 更新 vs GPU 更新」的临界点（约 1 万粒子）与理由

```javascript
// GPU 侧更新：位置由时间公式生成，CPU 零负担
attribute vec3 aSeed; // 每粒子随机种子
uniform float uTime;
void main() {
  float t = mod(uTime + aSeed.x * 10.0, 10.0); // 循环生命周期
  vec3 pos = aSeed + vec3(0.0, t * 2.0, 0.0);  // 上升烟花
  gl_Position = projectionMatrix * viewMatrix * vec4(pos, 1.0);
  gl_PointSize = 4.0 * (1.0 - t / 10.0);       // 渐隐
}
```
