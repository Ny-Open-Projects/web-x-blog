---
title: [H5-214] WebGL 帧循环的性能预算：drawcall
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-214：WebGL 帧循环的性能预算：drawcall

**答**：
- drawcall = 一次 gl.drawArrays/drawElements 调用；CPU 侧有固定开销（状态提交），数量大了 CPU 成瓶颈而 GPU 闲着
- 经验量级：移动端目标 100 以内、桌面 500 以内（因设备而异，看 CPU 占用比）
- 减 drawcall 手段：合并几何体（相同材质的 mesh merge）、纹理图集（一张图装多个小图减少切换）、实例化渲染（InstancedMesh，一次画一万棵草）
- 帧循环预算分配：16.6ms 里 CPU 准备（JS/提交）+ GPU 绘制要流水线重叠，任何一侧满载都会掉帧
- 检测工具：Spector.js 抓帧看 drawcall 明细、three.js 的 renderer.info

```javascript
// three.js 实例化：1 个 drawcall 画 10000 个实例
const grass = new THREE.InstancedMesh(geo, mat, 10000);
const m = new THREE.Matrix4();
for (let i = 0; i < 10000; i++) {
  m.setPosition(Math.random() * 100, 0, Math.random() * 100);
  grass.setMatrixAt(i, m);
}
console.log(renderer.info.render.calls); // drawcall 数
```
