---
title: [PER-098] WebGL/Canvas 应用的性能基线怎么建立？关键指标有哪些？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-098：WebGL/Canvas 应用的性能基线怎么建立？关键指标有哪些？

**答**：
- 基线四指标：**帧时间**（rAF 间隔 p95 < 16.7ms）、**draw call 数**（每帧百级以内）、**显存占用**（纹理总量）、**JS 每帧耗时**（逻辑更新 < 4ms）。
- 常见瓶颈排序：draw call 过多（用实例化渲染合并）> 纹理过大/格式不对（用压缩纹理格式）> 每帧 GC（对象池）> 着色器过重。
- 建立方法：在多档设备上录基线（旗舰/中端/低端机各一组指标），低于基线即告警；用 `renderer.info`（three.js）或 self-reported 统计。
- 探针注意：GPU 耗时无法直接读，用“CPU 提交后空闲时间”估算，或用 EXT_disjoint_timer_query 扩展。

```javascript
// three.js 渲染循环：基线指标采集
import * as THREE from 'three';

const renderer = new THREE.WebGLRenderer({ antialias: false, powerPreference: 'high-performance' });
const frameStats = { jsTime: [], fps: [] };
let last = performance.now();

renderer.setAnimationLoop(() => {
  const t0 = performance.now();
  updateLogic();                       // 逻辑更新，目标 < 4ms
  renderer.render(scene, camera);
  frameStats.jsTime.push(performance.now() - t0);

  const info = renderer.info;          // 每帧 draw call 与三角形数
  if (info.render.calls > 150) {
    console.warn('draw call 超标', info.render.calls); // 考虑 InstancedMesh 合并
  }
  const now = performance.now();
  frameStats.fps.push(1000 / (now - last));
  last = now;
  if (frameStats.fps.length >= 120) {  // 每 2 秒汇总上报一次基线
    reportBaseline({
      jsP95: percentile(frameStats.jsTime, 0.95).toFixed(2),
      fpsP05: percentile(frameStats.fps, 0.05).toFixed(1),
      calls: info.render.calls,
      triangles: info.render.triangles,
      geometries: info.memory.geometries,   // 显存侧资源数
      textures: info.memory.textures,
    });
    frameStats.jsTime.length = 0; frameStats.fps.length = 0;
  }
});
```

## 十六、监控体系深化
