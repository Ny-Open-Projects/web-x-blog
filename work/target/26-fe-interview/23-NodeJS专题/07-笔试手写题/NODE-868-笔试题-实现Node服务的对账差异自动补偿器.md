---
title: [NODE-868] 笔试题——实现对账差异自动补偿器（可修/人工分流）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-868：手写自动补偿

**需求与边界**：
- 需求：对账差异补偿（SCN-NODE-755/865）——① 差异分类（可自动修/需人工——SCN-OPS-259 边界）；② 自动补偿的幂等（补偿动作幂等键——SCN-NODE-655）；③ 补偿的审计与回滚（补偿失败——SCN-OPS-227）；④ 补偿率监控（自动补偿占比——SCN-NODE-682）。
- 边界：① 补偿的依赖顺序（补偿链——先修 A 再修 B，SCN-NODE-740 DAG）；② 补偿的风险分级（金额大的走人工——SCN-联想-868 金额阈值）；③ 补偿的时效（T+1 内完成——SLA）。

**答**：
```javascript
const COMPENSATORS = {
  MISSING_ORDER: { auto: true, run: (d) => replayOrder(d) },       // 幂等重放（SCN-NODE-655）
  AMOUNT_MISMATCH: { auto: false, run: manualPool },   // 金额差异走人工（SCN-联想-868 阈值）
  STATUS_DIFF: { auto: (d) => d.amount < 100, run: (d) => fixStatus(d) },   // 条件自动
};
async function compensate(diff) {
  const c = COMPENSATORS[d.kind];
  const auto = typeof c.auto === 'function' ? c.auto(d) : c.auto;
  if (!auto) return enqueueManual(d);                  // 人工池（SCN-OPS-259 分流）
  const result = await withIdempotency(`comp:${d.id}`, () => c.run(d));   // 补偿幂等（SCN-NODE-655）
  audit({ kind: d.kind, id: d.id, result });           // 审计
  if (result.blocked) enqueueManual(d);                // 补偿失败 → 人工
  return result;
}
```

**评分点**:
- 差异分类分流（auto 条件声明——SCN-OPS-259 边界）。
- 补偿幂等（idemKey——SCN-NODE-655）。
- 补偿失败 → 人工兜底（显式降级）。
- 审计 + 监控（SCN-OPS-220/682）。
