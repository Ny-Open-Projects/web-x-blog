---
title: [RBL-797] 场景题：A/B 测试的产物策略——双包并存与实验收敛的构建管理
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-797：场景题：A/B 测试的产物策略——双包并存与实验收敛的构建管理

**答**:
- 实验的产物形态：同一路由两个版本的 chunk（control/treatment）按分流规则加载——构建管理问题：1) 实验代码的组织（feature flag 编译 vs 运行时分支）；2) 双包体积成本（两个实验版本常驻 = 2×chunk）；3) 实验收敛后的清理（代码合并回单包——「实验债」的清偿）。
- 编译期 vs 运行时的选择：UI 大改（两个完整版本）→ 运行时双 chunk（分流后动态 import）；小改（文案/颜色）→ 运行时 flag（单产物）。判据是「差异的代码比例」：<10% 用 flag（产物共享），大改用双包。
- 双包的构建纪律：实验分支的产物从「主 manifest」分离（实验 manifest 单独管理）；实验 chunk 的 hash 独立（RBL-598——不影响主产物缓存）；实验的共享依赖用同一 vendor（两侧共享闭包，只 diff 实验模块）。
- 收敛管理：实验结束（胜出版本确定）→ 删除败者代码 → 构建器诊断「实验残留」（flag 引用的双分支代码仍存在）——实验债的自动清偿清单是构建器独有贡献。
- 追问钩子：为什么「实验 chunk 与主产物共享 vendor」重要？——两个实验版本如果各自带 vendor，分流用户在版本切换时重下 vendor（缓存 miss）且内存双份；共享闭包让实验只差「实验模块」的字节——A/B 的工程本质是「最小 diff 的两个产物」。

```javascript
// 实验构建管理
const experiments = {
  'exp-checkout-v2': { modules: ['src/checkout/v2/**'], assign: '50%' },
};
function buildWithExperiments(manifest, experiments) {
  for (const [name, exp] of Object.entries(experiments)) {
    manifest.experiments[name] = {
      chunks: glob(exp.modules),                         // 实验 chunk 独立 hash
      sharedWith: 'checkout-v1',                         // 共享闭包标注
      cleanupChecklist: ['v1 代码', '分流 flag', '实验 manifest'],   // 收敛清偿清单
    };
  }
}
// 实验残留诊断
function diagnoseExperimentDebt(code, experiments) {
  const findings = [];
  for (const [name, exp] of Object.entries(experiments)) {
    if (exp.concluded && code.includes(`__exp_${name}`))
      findings.push(`${name} 已结束但 flag/分支代码残留——按清偿清单删除`);
  }
  return findings;
}
```
