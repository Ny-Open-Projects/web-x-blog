---
title: [H5-212] three.js 场景三要素：scene-camera-renderer
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-212：three.js 场景三要素：scene、camera、renderer

**答**：
- scene 是场景图（节点树），所有 Mesh/Light/Group 挂载其上，变换逐层继承
- camera 不是场景成员而是观察者：PerspectiveCamera（fov/aspect/near/far）最常用；相机位置与 lookAt 决定视野
- renderer 每帧把 scene 用 camera 的视角画到 canvas；resize 时必须同步更新 camera.aspect 与 renderer.setSize
- 最小闭环 8 行代码可以跑起来，面试能默写说明真用过
- 常见坑：材质在暗场景全黑（没加光）、模型不显示（相机没对准或 far 太小）

```javascript
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, innerWidth / innerHeight, 0.1, 1000);
camera.position.z = 5;
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);
scene.add(new THREE.Mesh(new THREE.BoxGeometry(), new THREE.MeshNormalMaterial()));
(function loop() { requestAnimationFrame(loop); renderer.render(scene, camera); })();
addEventListener('resize', () => {
  camera.aspect = innerWidth / innerHeight; camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
```
