---
title: [ENG-302] 笔试题——实现 flaky 检测与隔离流水线（N 次复跑 + 隔离 SLA）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-302：手写 flaky 流水线

**需求与边界**：
- 需求：失败测试自动复跑 N 次 → 判定 flaky（通过率 0<r<1）→ 进隔离区（skip 不阻塞门禁）→ 隔离 SLA（14 天）到期强制「修或删」；复跑结果标记不报绿。
- 边界：① 复跑成本控制（只复跑失败用例，非整个 suite）；② flaky 记录历史（复现率趋势：复现率上升优先修）；③ 隔离区看板可见（不静默吞掉）。

**答**：
```javascript
async function flakyPipeline(test, { runs = 5, slaDays = 14 } = {}) {
  const results = [];
  for (let i = 0; i < runs; i++)
    results.push(await runCase(test));                 // 只复跑失败用例
  const passRate = results.filter(Boolean).length / runs;
  const verdict = passRate === 1 ? 'PASS(FLAKY_FIXED)' : passRate === 0 ? 'FAIL' : 'FLAKY';
  if (verdict === 'FLAKY') {
    quarantine.add({ test, passRate, addedAt: Date.now(),
      history: [...(quarantine.get(test)?.history ?? []), passRate] });   // 复现率趋势
    report({ type: 'QUARANTINED', test, passRate, note: '不报绿，看板可见' });
  }
  return { verdict, passRate };
}
setInterval(() => {                                    // 隔离 SLA 到期强制收敛
  for (const item of quarantine.all())
    if (Date.now() - item.addedAt > slaDays * 864e5)
      requireAction(item, ['fix', 'delete']);          // 两选一，不接受继续隔离
}, 864e5);
```

**评分点**:
- 只复跑失败用例（复跑成本控制）。
- 三态判定（FLAKY/PASS_FIXED/FAIL）且 flaky 不报绿。
- 复现率历史趋势（上升优先修——ENG-218 联动）。
- 隔离 SLA 到期强制「修或删」。
