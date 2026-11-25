---
title: [VIZ-397] 着色器分支（if）的代价与分支消除技巧
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-397：着色器分支（if）的代价与分支消除技巧

**答**：
- GPU 按 warp 执行：同 warp 内分支发散则两侧都执行——数据分歧大时 if 不省反贵。
- 技巧：step/mix 消除分支、early return 按 warp 统一、循环次数常量化（可编译展开）。
- 例外：分支内访问纹理/大循环时真分支能省带宽——按材质分组 draw 让分支统一。

```javascript
// 分支消除示例
// 反模式：
// if (metallic > 0.5) { color = F0; } else { color = 0.04; }
// 改写：
// vec3 F0 = mix(vec3(0.04), albedo, metallic);
// 循环展开：
// #pragma unroll 或 for (int i = 0; i < LIGHT_COUNT; i++)  // LIGHT_COUNT 用 define
```
