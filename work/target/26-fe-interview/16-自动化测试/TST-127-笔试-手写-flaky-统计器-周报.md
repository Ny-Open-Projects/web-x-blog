---
title: [TST-127] 笔试：手写 flaky 统计器（多轮报告聚合 + 榜单输出）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-127：笔试：手写 flaky 统计器（多轮报告聚合 + 榜单输出）
**答**：
- 需求：实现 `flakyReport(reports)`——输入同一套用例在 N 次运行的结果数组（`[{ suite, name, status: 'passed'|'failed'|'skipped' }]` × N 轮），输出 flaky 榜单：定义「不稳定用例」为多次运行中**状态不一致**（有时过有时挂）的用例；按不稳定率排序，输出 topN 与整体 flaky 率。
- 核心：按用例唯一键聚合各轮状态；全 passed 或全 failed 都不算 flaky（全 failed 是稳定坏，另列 broken 名单）；skipped 参与判断但不计入分母？——统一约定：skipped 视为「未跑」，从分母剔除。
- 边界：只有一轮报告时 flaky=0 但要提示样本不足；用例被重命名导致跨轮无法匹配（按 suite+name 键，重命名会分裂统计，注明局限）；并发运行轮数很大时聚合用 Map 即可，无需特殊优化。

```javascript
function flakyReport(reports, { topN = 10 } = {}) {
  // 1) 聚合：key -> 每轮状态序列
  const runs = new Map();
  reports.forEach((round, i) => {
    for (const t of round) {
      const key = `${t.suite} > ${t.name}`;
      if (!runs.has(key)) runs.set(key, []);
      runs.get(key)[i] = t.status;
    }
  });

  const rows = [];
  for (const [key, statuses] of runs) {
    const executed = statuses.filter((s) => s && s !== 'skipped');
    if (!executed.length) continue;
    const passed = executed.filter((s) => s === 'passed').length;
    if (passed === executed.length) continue;              // 稳定通过
    if (passed === 0) { rows.push({ key, type: 'broken', rate: 1 }); continue; } // 稳定失败
    rows.push({ key, type: 'flaky', rate: 1 - passed / executed.length,
      rounds: `${passed}/${executed.length} passed` });
  }

  const flaky = rows.filter((r) => r.type === 'flaky').sort((a, b) => b.rate - a.rate);
  const total = runs.size;
  return {
    overallFlakyRate: flaky.length / total,
    top: flaky.slice(0, topN),
    broken: rows.filter((r) => r.type === 'broken').map((r) => r.key),
    note: reports.length < 3 ? 'sample < 3 rounds, statistics unreliable' : null,
  };
}

// reports = [[{suite:'cart', name:'去结算', status:'passed'}], [...status:'failed'], [...'passed']]
// → { overallFlakyRate: 1, top: [{ key: 'cart > 去结算', rate: 0.5, rounds: '2/3 passed' }], ... }
```

**评分点**：
1. flaky 判定语义正确：状态不一致才算，稳定失败单独归为 broken。
2. skipped/样本不足的边界处理与提示。
3. 排序输出 topN，能直接进治理周报（工程化）。
4. 是否指出「重命名分裂统计」这类统计口径局限。
