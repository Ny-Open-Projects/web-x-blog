---
title: [TST-475] 笔试：验收标准 → 用例追溯矩阵生成。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-475：笔试：验收标准 → 用例追溯矩阵生成。
**题目**：AC 列表与用例 `[{name, acs: ['AC-1']}]`。输出矩阵：每 AC 关联用例与最新状态；未覆盖 AC 标记 manual-required；无 AC 的用例标 orphan（冗余嫌疑）。

```javascript
function traceMatrix(acs, cases, statusMap) {
  const byAc = new Map(acs.map(a => [a.id, []]));
  for (const c of cases) {
    if (!c.acs?.length) c.orphan = true;
    for (const ac of c.acs || []) {
      if (!byAc.has(ac)) byAc.set(ac, []);
      byAc.get(ac).push(c.name);
    }
  }
  return [...byAc].sort((a, b) => a[0].localeCompare(b[0]))
    .map(([id, cs]) => ({ ac: id, cases: cs,
      status: cs.length ? (cs.every(c => statusMap[c] === 'pass') ? 'green' : 'red') : 'manual-required' }));
}

```

**评分点**：
- 正向（AC→用例）与反向（用例→AC）双向校验。
- 未覆盖 AC → manual-required（显式缺口）。
- orphan 用例标记（防测试漂移）。
- 矩阵按 AC 编号排序。
