---
title: [AGT-184] AI 功能的产品指标体系怎么搭（不只看 DAU）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-184：AI 功能的产品指标体系怎么搭（不只看 DAU）？
**答**：
- 三层指标：采用率（多少用户真的用：AI 功能渗透率、周活跃使用人数）、质量（任务完成率、AI 回答采纳率、编辑率——「用户改了多少 AI 输出」是最诚实的质量信号）、留存与价值（AI 使用者的留存差、AI 功能对核心转化的增量，用 A/B 验证因果）。
- 健康信号分层监控：采纳率降 → 质量问题（查评测集与负反馈聚类）；采纳率高但编辑率高 → 「能用但费劲」（体验问题）；渗透率低但试用者留存高 → 发现性问题（入口/引导），而不是质量问题。
- 反指标要盯：AI 关闭率（用户主动关掉 AI 功能）、重复请求率（同一个问题反复问 = 没答对）、人工升级率（客服场景转人工比例）。
- 指标要有「护栏对」：效率指标（响应时长下降）配质量护栏（采纳率不降），防止为快牺牲好。

```typescript
// AI 功能指标看板的数据模型与健康诊断
import { z } from 'zod';

const AiMetrics = z.object({
  dau: z.number(),
  aiWeeklyUsers: z.number(),
  aiSuggestions: z.number(), accepted: z.number(), edited: z.number(),
  repeatQueries: z.number(), aiDisabled: z.number(),
  retentionAiUsers: z.number(), retentionAll: z.number(),
});
type AiMetrics = z.infer<typeof AiMetrics>;

export function diagnose(m: AiMetrics) {
  const adoption = m.aiWeeklyUsers / m.dau;
  const acceptRate = m.accepted / m.aiSuggestions;
  const editRate = m.edited / m.accepted;                 // 采纳后仍被编辑：能用但费劲
  const repeatRate = m.repeatQueries / m.aiSuggestions;
  const retentionLift = m.retentionAiUsers - m.retentionAll;

  const findings: string[] = [];
  if (adoption < 0.2 && retentionLift > 0.05) findings.push('渗透率低但使用者留存高：发现性问题，优化入口与引导');
  if (acceptRate < 0.5) findings.push('采纳率低：质量问题优先，看负反馈聚类与评测集回归');
  if (acceptRate > 0.7 && editRate > 0.4) findings.push('采纳后编辑率高：体验问题，输出粒度/格式需要优化');
  if (repeatRate > 0.15) findings.push('重复请求率高：回答未解决真实问题，检查检索覆盖与追问引导');
  if (m.aiDisabled / m.aiWeeklyUsers > 0.05) findings.push('主动关闭率高：产品价值存疑，考虑默认关闭 + 显式开启');
  return { adoption, acceptRate, editRate, retentionLift, findings };
}
```
