---
title: [VIZ-368] PBR 基础：BRDF 的组成（漫反射 + 高光）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-368：PBR 基础：BRDF 的组成（漫反射 + 高光）

**答**：
- PBR 材质参数：albedo（基础色）、metallic（金属度）、roughness（粗糙度）—— metallic/roughness 工作流是 glTF 标准。
- 漫反射：Lambert albedo/π；高光：GGX/Trowbridge-Reitz 分布（roughness 驱动高光宽度）。
- Fresnel：Schlick 近似 F(θ) = F0 + (1-F0)(1-cosθ)^5，F0 = ((n-1)/(n+1))²，金属 F0 带颜色。

```javascript
// GGX 高光 + Schlick Fresnel
function fresnelSchlick(cosTheta, F0) {
  return F0.map(f => f + (1 - f) * Math.pow(1 - cosTheta, 5));
}
function ggxD(NdotH, roughness) {
  const a = roughness * roughness;
  const a2 = a * a;
  const d = NdotH * NdotH * (a2 - 1) + 1;
  return a2 / (Math.PI * d * d || 1e-9);
}
const F0_dielectric = [0.04, 0.04, 0.04];    // 塑料
const F0_metal = albedo;                      // 金属用 albedo 作 F0
```
