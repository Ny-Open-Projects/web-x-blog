---
title: [VIZ-426] 体积渲染（Volume）的传输积分入门
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-426：体积渲染（Volume）的传输积分入门

**答**：
- 原理：沿视线积分吸收/发射（体数据密度），常 32~128 步采样 + 早停（透射率 < 0.01）。
- 数据：3D 纹理（医学 CT/流体模拟）三线性采样；WebGL2/WebGPU 支持 3D 纹理。
- 性能：半分辨率 + 时间上采样、空块剔除（包围盒先判定）。

```javascript
// 体积光线积分
function volumeRender(ro, rd, sampler, { steps = 64, maxDist = 5 } = {}) {
  let transmittance = 1, color = [0, 0, 0];
  const dt = maxDist / steps;
  for (let i = 0; i < steps && transmittance > 0.01; i++) {
    const p = ro.map((v, j) => v + rd[j] * dt * i);
    const density = sampler(p);                        // 0~1
    if (density > 0.01) {
      const emit = colormap(density);
      const a = density * dt * 10;                     // 吸收系数
      color = color.map((c, j) => c + transmittance * a * emit[j]);
      transmittance *= 1 - a;
    }
  }
  return { color, transmittance };
}
```
