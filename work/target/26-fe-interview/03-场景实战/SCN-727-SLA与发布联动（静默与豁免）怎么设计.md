---
title: [SCN-727] SLA 与发布联动（发布静默/预算冻结豁免）怎么设计？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-727：SLA 与发布联动怎么设计？
**答**：
- 发布静默窗口：发布开始自动对该服务相关指标静默 15 分钟（burn rate 不告警），看板显示静默标记；静默期间指标照常记录（只是不触发告警），发布结束看对比。
- 发布前后对账：发布自动生成 before/after 指标对比卡（同口径同流量段），劣化自动关联到该发布——「发布质量」量化。
- 预算联动发布：预算剩余 < 25% 时发布需额外审批；烧完时冻结（SCN-722 联动）。
- 回滚触发：发布后指标劣化超阈值（burn rate 快窗）自动提示回滚（人确认），看板一键回滚按钮（有权限者）。
- 追问钩子：静默窗口会不会掩盖发布劣化——不会，静默只停告警不停记录；发布对账卡 + 静默结束后的补发检查（若静默期间已超阈值，解除静默时立即补告警）。

```javascript
async function deployWithGuard(release) {
  await silence.metrics(affectedMetrics(release), { window: 15 * 60_000 });
  const after = await canary.observe(release, { window: 30 * 60_000 });
  const compare = await diffMetrics(release.before, after);
  if (compare.burnRate > 6) {
    await unpublish(release);                        // 自动提示回滚（人确认）
    report({ type: 'DEPLOY_ROLLBACK_SUGGESTED', release, compare });
  }
  await silence.release(affectedMetrics(release));   // 解除静默并补发检查
  return compare;
}
```
