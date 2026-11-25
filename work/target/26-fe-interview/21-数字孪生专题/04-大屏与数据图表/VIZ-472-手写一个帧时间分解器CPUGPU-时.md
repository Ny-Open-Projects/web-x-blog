---
title: [VIZ-472] 手写一个帧时间分解器：CPU/GPU 时间拆分
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## VIZ-472：手写一个帧时间分解器：CPU/GPU 时间拆分

**答**：
- 需求：implement frameBreakup(jsMs, gpuMs) 用 ext timer（WebGL EXT_disjoint_timer_query 模拟）输入 { jsMs, gpuMs }；判定瓶颈：gpuMs/jsMs > 1.5 GPU 瓶颈、< 0.67 CPU 瓶颈、否则均衡；输出 { verdict, utilization }（gpuMs/(max(jsMs,gpuMs)) 利用率）。
- 边界：值为 0 防除零；输出含建议（GPU 瓶颈 -> 降像素/顶点，CPU -> 减 draw）；两侧缺失按未知。
- 评分点：比值判定；利用率；零值防护；建议输出

```javascript
function frameBreakup({ jsMs, gpuMs } = {}) {
  if (jsMs == null || gpuMs == null)
    return { verdict: 'unknown', note: '需要 timer query 双侧数据' };
  const j = Math.max(jsMs, 1e-3), g = Math.max(gpuMs, 1e-3);
  const utilization = +(g / Math.max(j, g)).toFixed(2);
  if (g / j > 1.5)
    return { verdict: 'gpu-bound', utilization,
      note: '降分辨率/LOD/片元复杂度' };
  if (j / g > 1.5)
    return { verdict: 'cpu-bound', utilization,
      note: '减 draw/合批/移 Worker' };
  return { verdict: 'balanced', utilization, note: '均衡，双侧同步优化' };
}
```
