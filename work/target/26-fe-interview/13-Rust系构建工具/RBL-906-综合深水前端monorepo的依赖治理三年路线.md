---
title: [RBL-906] 综合深水：Monorepo 依赖治理三年路线——从混乱到受控的四个阶段
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-906：综合深水：依赖治理三年路线——从混乱到受控

**答**:
- 依赖治理四阶段：1) **可见期**（幽灵依赖/双版本审计 RBL-833 + 依赖图报告 RBL-871——先知道现状，门禁只报告不阻断）；2) **止血期**（新增依赖门禁：幽灵阻断 + 双版本警告——防止恶化，存量豁免清单）；3) **清理期**（存量修复：冗余移除 PR 自动化/版本统一计划——按使用面排序）；4) **受控期**（声明完整性 CI 硬门禁 + peer 一致性 + 定期复核——新常态）。每阶段有 exit 条件（RBL-893 路线模式）。
- 依赖治理的特殊难度：依赖是「多人协作的公共品」——升级/清理会破坏别人的工作（semver 区间内的行为变化）——治理动作都要「先通知后执行」（升级日 RBL-821 模式）。
- 版本收敛的策略选择：统一到最新（大爆炸风险）vs 逐包迁移（窗口期长）——「hostage 版本」（被深度依赖的包）最后动；兼容层过渡（同包双版本共存声明化）。
- 度量：幽灵依赖数/双版本对数/平均依赖年龄——趋势向下即治理有效；「依赖年龄」暴露僵尸依赖（3 年没升级 = 安全与兼容双风险）。
- 追问钩子：为什么治理要「先报告后阻断」而不是直接上硬门禁？——直接阻断会把存量问题一次性爆给团队（几百个幽灵依赖的 PR 全红 = 团队对工具失去信任）；可见期让团队理解问题、止血期控制增量（新增少易修）、清理期消化存量——门禁的收紧节奏与「问题存量消化」同步，这与 Ratchet 基线（AIC/工程化通用模式）同构：只收紧不放松，存量给窗口。

```javascript
// 治理阶段门禁
const GOVERNANCE_STAGES = [
  { stage: 'visible', exit: (s) => s.auditReportGenerated && s.baselineRecorded },
  { stage: 'hemostasis', exit: (s) => s.phantomGateActive && s.newPhantoms === 0 },
  { stage: 'cleanup', exit: (s) => s.phantomCount <= s.initialPhantoms * 0.1 },
  { stage: 'controlled', exit: (s) => s.hardGateActive && s.quarterlyReview },
];
// 依赖年龄报告
function dependencyAge(lockfile, { now = Date.now() } = {}) {
  return Object.entries(lockfile).map(([name, meta]) => ({
    name, version: meta.version,
    ageDays: Math.floor((now - new Date(meta.publishedAt)) / 86400000),
    zombie: (now - new Date(meta.publishedAt)) > 365 * 3,
  })).filter(x => x.zombie);
}
```
