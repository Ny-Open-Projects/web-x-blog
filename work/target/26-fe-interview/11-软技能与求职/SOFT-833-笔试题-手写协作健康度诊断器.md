---
title: [SOFT-833] 手写 collabHealthCheck：三层指标（任务/关系/机制）采集与诊断、优先改进项生成？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-833：手写 collabHealthCheck：三层指标（任务/关系/机制）采集与诊断、优先改进项生成

**需求与边界**：
- 实现 collabHealthCheck(metrics)。
- 边界要求：① 三层指标：任务层（返工率/等待时长）、关系层（异见频率/摩擦事件数/互评活跃度）、机制层（RACI 覆盖率/ADR 归档率）；② 每指标带阈值（超出判差）；③ 诊断输出：最差层定位+优先改进项（SOFT-821 诊断逻辑）；④ 分数缺失的指标标 MISSING（不编数）。

**答**：
```javascript
const THRESHOLDS = {
  task: { reworkRate: 0.15, waitHours: 24 },
  relation: { dissentPerMonth: 2, frictionPerQuarter: 3, peerReviewActive: true },
  mechanism: { raciCoverage: 0.8, adrArchiveRate: 0.7 },
};
function collabHealthCheck(metrics) {
  const layer = (name, checks) => {
    const bad = checks.filter(c => {
      const v = metrics[name]?.[c.key];
      return v == null ? 'MISSING' : v > c.max || v < c.min;
    });
    return { layer: name, bad };
  };
  const rows = [
    layer('task', [
      { key: 'reworkRate', max: THRESHOLDS.task.reworkRate, min: 0 },
      { key: 'waitHours', max: THRESHOLDS.task.waitHours, min: 0 }]),
    layer('relation', [
      { key: 'dissentPerMonth', min: THRESHOLDS.relation.dissentPerMonth, max: 99 },
      { key: 'frictionPerQuarter', max: THRESHOLDS.relation.frictionPerQuarter, min: 0 }]),
    layer('mechanism', [
      { key: 'raciCoverage', min: THRESHOLDS.mechanism.raciCoverage, max: 1 },
      { key: 'adrArchiveRate', min: THRESHOLDS.mechanism.adrArchiveRate, max: 1 }]),
  ];
  const worst = rows.reduce((a, b) => b.bad.length > a.bad.length ? b : a);
  const FIX = { task: '微习惯五件+同步分级（SOFT-815/824）',
    relation: '心理安全四建立+1:1常态化（SOFT-818/591）',
    mechanism: '机制清单六件补齐（SOFT-811）' };
  return { rows,
    missing: rows.flatMap(r => r.bad.filter(b => b === 'MISSING')),
    priority: worst.bad.length ? `优先改进：${worst.layer}层——${FIX[worst.layer]}`
      : '三层健康' };
}
```

**评分点**:
- 三层指标体系与阈值判差（SOFT-821/830 的落地工具）。
- 最差层定位+对应改进包路由（诊断→行动闭环）。
- MISSING 不编数（诚实性）。

