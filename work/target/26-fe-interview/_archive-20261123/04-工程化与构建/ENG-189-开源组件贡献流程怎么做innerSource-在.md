---
title: [ENG-189] 开源组件贡献流程怎么做？innerSource 在组织内怎么落地？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-189：开源组件贡献流程怎么做？innerSource 在组织内怎么落地？
**答**：
- innerSource 是把开源协作方式用于组织内：公开仓库 issue 驱动 RFC 决策 明确 CODEOWNERS 与贡献指南。
- 前提条件：README 说清是什么怎么用、CONTRIBUTING 写明流程、维护团队承诺响应 SLA，否则贡献者流失。
- 贡献链路：feature 分支 → PR → CODEOWNERS 自动分配 review → CI 门禁 → 合入；跨团队 PR 记录可作晋升材料。
- 收益度量：外部贡献 PR 占比 issue 平均响应时间 被引用仓库数，证明是在共建而非单方面输出。

```ini
# .github/CODEOWNERS —— innerSource 责任与评审路由
# 全局默认 平台组兜底
*                         @corp/platform-team
# 组件库 组件组与设计组必须评审
/packages/ui/             @corp/ui-core @corp/design-guild
# 构建配置变更 需构建负责人
/turbo.json               @corp/build-owners
/.github/workflows/       @corp/ci-owners
# 文档 任何团队可提 文档 owner 审核
/docs/                    @corp/docs-owners
# 业务子应用 自治 review 不阻塞平台组
/apps/mall/               @corp/team-mall
```
