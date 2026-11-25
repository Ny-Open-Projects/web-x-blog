---
title: [H5-275] WebGL 性能优化思路：合批-纹理图集-降分辨率
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-275：WebGL 性能优化思路：合批、纹理图集、降分辨率

**答**：
- 先定位瓶颈：drawcall 多（CPU 提交瓶颈）还是片元复杂（GPU 填充瓶颈）？renderer.info 和 Spector.js 看数据再动手
- 减 drawcall：同材质几何体合并、InstancedMesh 实例化、纹理图集（一张大图装小图，减少 bindTexture 切换）
- 减像素成本：复杂 shader 降采样（半分辨率渲染再放大）、限制 devicePixelRatio 上限（retina 上 dpr=2 已够）、关闭不必要的后处理
- 资源侧：KTX 压缩纹理（解码快、显存省）、模型减面+Draco 压缩、按需加载与显存回收
- 预算话术：移动端帧预算 16.6ms，drawcall <100、三角形 <50 万是常见经验值，超了先砍哪个要能说出来

```javascript
renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5)); // 限制 retina 开销
console.log(renderer.info.render.triangles, renderer.info.render.calls);
```
