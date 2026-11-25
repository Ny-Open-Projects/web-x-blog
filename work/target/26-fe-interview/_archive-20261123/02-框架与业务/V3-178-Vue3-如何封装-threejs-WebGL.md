---
title: [V3-178] Vue3 如何封装 three.js（WebGL）组件？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-178：Vue3 如何封装 three.js（WebGL）组件？
**答**：
- 生命周期映射：scene/camera/renderer 全部在 onMounted 创建，onUnmounted 里 renderer.dispose + geometry/material dispose + 释放 WebGL 上下文，防 GPU 内存泄漏。
- 响应式桥接：props（颜色、旋转速度、模型地址）经 watch 更新 three 对象属性；交互状态经 ref + defineExpose 暴露。
- 渲染循环用 requestAnimationFrame，卸载时 cancelAnimationFrame；页面不可见时暂停可省电。
- 资源加载（GLTFLoader）是异步的，配合 Suspense 或内部 loading 状态展示骨架。

```vue
<!-- components/ThreeBox.vue -->
<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from "vue";
import * as THREE from "three";

const props = defineProps<{ color: string; spin: boolean }>();

const wrapRef = ref<HTMLDivElement | null>(null);
let renderer: THREE.WebGLRenderer, scene: THREE.Scene, camera: THREE.PerspectiveCamera;
let mesh: THREE.Mesh, rafId = 0;

function animate() {
  rafId = requestAnimationFrame(animate);
  if (props.spin) mesh.rotation.y += 0.01; // props 直读：渲染循环里保持响应
  renderer.render(scene, camera);
}

onMounted(() => {
  const { clientWidth: w, clientHeight: h } = wrapRef.value!;
  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(w, h);
  wrapRef.value!.appendChild(renderer.domElement);

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(45, w / h, 0.1, 100);
  camera.position.z = 5;

  mesh = new THREE.Mesh(
    new THREE.BoxGeometry(2, 2, 2),
    new THREE.MeshStandardMaterial({ color: props.color })
  );
  scene.add(mesh);
  scene.add(new THREE.AmbientLight(0xffffff, 0.8));
  scene.add(new THREE.DirectionalLight(0xffffff, 1));

  animate();
});

// 响应式 -> three 对象：颜色变化直接改 material
watch(() => props.color, (c) => {
  (mesh?.material as THREE.MeshStandardMaterial)?.color.set(c);
});

onUnmounted(() => {
  cancelAnimationFrame(rafId);
  // 完整释放：几何体、材质、渲染器、GL 上下文
  mesh.geometry.dispose();
  (mesh.material as THREE.Material).dispose();
  renderer.dispose();
  renderer.domElement.remove();
});
</script>

<template>
  <div ref="wrapRef" class="stage" />
</template>

<style>
.stage { width: 100%; height: 360px; }
</style>
```
