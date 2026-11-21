---
title: [ARC-189] 大规模前端团队的角色分工（Platform / App / Infra）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-189：大规模前端团队的角色分工（Platform / App / Infra）如何设计？
**答**：
- 三类角色职责边界：App 团队（业务交付与领域代码）、Platform（组件库/物料/模板——产出"可复用件"）、Infra（构建/运行时/监控/发布——产出"管线与平台"）；边界口诀：App 写业务，Platform 供砖，Infra 修路。
- 接口契约治理：Platform/Infra 对 App 的承诺写成 SLA（版本支持窗口、issue 响应时限、升级通告流程），避免"基建团队消失在需求里"。
- 人员比例参考：业务:平台:基建 ≈ 70:20:10，比例随阶段浮动（基建空窗期临时上调）；轮岗机制防止基建团队与业务脱节（业务工程师轮岗进 Platform 一个季度）。
- 协调节奏：三边月度对齐会（路线图/升级计划/痛感反馈），业务痛感是 Platform/Infra 排期的最高优先级输入。

```yaml
# 大规模前端团队角色分工契约（组织配置）
org_model:
  app_teams:                            # 业务团队（70%）
    mission: 业务交付与领域沉淀
    owns: [业务代码, 领域组件提案, 线上业务稳定性]
  platform_team:                        # 平台团队（20%）
    mission: 可复用件——组件库/物料/模板/CLI
    owns: [ui 库, 领域组件库, 脚手架, 文档站]
    sla: { issue_first_response: 24h, version_window: N-1 两个月, 升级通告: 提前 30 天 }
  infra_team:                           # 基建团队（10%）
    mission: 管线与平台——构建/CI/CD/监控/发布/性能
    owns: [monorepo 工具链, 流水线, 可观测性平台, 性能预算体系]
    sla: { 流水线可用性: 99.9%, 故障响应: P0 15min }
  governance:
    ratio_guide: "70 / 20 / 10，基建空窗期临时上调"
    rotation: 业务工程师 → Platform 轮岗一个季度（防脱节）
    sync: 三边月度对齐会：路线图 + 升级计划 + 业务痛感清单（最高优先级输入）
    anti_patterns:
      - 基建接业务定制需求（定位漂移）
      - Platform 团队消失（SLA 失效，App 团队自建影子组件库）
```
