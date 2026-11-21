---
title: [R19-174] React 与 three.js 集成的思想是什么？react-three-fiber 为什么能"声明式渲染 3D"？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-174：React 与 three.js 集成的思想是什么？react-three-fiber 为什么能"声明式渲染 3D"？
**答**：
- R3F 的核心洞察：three.js 场景图（scene graph）本质是一棵**树**，把 three 的类映射为 JSX 元素、构造参数映射为 props，就得到了声明式 3D。
- 它是 renderer 而不是 wrapper：自定义 reconciler 接管 React 元素 -> three 对象的创建/挂载/更新，React 只负责"想渲染什么"，帧循环（useFrame）负责"怎么动"。
- 状态同步模式：声明式属性（position/材质）走 reconciler diff；每帧变化的量放 ref（meshRef.current.rotation），不进 state——3D 里 state 只描述"配置"，ref 描述"动画"。
- 交互桥接：three 的 raycaster 命中检测包装成 onClick/onPointerOver 等 React 事件。

```tsx
// r3f-demo.tsx —— react-three-fiber 的声明式 3D
import { Canvas, useFrame, type ThreeElements } from '@react-three/fiber';
import { useRef, useState } from 'react';
import * as THREE from 'three';

// 声明式：scene graph 直接用 JSX 表达
// <mesh geometry material> 对应 new THREE.Mesh(new THREE.BoxGeometry(), new THREE.MeshStandardMaterial())

function SpinningBox(props: ThreeElements['mesh']) {
  const meshRef = useRef<THREE.Mesh>(null!);   // 每帧动画走 ref，不走 state
  const [hovered, setHovered] = useState(false);
  const [clicked, setClicked] = useState(false);

  useFrame((_, delta) => {
    meshRef.current.rotation.x += delta;       // 帧循环：每帧增量更新
    meshRef.current.rotation.y += delta * 0.5;
  });

  return (
    <mesh
      {...props}
      ref={meshRef}
      scale={clicked ? 1.5 : 1}
      // R3F 把 raycaster 命中包装成 React 事件
      onPointerOver={() => setHovered(true)}
      onPointerOut={() => setHovered(false)}
      onClick={() => setClicked(c => !c)}
    >
      <boxGeometry args={[1, 1, 1]} />                     {/* BoxGeometry */}
      <meshStandardMaterial color={hovered ? 'orange' : 'skyblue'} />
    </mesh>
  );
}

export function Scene() {
  return (
    <Canvas camera={{ position: [0, 0, 5] }}>  {/* R3F 自带 render loop */}
      <ambientLight intensity={0.5} />         {/* new THREE.AmbientLight */}
      <pointLight position={[10, 10, 10]} />   {/* new THREE.PointLight */}
      <SpinningBox position={[0, 0, 0]} />     {/* mesh.position.set */}
    </Canvas>
  );
}

// 心智模型总结：
// state = 低频配置（颜色、选中态）；ref + useFrame = 高频逐帧量
// 永远不要在 useFrame 里 setState —— 60fps 的 setState 是 React 性能灾难
```
