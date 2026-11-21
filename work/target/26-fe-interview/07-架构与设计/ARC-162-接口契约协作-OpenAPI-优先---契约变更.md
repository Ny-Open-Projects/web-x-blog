---
title: [ARC-162] 接口契约协作（OpenAPI 优先 / 契约变更流程）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-162：接口契约协作（OpenAPI 优先 / 契约变更流程）如何设计？
**答**：
- OpenAPI 先行：接口定义（不是实现）是协作起点——后端先提交 schema PR，前端基于 schema 生成类型与 mock 同步开发；契约仓库是前后端的"共同上游"。
- 变更流程分级：新增可选字段（自由）、新增必填/删字段/改类型（breaking）→ 必须发新版本路径（/v2/）或走弃用流程，契约 CI 自动检测 diff 是否 breaking。
- 联调成本归零：契约即 mock（schema 直接生成 mock server），前端不等后端；后端实现完成后用契约做一致性验证。
- 责任闭环：契约与实现不一致视为后端 bug（验证失败阻断后端发布）；前端发现文档外的字段行为，反哺修契约而不是前端"默默适配"。

```yaml
# 接口契约协作流程（契约仓 + CI）
contract_workflow:
  source_of_truth: contracts/openapi/mall.yaml     # 契约仓库，单一代码源
  flow:
    - step: 需求评审后，后端提契约 PR（schema 变更）
      check: [spectral lint, breaking-change-diff vs main]
    - step: breaking 变更 → 需要新版本路径或 deprecation 计划（字段级 sunset 日期）
      approval: 前端 owner + 后端 owner 双审
    - step: 契约合入 → 自动产物
      artifacts:
        - 前端类型：openapi-typescript → packages/api-types（版本锁定）
        - mock server：基于 schema 自动部署（前端并行开发）
    - step: 后端实现 → CI 用契约验证（schemathesis），不一致阻断发布
  rules:
    - "前端禁止适配契约外的字段行为：发现偏差提契约 PR 修正（单一真源）"
    - "字段 sunset：deprecated 字段必须带移除日期，超期 CI 告警"
  benefits:
    - 联调时间趋近于 0（mock 与类型自动化）
    - 破坏性变更在 PR 阶段可见，而非联调阶段
```
