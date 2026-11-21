---
title: [DP-292] 笔试题：手写策略路由与 AB 分流？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-292：笔试题：手写策略路由与 AB 分流？
**题目**：实现分流器：1) `assign(userId, layer, experiments)` 返回该用户在各实验的分组（control/treat）；2) 分桶确定性（同用户同结果）；3) 层间正交（不同层独立分配）；4) 白名单强制分组；5) SRM 校验函数（观测比例 vs 配置比例，p 值近似）。
**评分点**：
- hash 分桶确定性（稳定字符串 hash + salt）。
- 层 salt 隔离（layer 进 hash 输入）。
- 白名单优先级高于分桶。
- SRM：比例偏差 > 阈值报异常（z 检验近似即可）。
```javascript
function hash(s) { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) >>> 0; return h; }
function assign(userId, layer, experiments) {
  const result = {};
  for (const exp of experiments) {                       // 3) 层间正交：layer+salt 进 hash
    if (exp.whitelist?.[userId]) { result[exp.name] = exp.whitelist[userId]; continue; }   // 4) 白名单
    const bucket = hash(`${layer}:${exp.salt}:${userId}`) % 100;
    result[exp.name] = bucket < exp.ratio ? 'treat' : 'control';
  }
  return result;
}
function srm(observedTreat, observedControl, configuredRatio) {    // 5)
  const n = observedTreat + observedControl;
  if (!n) return { ok: false, reason: 'no sample' };
  const expectTreat = n * configuredRatio;
  const z = (observedTreat - expectTreat) / Math.sqrt(expectTreat * (1 - configuredRatio));
  return { z, ok: Math.abs(z) < 3 };                     // |z|<3 近似 p>0.001
}
```
