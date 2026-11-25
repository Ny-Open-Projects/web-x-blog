---
title: [VIZ-457] 自适应质量系统（Quality Preset）的构建
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-457：自适应质量系统（Quality Preset）的构建

**答**：
- 档位：按设备评分（GPU 型号/内存/DPR/实测帧率）映射 L0~L3 预设（分辨率/阴影/粒子/后处理开关）。
- 动态修正：运行时帧率不达标逐级降档（439 联动）。
- 初始化：首 5 秒基准测试（渲染标准场景测帧时间）定档，避免误判。

```javascript
// 质量档位
const PRESETS = {
  L0: { resScale: 0.6, shadows: false, particles: 500, bloom: false },
  L1: { resScale: 0.8, shadows: 'low', particles: 2000, bloom: true },
  L2: { resScale: 1.0, shadows: 'medium', particles: 5000, bloom: true },
  L3: { resScale: 1.0, shadows: 'high', particles: 10000, bloom: true },
};
function pickPreset(benchFps, deviceMem) {
  if (benchFps < 30 || deviceMem <= 2) return 'L0';
  if (benchFps < 45 || deviceMem <= 4) return 'L1';
  return benchFps >= 58 ? 'L3' : 'L2';
}
```
