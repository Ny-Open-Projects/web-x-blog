---
title: [VIZ-412] Shader 特效：溶解/扫光/描边的经典实现
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-412：Shader 特效：溶解/扫光/描边的经典实现

**答**：
- 溶解：噪声阈值比较 alpha，边缘用阈值带宽做发光色——clipping mask 思路。
- 扫光：时间驱动的斜向渐变与纹理 alpha 相乘；描边：法线外扩（顶点）或后期边缘检测。
- 参数：全部走 uniform 时间驱动，零 CPU 每帧逻辑。

```javascript
// 经典特效片段
`// 溶解
float n = texture(uNoise, vUV).r;
float cut = smoothstep(uProgress - 0.1, uProgress, n);
if (cut < 0.5) discard;
vec3 edge = mix(vec3(1.0, 0.4, 0.1), uColor, smoothstep(uProgress - 0.02, uProgress, n));
color = mix(baseColor, edge, smoothstep(uProgress - 0.15, uProgress, n));
// 扫光
float sweep = smoothstep(0.0, 0.2, sin(vUV.x * 3.0 + uTime * 2.0) - 0.9);
color += sweep * uSweepColor;`
```
