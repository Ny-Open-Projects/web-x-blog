---
title: [ARC-289] 灰度与 AB 平台的观测时长与统计功效平衡？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-289：灰度与 AB 平台的观测时长与统计功效平衡？
**答**：
- 核心权衡：观察越长结论越稳（功效高、覆盖周内行为周期），但业务等不起；太短则假阳性/假阴性都高。平台给出"最少观察周期"的科学依据：样本量 + 周期效应（至少覆盖一个完整周，周末行为不同）。
- 提速手段（不牺牲正确性）：提高 MDE（接受检测更大效应）、CUPED 用实验前数据降方差（样本量可减 20%~40%）、序贯检验（提前显著可提前停，但需要预设边界）。
- 平台功能：实验面板展示"预计完成时间"（按当前流量速率），T-7 冻结期前未完成的实验给出"延长/放弃"建议。
- 陷阱提示：提前停止是统计上最常见错误——序贯检验必须用 alpha-spending 边界，普通 z 检验不允许中途停。

```typescript
// 预计完成时间
function eta(exp, dailyTraffic) {
  const perArmDaily = dailyTraffic * exp.ratio / 2;
  const need = exp.requiredN - exp.currentN;
  return { days: Math.ceil(need / perArmDaily), minDays: Math.max(need / perArmDaily, 7) }; // 至少一个完整周
}
// CUPED：y' = y - θ(x - mean(x))，x=实验前 7 天同指标 → 方差下降 θ²·var(x)/var(y)
// 序贯：alphaSpending(n, N) 边界表，p < 边界才允许提前停
```
