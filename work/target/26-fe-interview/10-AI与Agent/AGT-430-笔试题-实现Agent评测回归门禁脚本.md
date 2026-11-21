---
title: [AGT-430] 笔试题——实现评测回归门禁（新旧对比+分级统计+阻断）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-430：手写回归门禁：双版本跑集、逐任务对比、分级统计与阻断决策

**需求与边界**：
- 输入：评测集、新旧配置、阈值 {successDelta, costDelta}；输出：报告+决策（pass/block/gray）。
- 边界要求：① 新旧并行跑同集（环境固定 mock 工具）；② 逐任务分级（提升/持平/退化/翻转）；③ 核心成功率下降超阈值阻断；④ 成本上涨超阈值单独告警（质量过成本不过也要灰度）。

**答**：
```javascript
async function regressionGate({ suite, oldCfg, newCfg,
  thresholds = { successDelta: 0.02, costDelta: 0.1 } }) {
  const env = mockEnv(suite);                    // 固定环境（mock 工具）
  const [oldR, newR] = await Promise.all([
    runSuite(suite, oldCfg, env),
    runSuite(suite, newCfg, env)]);
  const cmp = suite.map(c => {
    const o = oldR.get(c.id), n = newR.get(c.id);
    const d = n.score - o.score;
    const grade = d > 0.1 ? 'better' : d < -0.1 ? 'worse'
      : (o.score >= 1 && n.score < 1) ? 'flipped' : 'same';
    return { id: c.id, old: o.score, new: n.score, delta: d,
      grade, costDelta: n.cost - o.cost, hard: c.hard ?? false };
  });
  const stat = {
    successOld: avg(oldR.mapScore), successNew: avg(newR.mapScore),
    delta: avg(newR.mapScore) - avg(oldR.mapScore),
    worse: cmp.filter(x => x.grade === 'worse' || x.grade === 'flipped'),
    hardWorse: cmp.filter(x => x.hard &&
      (x.grade === 'worse' || x.grade === 'flipped')),
    costDelta: cmp.reduce((s, x) => s + x.costDelta, 0) / cmp.length,
  };
  let decision = 'pass';
  if (stat.delta < -thresholds.successDelta || stat.hardWorse.length)
    decision = 'block';                          // 核心退化或 hard case 翻转
  else if (Math.abs(stat.delta) < 0.01)
    decision = 'gray';                           // 临界 → 灰度观察
  if (stat.costDelta > thresholds.costDelta)
    decision = decision === 'pass' ? 'gray' : decision;  // 成本告警
  return { decision, stat, worseList: stat.worse.slice(0, 10) };
}
```

**评分点**:
- 双版本同环境并行跑（mock 固定），对比公平。
- 逐任务四态分级（含 flipped 翻转单列）与 hard case 专项检查（hard case 翻转即阻断）。
- 三档决策（pass/gray/block）阈值清晰，成本超阈值触发降档。
- worseList 输出供人工分析，报告可归因。
