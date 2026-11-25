---
title: [1189] 团队定了 Agent 开发规范，怎么「质检」落地
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 治理]
type: 面试题
---

## 1189：团队定了 Agent 开发规范，怎么「质检」落地

**答**：
- 质检三层：静态检查（CI：规范可机器判的条款——工具白名单、预算声明、降级配置齐全）、动态检查（上线探针：跑规范场景验证行为——如「高危必须走审批」用探针任务验证）、人工抽查（季度抽 2 个 Agent 全项体检，静态动态都覆盖不到的条款靠抽查）。
- 质检结果分级：通过 / 有条件通过（带修复期限）/ 不通过（禁止放量）；结果进团队看板，修复率是规范落地的北极星。
- 规范的死循环防止：每次质检发现的「规范本身不合理」条款收集起来，季度修订——质检不是单向执法，是规范与现实的校准器。
- 追问钩子：质检会不会变成形式主义？——把「机器可判」的比例做高（>70% 条款自动化），人工部分聚焦高风险条款；纯靠人工勾选的规范三个月必然形式化。

```ts
const audit = {
  static: lintRules,                // CI 静态条款
  dynamic: probeScenarios,          // 上线探针
  manual: quarterlyChecklist,       // 人工抽查
};
async function qualityGate(agent) {
  const s = await lintRules.run(agent);
  const d = await probeScenarios.run(agent);
  const verdict = s.ok && d.ok ? 'pass'
    : s.ok || d.ok ? 'conditional' : 'reject';
  board.record(agent, verdict);     // 修复率北极星
  return verdict;
}
```
