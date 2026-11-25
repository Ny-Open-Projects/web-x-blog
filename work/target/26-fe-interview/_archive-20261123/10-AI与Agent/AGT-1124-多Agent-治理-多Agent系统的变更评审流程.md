---
title: [1124] 多 Agent 系统的变更（prompt/工具/拓扑）怎么评审
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 治理]
type: 面试题
---

## 1124：多 Agent 系统的变更（prompt/工具/拓扑）怎么评审

**答**：
- 变更分级：prompt 微调（轻评审：核心集门禁）、工具/权限变更（中评审：安全评审 + 行为 diff）、拓扑变更（重评审：架构评审会 + 混沌演练）——分级让轻变更不阻塞、重变更不裸奔。
- 变更说明强制字段：动机、影响面、评估数据、回滚方案；缺回滚方案的变更不进评审。
- 变更日历：重大变更错峰（避开大促/版本发布周），同一时间只允许一个拓扑级变更（多变更并发无法归因）。
- 追问钩子：评审怎么防止变成走过场？——评审结论必须落在「可验证的验收条件」，评审会后自动建验证任务；连续两次评审无验收条件的变更人要被约谈。

```ts
const changeTypes = {
  prompt_tweak: { review: 'light', gate: 'core_set' },
  tool_or_perm: { review: 'security', extra: ['behavior_diff'] },
  topology: { review: 'arch_meeting', extra: ['chaos_drill'], calendar: true },
};
function submitChange(c) {
  require(c.motivation && c.impact && c.evals && c.rollback, '变更说明不全');
  return queue(type(c), c);   // 分级入评审
}
```

