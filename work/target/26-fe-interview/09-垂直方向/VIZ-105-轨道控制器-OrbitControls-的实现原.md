---
title: [VIZ-105] 轨道控制器 OrbitControls 的实现原理是什么？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-105：轨道控制器 OrbitControls 的实现原理是什么？
**答**：本质是**球面坐标 + 目标点**：相机始终看向 target，位置由半径 r、方位角 theta、极角 phi 的球面坐标决定。鼠标拖动 → 修改 theta/phi（带阻尼惯性）；滚轮 → 缩放 r（乘法缩放 + min/maxDistance 夹紧，手感与距离无关）；右键/双指 → 平移 target。每帧先按阻尼因子插值再由球面坐标重建相机位置并 lookAt。注意 phi 要夹在 (0.01, PI - 0.01) 避免极点万向节死锁。

```javascript
// 迷你轨道控制器：球面坐标 + 阻尼 + 乘法缩放
class MiniOrbit {
  constructor(camera, dom, target = new THREE.Vector3()) {
    this.camera = camera; this.dom = dom; this.target = target;
    this.sph = new THREE.Spherical().setFromVector3(camera.position.clone().sub(target));
    this.vel = { theta: 0, phi: 0 };
    dom.addEventListener('pointermove', e => {
      if (e.buttons !== 1) return;
      this.vel.theta -= e.movementX * 0.005;   // 拖动 -> 方位角速度
      this.vel.phi   -= e.movementY * 0.005;   // 拖动 -> 极角速度
    });
    dom.addEventListener('wheel', e => {
      const k = e.deltaY > 0 ? 1.1 : 0.9;      // 乘法缩放：手感与当前距离无关
      this.sph.radius = THREE.MathUtils.clamp(this.sph.radius * k, 5, 500);
      e.preventDefault();
    }, { passive: false });
  }
  update() {  // 每帧：阻尼逼近 + 重建相机位置
    this.sph.theta += this.vel.theta;
    this.sph.phi = THREE.MathUtils.clamp(this.sph.phi + this.vel.phi, 0.01, Math.PI - 0.01);
    this.vel.theta *= 0.85; this.vel.phi *= 0.85;   // 阻尼惯性
    const offset = new THREE.Vector3().setFromSpherical(this.sph);
    this.camera.position.copy(this.target).add(offset);
    this.camera.lookAt(this.target);
  }
}
```
