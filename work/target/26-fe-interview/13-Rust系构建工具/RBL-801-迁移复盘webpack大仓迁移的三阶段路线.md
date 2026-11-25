---
title: [RBL-801] 迁移复盘：200 仓库 webpack 大仓迁移的三阶段路线图
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-801：迁移复盘：200 仓库 webpack 大仓迁移的三阶段路线图

**答**:
- 三阶段路线：1) **标准化期**（不迁移先统一：所有仓库构建配置收敛到共享 preset——迁移的敌人是「200 份不同配置」；标准化让迁移对象从 200 个变成 3-5 个 preset）；2) **试点期**（选 3 个代表性仓库：最标准的/中等复杂的/最难的——验证规则库与工时预估，产出「迁移手册 v1」）；3) **放量期**（按收益排序批量迁移，每周 N 仓，迁移平台自动执行 + 人工复查——RBL-789 平台化）。
- 标准化期的关键决策：「允许的配置差异白名单」（entry 数量/特殊 alias 可配，其余必须用 preset）——差异面收窄是后续一切自动化的前提；白名单外的配置要走「豁免申请 + 复审」。
- 放量期的节奏控制：每批迁移后 48h 的观察窗（构建失败率看板 RBL-705）再发下一批；回滚能力保持到全量完成——「迁移完成」的定义是全仓观察窗通过，不是最后一个 PR 合并。
- 组织面：迁移不是构建团队单打——每个仓库 owner 参与验证（行为测试他们的业务才知道对不对）；构建团队提供工具与规则，业务团队提供语义判断。
- 追问钩子：为什么「先标准化再迁移」而不是边迁边统一？——迁移工具（翻译器/diff）的规则库只能覆盖有限形态；200 种配置形态让每仓都是「定制迁移」，成本不可预估；标准化是给迁移工具「收敛输入域」——工具的可靠性 = 输入域的可枚举性。

```javascript
// 迁移路线的阶段门禁
const STAGES = {
  standardize: { exit: (repos) =>
      repos.every(r => usesSharedPreset(r) && whitelistOnly(r)),   // 全仓用 preset
    note: '差异白名单外的配置必须豁免申请' },
  pilot: { exit: (pilotRepos) =>
      pilotRepos.every(r => r.semanticDiff.length === 0 &&
        r.buildSpeedup >= 2 && r.ownerSignOff),          // 语义一致 + 提速 2 倍 + owner 确认
    note: '产出迁移手册 v1 与工时校准' },
  rollout: { exit: (repos) =>
      repos.every(r => r.stage === 4 && r.observationWindowDays >= 2),   // 全量 + 观察窗
    note: '每周 N 仓节奏 + 48h 观察窗' },
};
function stageGate(stage, data) {
  const ok = STAGES[stage].exit(data);
  if (!ok) fail(`阶段 ${stage} 门禁未过——禁止进入下一阶段`);
  return ok;
}
```
