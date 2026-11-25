---
title: [VIZ-362] 实例化渲染（Instancing）的数学与适用条件
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-362：实例化渲染（Instancing）的数学与适用条件

**答**：
- 条件：同一几何体大量重复（树/草/粒子），仅变换不同——一次 draw 画 N 个实例。
- 实例属性：每实例变换矩阵（或 position+scale+rot 分量）存 instance buffer；顶点着色器 gl_InstanceID 取。
- 收益：draw call 从 N 降到 1，CPU 提交成本骤降；GPU 侧顶点量不变。

```javascript
// 实例变换打包（WebGL2 / WebGPU）
function packInstances(instances) {
  // 每实例：pos(3) + scale(1) + quat(4) = 8 floats
  const out = new Float32Array(instances.length * 8);
  instances.forEach((it, i) => {
    out.set([...it.pos, it.scale, ...it.quat], i * 8);
  });
  return out;
}
// vertex shader:
// vec3 pos = aPos * aScale + aInstancePos;
// vec4 q = aQuat; // 旋转用四元数变换 position
// 1 万棵树：1 draw call，帧时间从 12ms -> 2ms
```
