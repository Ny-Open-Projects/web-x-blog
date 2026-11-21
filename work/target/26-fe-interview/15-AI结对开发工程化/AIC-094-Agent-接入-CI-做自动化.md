---
title: [AIC-094] 「自动修 bug 的 Agent 机器人」接入 CI 要解决哪些问题？为什么多数团队做不好它？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-094：「自动修 bug 的 Agent 机器人」接入 CI 要解决哪些问题？为什么多数团队做不好它？
**答**:
- 要解决的问题：① 触发边界——哪些失败允许自动修（lint/类型错可修，业务逻辑红测试要人看）② 基线可信——测试本身 flaky 时 agent 会「修」不存在的 bug ③ 权限收敛——CI 机器人只能写代码不能改 CI 配置/依赖版本 ④ 产出通道——修复走 PR 而非直接 push，标签 ai-fix 便于统计与回滚。
- 多数团队做不好的根因：基线不干净（flaky 测试污染）+ 缺乏触发边界（什么都修）→ 产出大量似是而非的修复 PR → 工程师烦 → 下线。先治理测试稳定性，才有自动修复的资格。
- 成功形态：限定「机械性失败」——类型报错、lint、快照更新、明确的空指针——成功率 60%+ 且风险低；业务 bug 修复保持人主导。
- 度量：ai-fix PR 的合并率、二次修复率（修完又坏）是核心指标。
- 追问钩子：回答的亮点是「自动化范围=确定性范围」，能主动收缩范围的是工程成熟度。

```javascript
// 自动修复机器人的触发分类器
function classifyFailure(ciLog) {
  const mechanical = [/TS\d{4}/, /ESLint/, /Snapshot .* mismatch/, /TypeError: Cannot read/];
  if (mechanical.some(r => r.test(ciLog))) return { autoFix: true, channel: 'pr:ai-fix' };
  if (/flaky/.test(ciLog)) return { autoFix: false, action: 'retry_once_then_report' };
  return { autoFix: false, action: 'report_to_owner' }; // 业务失败不自动修
}
```
