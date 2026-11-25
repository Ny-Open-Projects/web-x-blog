---
title: [NODE-926] 笔试题——实现灰度回滚执行器（入口+数据+配置+通知）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-926：手写多维回滚

**需求与边界**：
- 需求：多维回滚（SCN-OPS-227/251）——① 入口回滚（SCN-OPS-251 切入口）；② 数据回滚（兼容验证——SCN-OPS-832）；③ 配置回滚（快照——SCN-OPS-228）；④ 通知回滚（依赖方——SCN-OPS-245）；⑤ 全链审计（SCN-OPS-273）。
- 边界：① 多维的顺序（入口→数据→配置→通知——SCN-OPS-227 善后链）；② 回滚的幂等（SCN-NODE-655）；③ 回滚的演练（SCN-OPS-215/860）。

**答**：
```javascript
async function multidimRollback(release, reason) {
  await switchEntry(release.prev);                     // ① 入口（SCN-OPS-251）
  const dataOk = await verifyRollbackData(release.canaryWrites, release.stable);   // ② 数据（SCN-OPS-832）
  await rollbackConfig(release.configSnapshot);        // ③ 配置（SCN-OPS-228）
  await notifyRollback(release.dependents, { reason });   // ④ 通知（SCN-OPS-245）
  const recovered = await waitForMetricRecovery(10 * 60_000);   // ⑤ 指标恢复（SCN-OPS-227）
  audit({ release: release.id, reason, dataOk, recovered });   // 全链审计（SCN-OPS-273）
  if (!recovered) return { action: 'ROOT_CAUSE_NOT_RELEASE' };
  await postRollbackChain(release);                    // 善后五步（SCN-OPS-227）
  return { action: 'ROLLED_BACK', dataOk, recovered };
}
```

**评分点**:
- 四维回滚顺序（入口→数据→配置→通知——SCN-OPS-227）。
- 数据验证阻塞善后（SCN-OPS-832）。
- 指标恢复验证（SCN-OPS-227）。
- 全链审计（SCN-OPS-273）。
