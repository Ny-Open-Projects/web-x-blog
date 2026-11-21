---
title: [VIZ-029] Three.js 的场景图与渲染循环如何工作？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-029：Three.js 的场景图与渲染循环如何工作？
**答**：场景图是 Object3D 树：每个节点携带自己的局部变换，**父级变换级联作用于子级**（渲染时自顶向下算世界矩阵）。渲染循环 `renderer.render(scene, camera)` 做四件事：更新世界矩阵 → 视锥剔除 → 按材质/几何分组合并 draw call → 提交 WebGL。工程要点：动画只在 rAF 循环里改 transform；页面不可见暂停循环；resize 时同步 `camera.aspect` 与 `renderer.setSize`；静态对象合并 geometry 或用 InstancedMesh 降 draw call。

```javascript
import * as THREE from 'three';
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, innerWidth / innerHeight, 0.1, 1000);
camera.position.set(0, 5, 10);
camera.lookAt(0, 0, 0);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);
// 场景图：Object3D 树，父级变换级联影响子级
const group = new THREE.Group();
group.add(new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshNormalMaterial()));
scene.add(group);
function tick(t) {
  group.rotation.y = t / 1000;         // 每帧只更新变换，渲染交给 render()
  renderer.render(scene, camera);      // 更新世界矩阵 -> 剔除 -> 合批 -> WebGL
  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
addEventListener('resize', () => {     // resize 必须同步相机纵横比与画布尺寸
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
```

---

## 五、ECharts 工程（VIZ-030 ~ VIZ-037）
