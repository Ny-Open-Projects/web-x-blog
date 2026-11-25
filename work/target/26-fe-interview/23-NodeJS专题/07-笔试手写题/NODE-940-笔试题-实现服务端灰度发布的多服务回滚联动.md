---
title: [NODE-940] 笔试题——实现多服务回滚联动（组合回滚执行）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-940：手写组合回滚

**需求与边界**：
- 需求：组合回滚（SCN-OPS-926/251）——① 组合回滚顺序（逆序——SCN-OPS-251）；② 组合回滚的数据验证（SCN-OPS-832）；③ 组合回滚的审计（SCN-OPS-273）；④ 组合回滚的演练（SCN-OPS-215）。
- 边界：① 逆序的语义（先回滚消费方——SCN-OPS-251）；② 组合回滚的部分失败（SCN-OPS-227）；③ 回滚的验证（SCN-OPS-930）。

**答**：
```javascript
async function comboRollback(plans) {
  const reversed = plans.reverse();                    // 逆序（SCN-OPS-251）
  const results = [];
  for (const p of reversed) {
    results.push(await multidimRollback(p, { reason: 'combo' }));   // SCN-NODE-926
  }
  const failures = results.filter(r => !r.recovered);
  if (failures.length) {
    alert({ type: 'COMBO_ROLLBACK_PARTIAL', failures });   // 部分失败（SCN-OPS-227）
    blockNextRelease(plans[0].app);                    // 阻塞（SCN-OPS-227）
  }
  audit({ combo: plans.map(p => p.app), results });    // 审计（SCN-OPS-273）
  return { results };
}
```

**评分点**:
- 逆序组合回滚（SCN-OPS-251）。
- 多维回滚复用（SCN-NODE-926）。
- 部分失败处理（SCN-OPS-227）。
- 审计（SCN-OPS-273）。
