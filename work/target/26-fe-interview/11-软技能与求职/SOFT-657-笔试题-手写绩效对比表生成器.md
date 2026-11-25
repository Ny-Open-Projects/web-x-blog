---
title: [SOFT-657] 手写 genComparison：与基线/同侪口径的对比表、口径标注强制、趋势箭头？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-657：手写 genComparison：与基线/同侪口径的对比表、口径标注强制、趋势箭头

**需求与边界**：
- 实现 genComparison(metrics, baseline)。
- 边界要求：① 每个指标必须带口径标注（scope 字段——缺则拒绝，防口径质疑）；② 表输出：指标/期初/期末/变化箭头（↑↓→）/基线对比；③ 变化方向按语义（某些指标下降是好事——字段 goodWhenDown）；④ 同期基线缺失时标 N/A 不硬造。

**答**：
```javascript
function genComparison(metrics, baseline, { now, then }) {
  const rows = metrics.map(m => {
    if (!m.scope) throw new Error(`${m.name} 缺口径标注`);
    const cur = m.values?.[now], prev = m.values?.[then];
    const goodDown = m.goodWhenDown ?? false;
    let arrow = '→';
    if (cur != null && prev != null) {
      const up = cur > prev;
      arrow = (up === !goodDown && cur !== prev) ? '↑' : '↓';
    }
    const bl = baseline?.[m.name];
    return `| ${m.name}（${m.scope}） | ${prev ?? '-'} | ${cur ?? '-'} | ${arrow} | ${bl ?? 'N/A'} |`;
  });
  return [
    '| 指标（口径） | 期初 | 期末 | 趋势 | 同期基线 |',
    '|---|---|---|---|---|', ...rows,
  ].join('\n');
}
```

**评分点**:
- 口径标注强制（缺 scope 抛错——校准会口径质疑的前置防御）。
- goodWhenDown 语义箭头（故障率下降显示 ↑ 的错误被避免）。
- 基线缺失 N/A 不硬造（诚实性）。

