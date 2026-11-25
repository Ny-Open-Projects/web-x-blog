---
title: [VIZ-028] WebGL 性能优化为什么要合并 draw call？instancing 怎么用？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-028：WebGL 性能优化为什么要合并 draw call？instancing 怎么用？
**答**：每次 draw call CPU 都要做状态校验、绑定切换与命令提交，GPU 本身很快，**瓶颈常在 CPU 提交侧**——10 万个三角形一次 draw 很轻松，1 万次 draw 则卡死。合批思路：把同材质图元拼进同一个缓冲一次画完。**instancing（实例化）**是合批的极致：同一 mesh 画 N 份、每份只差 transform/颜色这类"每实例属性"，用 `drawArraysInstanced` + `vertexAttribDivisor(1)` 一次 draw 搞定，海量散点图/图标渲染的标准答案。WebGL2 原生支持，WebGL1 用 ANGLE_instanced_arrays 扩展。

```javascript
// 1 万个同 mesh 不同 transform 的点/图标：instancing 把 1 万次 draw call 合成 1 次
const ext = gl.getExtension('ANGLE_instanced_arrays'); // WebGL2 原生无需扩展
const perInstance = new Float32Array(
  instances.flatMap(i => [i.x, i.y, i.scale])); // 每实例属性：偏移 + 缩放
const ibuf = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, ibuf);
gl.bufferData(gl.ARRAY_BUFFER, perInstance, gl.DYNAMIC_DRAW);
const aOffset = gl.getAttribLocation(prog, 'aOffset');
gl.enableVertexAttribArray(aOffset);
gl.vertexAttribPointer(aOffset, 3, gl.FLOAT, false, 12, 0);
ext.vertexAttribDivisorANGLE(aOffset, 1); // divisor=1：每实例更新一次，而非每顶点
ext.drawArraysInstancedANGLE(gl.TRIANGLE_STRIP, 0, 4, instanceCount);
// 对比：普通 draw 循环 1 万次 -> instanced 1 次，CPU 提交开销下降两个数量级
```
