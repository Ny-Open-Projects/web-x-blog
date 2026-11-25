---
title: [NODE-833] 笔试题——实现发布后自动回滚执行器（哨兵触发 → 回滚）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-833：手写自动回滚

**需求与边界**：
- 需求：自动回滚执行器（SCN-NODE-798/OPS-234）——① 哨兵触发 → 回滚执行（切入口——SCN-OPS-251）；② 回滚前检查（回滚通道可达——SCN-OPS-243）；③ 回滚后善后链（SCN-OPS-227 五步——指标恢复/话术/数据验证/RCA/善后阻塞）；④ 回滚风暴防御（连续回滚次数限制——发布冻结，SCN-OPS-234）。
- 边界：① 自动与人工的边界（自动回滚可配置——误回滚代价评估，SCN-OPS-298）；② 回滚的审计（SCN-OPS-273）；③ 回滚后的发布冻结（同问题修复前的准入——SCN-OPS-227）。

**答**：
```javascript
class AutoRollbackExecutor {
  constructor(release) { this.release = release; this.rollbackCount = 0; }
  async execute(reason) {
    if (this.rollbackCount >= 2) {                     // 回滚风暴防御（SCN-OPS-234）
      await freezeReleases(this.release.app);          // 发布冻结
      return { action: 'FROZEN', note: '连续回滚 ≥2——人工介入' };
    }
    const channel = await verifyRollbackChannel(this.release);   // 回滚通道检查（SCN-OPS-243）
    if (!channel.ok) return { action: 'MANUAL_REQUIRED', note: '回滚通道异常——值班介入' };
    await switchEntry(this.release.prev);              // 切入口（SCN-OPS-251 < 1min）
    audit({ action: 'AUTO_ROLLBACK', reason, release: this.release.id });   // 审计（SCN-OPS-273）
    this.rollbackCount++;
    const recovered = await waitForMetricRecovery(10 * 60_000);   // 指标恢复（SCN-OPS-227 第一步）
    if (!recovered) return { action: 'ROOT_CAUSE_NOT_RELEASE', note: '回滚无效——转常规故障' };
    await postRollbackChain(this.release);             // 善后五步（SCN-OPS-227）
    return { action: 'ROLLED_BACK', recovered };
  }
}
```

**评分点**:
- 回滚通道预检（SCN-OPS-243 独立验证）。
- 回滚风暴防御（连续 ≥2 → 冻结——人工介入）。
- 善后五步联动（SCN-OPS-227 指标恢复/数据验证/善后阻塞）。
- 审计留痕（SCN-OPS-273）。
