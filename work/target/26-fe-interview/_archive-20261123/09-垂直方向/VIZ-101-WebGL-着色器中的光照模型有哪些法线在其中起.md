---
title: [VIZ-101] WebGL 着色器中的光照模型有哪些？法线在其中起什么作用？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-101：WebGL 着色器中的光照模型有哪些？法线在其中起什么作用？
**答**：三大经典模型递进：**Lambert** 只算漫反射 `max(dot(N, L), 0)` 最廉价；**Phong** 加镜面反射 `pow(dot(R, V), shininess)`，高光沿反射向量；**Blinn-Phong** 用半程向量 `H = normalize(L + V)` 替代反射向量，更便宜且高光更圆润，是实时渲染默认选择。法线 N 是所有光照的输入基石：模型被非均匀缩放时必须用法线矩阵（模型矩阵逆转置的 3x3 部分）变换法线并 normalize，否则光照方向错误。可视化中 3D 柱体、地球、机柜的质感都来自这套公式。

```glsl
// Blinn-Phong 光照：顶点着色器里必须用 normalMatrix 变换法线
attribute vec3 aNormal;
uniform mat4 uModel; uniform mat3 uNormalMatrix; uniform mat4 uViewProj;
varying vec3 vNormal; varying vec3 vWorldPos;
void main() {
  vec4 wp = uModel * vec4(aPosition, 1.0);
  vWorldPos = wp.xyz;
  vNormal = normalize(uNormalMatrix * aNormal); // 非均匀缩放必须用 normalMatrix
  gl_Position = uViewProj * wp;
}
// 片元着色器：漫反射 + 半程向量高光
precision mediump float;
varying vec3 vNormal; varying vec3 vWorldPos;
uniform vec3 uLightDir; uniform vec3 uEyePos; uniform vec3 uColor;
void main() {
  vec3 N = normalize(vNormal);
  vec3 L = normalize(uLightDir);
  vec3 V = normalize(uEyePos - vWorldPos);
  float diff = max(dot(N, L), 0.0);             // Lambert 漫反射
  vec3 H = normalize(L + V);                    // Blinn 半程向量
  float spec = pow(max(dot(N, H), 0.0), 64.0);  // 高光强度
  gl_FragColor = vec4(uColor * (0.25 + 0.75 * diff) + vec3(spec), 1.0);
}
```
