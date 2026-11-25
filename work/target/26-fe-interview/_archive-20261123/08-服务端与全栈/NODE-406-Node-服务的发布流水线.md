---
title: [NODE-406] Node 服务的发布流水线（从合并到全量）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-406：Node 服务的发布流水线
**答**:
- 流水线阶段：CI 绿灯（测试/构建/镜像签名 NODE-374）→ 制品晋级（镜像 tag 关联 commit 与测试结果，禁止重构建）→ 部署测试环境自动验收（冒烟 + 契约测试）→ 预发（生产同构环境验证）→ 生产金丝雀（NODE-370：1%→5%→25%，自动指标判定 ARC-475）→ 全量。
- 发布与迁移协同：DB 迁移先于代码（向前兼容多步 NODE-335），代码发布后清理步骤下个版本执行——"迁移先行"是流水线的硬规则。
- 自动化判定与人工审批的分工：指标类判定自动化（错误率/延迟）、业务影响类人工（资损风险/合规），审批人预授权值班（紧急修复快速通道）。
- 回滚预案：每个发布自带回滚按钮（回上一镜像 + 迁移 down 不自动执行——数据兼容保证旧代码可跑）；回滚演练季度化。
- 发布记录：每次发布归档（谁/何时/什么变更/指标结果），事故复盘可回溯。
```yaml
# 发布流水线
stages:
  ci:    [test, build, sign-image]
  qa:    [deploy-test, smoke, contract-test]
  pre:   [deploy-staging, api-diff-check]
  prod:
    - approve (runtime-owner)
    - canary: { steps: [1%, 5%, 25%], gate: slo-burn-rate }
    - full-rollout
  post:  [record-release, watch-15m]
# 回滚：rollback-to <prev-tag>（迁移不回滚，向前兼容）
```
