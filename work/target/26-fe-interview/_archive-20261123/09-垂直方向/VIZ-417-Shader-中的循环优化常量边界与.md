---
title: [VIZ-417] Shader 中的循环优化：常量边界与展开
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-417：Shader 中的循环优化：常量边界与展开

**答**：
- 循环边界必须可静态推导（uniform 循环上限 + break）或用常量 define——否则部分驱动编译慢。
- 纹理循环：mip 链采样（bloom 降采样）循环展开后更快（寄存器换速度）。
- 嵌套循环：内层优先小循环（指令缓存友好）；数据驱动的循环改数据布局（预展开）。

```javascript
// 循环模板
`// 可静态推导：
const int MAX_LIGHTS = 16;
uniform int uLightCount;
for (int i = 0; i < MAX_LIGHTS; i++) {
  if (i >= uLightCount) break;     // 统一 break，warp 发散小
  ...
}
// 完全展开（宏生成）：
#define LIGHT_LOOP(n) for (int i = 0; i < n; i++)
// LIGHT_LOOP(8) { ... }`
```
