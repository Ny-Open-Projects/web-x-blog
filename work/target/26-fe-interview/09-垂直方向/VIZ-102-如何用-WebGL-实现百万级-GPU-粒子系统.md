---
title: [VIZ-102] 如何用 WebGL 实现百万级 GPU 粒子系统？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-102：如何用 WebGL 实现百万级 GPU 粒子系统？
**答**：核心思路是"状态放 GPU、CPU 只发一次"，三种做法：① 每帧 CPU 更新 BufferSubData——简单但 CPU 成为瓶颈；② WebGL2 **transform feedback** 在顶点着色器里更新位置写入另一块 buffer，乒乓交换，零 CPU 参与；③ 无状态粒子——位置完全由 `uTime` 在着色器里解析算出，CPU 每帧只更新一个 uniform。绘制用 `gl.drawArrays(gl.POINTS)` 一百万点一次 draw call。注意 gl_PointSize 有硬件上限，大粒子要用 billboard 四边形。

```javascript
// 无状态 GPU 粒子：种子数据只上传一次，位置由时间在顶点着色器解析计算
const N = 1000000;
const seeds = new Float32Array(N * 4); // xyz 初始位置 + w 随机相位
for (let i = 0; i < N; i++) {
  seeds[i * 4] = Math.random() * 2 - 1;
  seeds[i * 4 + 1] = Math.random() * 2 - 1;
  seeds[i * 4 + 2] = Math.random() * 2 - 1;
  seeds[i * 4 + 3] = Math.random();
}
gl.bindBuffer(gl.ARRAY_BUFFER, seedBuf);
gl.bufferData(gl.ARRAY_BUFFER, seeds, gl.STATIC_DRAW); // 一次性上传，STATIC_DRAW
// 顶点着色器核心逻辑：
// float t = fract(uTime * uSpeed + aSeed.w);          // 生命周期 0-1
// vec3 pos = aSeed.xyz + vec3(0.0, t * uRise, 0.0);   // 解析式位移，无需状态存储
// gl_PointSize = uSize * (1.0 - t);  vAlpha = 1.0 - t;
function frame(now) {
  gl.useProgram(prog);
  gl.uniform1f(uTimeLoc, (now / 1000) % 1);  // 每帧只更新一个 uniform
  gl.drawArrays(gl.POINTS, 0, N);            // 100 万点一次 draw call
  requestAnimationFrame(frame);
}
```
