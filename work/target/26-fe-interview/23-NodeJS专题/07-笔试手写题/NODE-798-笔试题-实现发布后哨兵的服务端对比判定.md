---
title: [NODE-798] 笔试题——实现服务端发布哨兵（canary vs stable 对比）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-798：手写发布哨兵

**需求与边界**：
- 需求：服务端金丝雀哨兵（SCN-OPS-298/668）——① canary vs stable 指标对比（错误率/延迟/CPU——版本维度，SCN-OPS-231 样本归属）；② 自动判定（hard 指标超阈值——建议回滚/自动，SCN-OPS-298）；③ 指标平滑（滑动窗——SCN-OPS-298）；④ 恢复检测（回滚后指标恢复——SCN-OPS-227 善后）。
- 边界：① 样本量下限（canary 流量小时不判定——SCN-OPS-203）；② 动态基线（SCN-OPS-304）；③ 判定记录（可审计——SCN-OPS-273）。

**答**：
```javascript
function canarySentinel(release, { windowMs = 10 * 60_000, minSamples = 100 } = {}) {
  const smooth = rollingWindow(windowMs);
  return {
    async evaluate() {
      const canary = await metrics.slice({ version: release.version });
      const stable = await metrics.slice({ version: release.stableVersion });
      if (canary.samples < minSamples)
        return { verdict: 'INSUFFICIENT', note: '样本不足——SCN-OPS-203' };   // 小流量不判定
      const verdicts = {
        errorRate: canary.errorRate > stable.errorRate * 1.5 ? 'FAIL' : 'OK',   // 倍数+绝对下限（SCN-OPS-298）
        latencyP99: canary.p99 > stable.p99 * 1.3 ? 'FAIL' : 'OK',
        cpu: canary.cpu > stable.cpu * 1.4 ? 'FAIL' : 'OK',
      };
      const fails = Object.entries(verdicts).filter(([, v]) => v === 'FAIL');
      const smoothed = smooth.average(verdicts);       // 平滑（SCN-OPS-298）
      audit({ release: release.id, verdicts, smoothed });   // 判定记录（SCN-OPS-273）
      if (fails.length) return { action: 'ROLLBACK_SUGGESTED', fails };   // 自动回滚可配置（SCN-OPS-298）
      return { verdicts };
    },
    async onRollbackDone() {                           // 恢复检测（SCN-OPS-227）
      return waitForMetricRecovery(stable, 10 * 60_000);
    },
  };
}
```

**评分点**:
- 版本维度对比（样本侧版本——SCN-OPS-231）。
- 样本量下限 + 倍数判定（SCN-OPS-203/298）。
- 判定记录审计（SCN-OPS-273 计划冻结配套）。
- 回滚后恢复检测（善后闭环——SCN-OPS-227）。
