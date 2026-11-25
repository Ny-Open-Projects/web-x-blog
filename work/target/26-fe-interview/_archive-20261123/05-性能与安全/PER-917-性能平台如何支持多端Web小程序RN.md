---
title: [PER-917] 性能平台如何支持多端（Web/小程序/RN）指标统一
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-917：性能平台如何支持多端（Web/小程序/RN）指标统一

**答**：
- 统一指标语义层：定义平台无关的指标模型（首屏、可交互、流畅度、稳定性），各端 SDK 负责映射到本地 API。
- 映射表：Web→LCP/INP；小程序→首屏时间+setData 耗时+触摸延迟；RN→JS 线程卡顿+TTI 近似；统一上报到同一 schema。
- 分端看板 + 全站总榜：既保留端差异细节，又能横向对比各端健康度。
- 口径文档化：每个指标的采集定义、局限性写进平台文档，防止跨端对比误读。

```javascript
// 统一指标 schema 与各端适配器
const SCHEMA = { firstPaint: 0, interactive: 0, jank: 0 }; // ms / 次/min
const adapters = {
  web: m => ({ firstPaint: m.lcp, interactive: m.tti, jank: m.longTasksPerMin }),
  mini: m => ({ firstPaint: m.firstRender, interactive: m.ready,
                jank: m.slowSetDataPerMin }),
  rn: m => ({ firstPaint: m.contentAppear, interactive: m.jsReady,
              jank: m.jsFrameDropsPerMin }),
};
function normalize(platform, m) { return { ...SCHEMA, ...adapters[platform](m) }; }
```
