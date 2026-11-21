---
title: [OPS-100] 发布节奏与 trunk-based 怎么配合？变更审计与自动化程度怎么评估？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-100：发布节奏与 trunk-based 怎么配合？变更审计与自动化程度怎么评估？
**答**：
- trunk-based（主干开发）+ 短生命周期分支是高频发布的前提：代码合主干即走流水线到生产，未完成功能用 Feature Flag 隐藏而非长期分支。
- 发布节奏按风险分级：常规改动每日发布、中风险每周窗口、高风险灰度观察期拉长；错误预算耗尽则冻结（OPS-067）。
- 变更审计：所有变更（发布/配置/开关）统一记录，支持"上周三都改了什么"的一键查询，这是事故排查与合规的双重要求。
- 自动化评估：列出从 commit 到生产的每个手动步骤，按"耗时×频率×出错率"排序逐个自动化；指标看 DORA（部署频率、变更前置时间、变更失败率、恢复时长）。

```yaml
# release-cadence.yaml：发布节奏 + 变更审计 + 自动化评估（团队工程规范）
trunk_based:
  branch_lifetime: <2 天        # 分支生命周期上限
  merge_to_main_requires: [ci_green, 1_review, feature_flag_declared]
  incomplete_features: feature_flag_hidden   # 未完成功能用开关隐藏在主干
release_cadence:
  routine: daily_1630           # 常规改动：每日 16:30 窗口
  medium_risk: weekly_tue       # 中风险：每周二窗口
  high_risk: canary_48h         # 高风险：灰度观察 48h 再放量
  freeze: [大促封网期, 春节保障期]
  guard: error_budget < 25% 时仅允许修复类发布
change_audit:
  sources:                      # 审计统一接入的变更源
    - deploy_system             # 发布
    - config_center             # 配置
    - feature_flags             # 开关
    - dns_provider              # DNS/域名
  query: "谁在何时对哪个环境改了什么，支持按时间窗导出"
  retention: 365d
automation_assessment:          # 手动步骤清点与自动化路线
  manual_steps:
    - { step: 发布前通知值班群, freq: daily, cost: 5m, automate: phase2 }
    - { step: CDN 刷新执行,    freq: daily, cost: 3m, automate: phase1 }
    - { step: 生产审批,        freq: daily, cost: 10m, automate: keep_human }  # 保留人工
    - { step: 回滚决策,        freq: rare,  cost: -,    automate: 辅助建议+人工确认 }
  dora_baseline:
    deploy_frequency: 每日 3-5 次
    lead_time: commit->prod < 4h
    change_fail_rate: < 15%
    mttr: < 30m
```

---

## 十一、Nginx 高阶（OPS-101 ~ OPS-110）

基础篇（第四章）解决"配起来"，本章解决"扛得住、跑得快、查得清"：性能调优、限流调参、多 SPA 路由、灰度切换、日志分析与 502/504 的系统化排查。
