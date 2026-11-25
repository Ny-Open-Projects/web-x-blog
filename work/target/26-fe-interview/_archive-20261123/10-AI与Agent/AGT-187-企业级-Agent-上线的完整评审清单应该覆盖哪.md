---
title: [AGT-187] 企业级 Agent 上线的完整评审清单应该覆盖哪些维度？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-187：企业级 Agent 上线的完整评审清单应该覆盖哪些维度？
**答**：
- 六大维度约 40 项，这里给结构化精简版：安全（注入测试、权限模型、密钥管理、输出过滤）、法务合规（数据驻留、保留策略、用户协议更新、AI 输出免责声明）、质量（评测集通过率、回归基线、幻觉率抽检）、成本（单任务成本上限、总预算告警、降级链）、性能（TTFT/吞吐 P95、扩容预案）、运营（灰度方案、回滚开关、值班与事故手册、审计完整性）。
- 评审的组织设计：安全与法务不是「签字环节」而是设计输入——上线前 2 周介入；清单评审要留证据（每项有检查人、检查方式、结论）。
- 高频考点：清单不是一次性的——每次模型升级、prompt 大改、新工具接入都触发「增量评审」，只过变化项。

```yaml
# 企业级 Agent 上线评审清单（CI 可执行的精简版）
review_checklist:
  security:
    - id: SEC-01
      item: 提示注入红队用例通过率 100%
      check: run_redteam --suite injection
      blocker: true
    - id: SEC-02
      item: 工具权限最小化评审完成且 RBAC 配置入库
      check: assert_rbac_minimal
      blocker: true
    - id: SEC-03
      item: API Key 零前端暴露，密钥轮换机制已启用
      check: scan_frontend_bundle --secrets
      blocker: true
  legal:
    - id: LEG-01
      item: 数据驻留区域与租户合同一致
      check: assert_data_region
      blocker: true
    - id: LEG-02
      item: 日志保留策略已配置且不超过合同上限
      check: assert_retention_policy
      blocker: true
  quality:
    - id: QUA-01
      item: 核心评测集通过率不低于基线 95%
      check: run_eval --suite core --gate 0.95
      blocker: true
    - id: QUA-02
      item: 幻觉抽检不合格率低于 2%
      check: sample_hallucination --rate 0.02
      blocker: false
  cost_perf:
    - id: COP-01
      item: 单任务成本 P95 低于 $0.50 且预算告警已配置
      check: assert_cost_budget
      blocker: true
    - id: COP-02
      item: TTFT P95 低于 3s，降级链演练通过
      check: run_perf --p95-ttft 3000
      blocker: false
  ops:
    - id: OPS-01
      item: 灰度方案与自动回滚条件已配置
      check: assert_rollout_plan
      blocker: true
    - id: OPS-02
      item: 审计日志覆盖全部工具写操作
      check: assert_audit_coverage
      blocker: true
```
