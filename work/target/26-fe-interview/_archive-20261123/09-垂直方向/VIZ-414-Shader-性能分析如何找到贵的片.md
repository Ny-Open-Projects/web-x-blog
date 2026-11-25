---
title: [VIZ-414] Shader 性能分析：如何找到"贵"的片元代码
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-414：Shader 性能分析：如何找到"贵"的片元代码

**答**：
- 工具：Spector.js 捕帧看 draw 耗时、Qualcomm/Mali/Metal shader 分析器看 ALU/寄存器占用。
- 指标：寄存器溢出（spilling）是最大杀手——减少同时活跃变量、拆分复杂函数。
- 定位法：二分注释（注释一半代码看耗时变化）快速定位热点行。

```javascript
// 耗时自测框架
function benchPass(gl, pass, frames = 100) {
  gl.finish();                       // 排空
  const t0 = performance.now();
  for (let i = 0; i < frames; i++) pass();
  gl.finish();                       // 等 GPU 完成
  return (performance.now() - t0) / frames;   // ms/帧
}
// 对比注释前后差值定位热点；
// 寄存器提示：WGP（WebGPU）编译日志或 vendor 工具看 reg usage
```
