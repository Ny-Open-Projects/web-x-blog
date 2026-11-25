---
title: [VIZ-234] 图表刻度生成（niceTicks）：人类可读刻度算法
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-234：图表刻度生成（niceTicks）：人类可读刻度算法

**答**：
- 题目：给定值域 [min, max] 与目标刻度数（约 5~8 个），生成「好看」的刻度（1/2/5×10^n 步长）。实现 niceTicks。
- 思路：step = (max-min)/目标数 → 归一到 1/2/5 量级（step/10^n 落 [1,10) 后就近取 1/2/5）；起始刻度 = ceil(min/step)×step。
- 评分点：量级归一；1/2/5 序列；起点对齐（从 min 向下取整到 step 倍数）。

```javascript
function niceTicks(min, max, targetCount = 6) {
  const span = max - min;
  const rawStep = span / targetCount;
  const mag = Math.pow(10, Math.floor(Math.log10(rawStep)));   // 量级
  const norm = rawStep / mag;                            // 归一到 [1, 10)
  const step = (norm >= 5 ? 5 : norm >= 2 ? 2 : 1) * mag;   // 1/2/5 就近
  const start = Math.ceil(min / step) * step;            // 起点对齐
  const ticks = [];
  for (let v = start; v <= max + 1e-9; v += step)
    ticks.push(+v.toFixed(10));                          // 浮点误差清理
  return { ticks, step };
}
// 例：[3, 97] 6 档 → rawStep≈15.7 → mag=10, norm=1.57 → step=2×10=20 → ticks [20,40,60,80]
```
