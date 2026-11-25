---
title: [TST-670] 笔试：实现 AI 数据生成器的合规闸门
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-670：笔试：实现 AI 数据生成器的合规闸门

**题目**：实现 complianceGate(rows,opts)。检查：forbidden 敏感字段（allow 可豁免）、ranges 值域、dist 分布 P50 漂移超 drift。返回 {pass, issues:[{row,why}]}。

**答**：
- 三类检查：敏感字段存在性、值域合法性、分布漂移（P50 偏差 >20%）。
- 任一检查失败即拦截，返回具体原因。
- 支持白名单字段豁免（明确授权的合成字段）。

```javascript
function complianceGate(rows, { forbidden = [], ranges = {}, dist = {},
    allow = [], drift = 0.2 } = {}) {
  const issues = [];
  rows.forEach((r, i) => {
    Object.keys(r).forEach(k => {
      if (forbidden.includes(k) && !allow.includes(k))
        issues.push({ row: i, why: `敏感字段 ${k}` });
      const rg = ranges[k];
      if (rg && (r[k] < rg[0] || r[k] > rg[1]))
        issues.push({ row: i, why: `${k} 越界` });
    });
  });
  Object.entries(dist).forEach(([k, want]) => {
    const vals = rows.map(r => r[k]).filter(v => typeof v === 'number')
      .sort((a, b) => a - b);
    const p50 = vals[Math.floor(vals.length * 0.5)] || 0;
    if (Math.abs(p50 - want) / want > drift)
      issues.push({ row: 'all', why: `${k} 分布漂移` });
  });
  return { pass: issues.length === 0, issues };
}
```

**评分点**：
- 三类检查全部实现
- P50 漂移计算正确
- 白名单豁免生效
- 失败原因定位到行
