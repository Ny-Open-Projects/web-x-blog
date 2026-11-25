---
title: [ENG-206] monorepo 的代码所有权（CODEOWNERS 进阶）怎么治理？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-206：代码所有权怎么治理？
**答**：
- 三层所有权：CODEOWNERS（文件级审批权）+ 包级 owner 字段（package.json 维护者）+ 系统级架构 owner（分层规则守护者）——审批权、发布权、架构权分离。
- 所有权健康度：owner 响应时长/审批积压/单人 owner 风险（bus factor=1 标红）——所有权不是写在文件里就完事，要有运营指标。
- 所有权转移流程：交接文档 + 双人并行审批期（新旧 owner 都批）+ 权限回收，防止「离职后 PR 无人批」。
- 紧急路径：owner 不在线时的应急审批人列表与事后复审要求。
- 追问钩子：为什么审批权与发布权要分离——审批人对代码质量负责，发布人对「何时上线」负责；混在一起会出现「审批人被迫连夜发版」或「发布人不审代码」的错位。

```yaml
# .github/CODEOWNERS —— 文件级
/packages/ui/          @org/ui-team
/packages/core/        @org/arch-team
# package.json 包级
{ "name": "@org/ui", "owner": "ui-team", "reviewers": 2 }
# 健康度看板
const ownershipHealth = (pkg) => ({
  busFactor: ownersOf(pkg).length,
  responseP95: metrics.prResponseP95(pkg),
  red: ownersOf(pkg).length === 1,
});
```
