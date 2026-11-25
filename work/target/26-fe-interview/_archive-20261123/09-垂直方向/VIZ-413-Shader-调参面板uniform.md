---
title: [VIZ-413] Shader 调参面板：uniform 与 UI 联动
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-413：Shader 调参面板：uniform 与 UI 联动

**答**：
- 机制：声明 uniform 元数据（名称/范围/默认值）自动生成调参面板（dat.GUI/lil-gui 风格）。
- 实时性：onChange 直接 gl.uniform1f，免重建 program；保存快照导出代码。
- 规范：调参名走语义命名（uNoiseScale 而非 u1），避免调完忘了含义。

```javascript
// uniform 元数据驱动 UI
const PARAMS = [
  { name: 'uNoiseScale', min: 0, max: 5, step: 0.01, value: 1.2 },
  { name: 'uProgress', min: 0, max: 1, step: 0.01, value: 0 },
];
function buildPanel(gl, prog) {
  const state = {};
  for (const p of PARAMS) {
    state[p.name] = p.value;
    gui.add(state, p.name, p.min, p.max, p.step)
      .onChange(v => gl.uniform1f(gl.getUniformLocation(prog, p.name), v));
  }
  return state;
}
```
