---
title: [SCN-658] 大屏 WebGL/3D 性能优化怎么做？帧率掉到 20fps 怎么排查？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-658：大屏 3D 性能优化怎么做？
**答**：
- Draw call 治理：万级同类对象用 InstancedMesh/合并几何体；材质合并（共享 material）；贴图图集。
- 帧预算拆解：用 Spector/Chrome Tracing 看 draw call 数、三角形数、GPU 时间——掉帧三查：draw call 过多、overdraw 严重、每帧 JS 太重。
- 渲染分级：低端机降分辨率（renderer.setPixelRatio 调低）、关闭后处理（bloom/阴影）、LOD（远处模型换低模）。
- 空闲降频：大屏无人值守时段降帧（30fps 或按需渲染——场景不变不重绘，只有数据变化才 render）。
- 追问钩子：按需渲染怎么做——three.js 默认每帧渲染，改造成「场景脏 + 数据脏才渲染」，静止场景 GPU 占用接近 0。

```javascript
function onDemandRenderer(renderer, scene, camera, store) {
  let dirty = true;
  store.subscribe(() => { dirty = true; });        // 数据变更标脏
  window.addEventListener('resize', () => { dirty = true; });
  function loop() {
    if (dirty) {                                   // 只有脏才渲染
      renderer.render(scene, camera);
      dirty = false;
    }
    requestAnimationFrame(loop);
  }
  loop();
}
// 帧率监控
let frames = 0, last = performance.now();
function fpsProbe() {
  frames++;
  const now = performance.now();
  if (now - last >= 5000) {
    report({ type: 'FPS', value: frames / ((now - last) / 1000) });
    frames = 0; last = now;
  }
  requestAnimationFrame(fpsProbe);
}
```
