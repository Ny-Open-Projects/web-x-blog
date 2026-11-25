---
title: [NODE-765] 笔试题——实现容量预估计算器（漏斗→实例→全局校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-765：手写容量预估

**需求与边界**：
- 需求：大促容量预估（SCN-NODE-699）——① 漏斗换算（UV → 各接口 QPS——转化系数）；② 实例数计算（压测单实例 × 系数）；③ 全局校验（连接池×实例 ≤ DB max、Redis QPS ≤ 上限——SCN-NODE-699 一致性）；④ 预算输出（扩容清单/成本）。
- 边界：① 放大系数来源（历史大促数据——非拍脑袋）；② 峰值系数（1.5× 冗余——SCN-NODE-647）；③ 校验失败的处理（减实例或提下游——双向调整建议）。

**答**：
```javascript
function capacityCalc({ uv, funnel, steadyPerInstance, poolMax, dbMaxConn, redisCap, surge = 1.5 }) {
  const qpsByApi = {};                                 // 漏斗换算（历史放大系数）
  for (const [api, conv] of Object.entries(funnel))
    qpsByApi[api] = uv * conv * historicalAmplifier(api);   // 峰值 QPS/接口
  const peakQps = Math.max(...Object.values(qpsByApi));
  const instances = Math.ceil(peakQps * surge / steadyPerInstance);   // 实例数（SCN-NODE-647）
  const checks = {
    db: { need: instances * poolMax, cap: dbMaxConn, ok: instances * poolMax <= dbMaxConn },
    redis: { need: peakQps * instances * redisRatio, cap: redisCap,
      ok: peakQps * instances * redisRatio <= redisCap },   // 全局一致性校验（SCN-NODE-699）
  };
  const violations = Object.entries(checks).filter(([, c]) => !c.ok);
  return { qpsByApi, instances, checks,
    action: violations.length
      ? { reduce: '降低实例数', expand: violations.map(v => `扩 ${v[0]}`) }   // 双向调整建议
      : 'PASS', cost: instanceCost(instances) };
}
```

**评分点**:
- 漏斗换算 + 历史放大系数（数据驱动——SCN-NODE-699）。
- 全局一致性校验（连接池×实例 ≤ DB max——核心校验）。
- 双向调整建议（减实例或扩下游——可行动）。
- surge 冗余系数（1.5×——SCN-NODE-647 压测方法论）。
