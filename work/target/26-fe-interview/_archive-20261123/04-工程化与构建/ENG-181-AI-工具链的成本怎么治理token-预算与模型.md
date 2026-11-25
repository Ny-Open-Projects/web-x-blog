---
title: [ENG-181] AI 工具链的成本怎么治理？token 预算与模型分层怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-181：AI 工具链的成本怎么治理？token 预算与模型分层怎么做？
**答**：
- 成本可见性先行：按团队/场景/模型打 tag 统计 token 与费用，月报公开；没数据就谈不上治理。
- 模型分层路由：格式转换摘要用小模型，架构评审复杂重构用旗舰模型；同场景小模型先行，失败率超阈值自动升档。
- 预算与限流：按团队设月度预算，超预算降级到小模型并通知 owner；高频重复请求走前缀缓存。
- 增量更新：codebase 索引用增量 embedding 而非全量重建，是最大的成本节省点之一。

```json
// ai-gateway/policy.json —— 模型分层与预算治理
{
  "routing": {
    "default": "corp-llm-mini",
    "escalate_to": "corp-llm-flagship",
    "escalate_when": {
      "failure_rate_1h": ">0.3",
      "task_type": ["arch-review", "complex-refactor"]
    }
  },
  "budgets": {
    "per_team_monthly_usd": { "platform": 2000, "business-a": 800, "business-b": 800 },
    "on_exceed": "downgrade_to_mini_and_notify_owner"
  },
  "cache": { "prompt_prefix_cache": true, "ttl_hours": 24 },
  "reporting": { "granularity": ["team", "scenario", "model"], "report_cron": "0 9 1 * *" }
}
```
