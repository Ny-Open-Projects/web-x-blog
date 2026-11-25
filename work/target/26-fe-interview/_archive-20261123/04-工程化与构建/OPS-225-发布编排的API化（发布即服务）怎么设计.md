---
title: [OPS-225] 发布即服务（Release as a Service API）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-225：发布即服务怎么设计？
**答**：
- API 面：创建发布计划 → 校验（窗口/依赖/审批）→ 异步执行（releaseId）→ 状态/进度查询 → 回滚/熔断 API——与构建 API 同构（SCN-ENG-278 提交-查询模型）。
- 权限与配额：API 调用方（自动化系统/值班机器人）持专用凭据，按产品线配额；人肉发布与 API 发布同审计同治理。
- Webhook：发布事件（step-failed/rollback-done）推送给订阅方（值班 IM/工单系统）——发布编排成为事件源。
- 幂等：同 planId 重复提交返回已有 releaseId；取消 API 终止排队中的发布。
- 追问钩子：为什么发布要 API 化而不仅是控制台——API 化让发布可被自动化消费（值班机器人自动回滚/灾备系统自动发布 fallback 版本）；控制台只服务人类，API 才让发布工程成为可编程基础设施——这也是「发布演练自动化」的前提。

```typescript
POST /releases { planId } -> { releaseId, checks }        // 幂等
GET /releases/:id -> { stage, progress, currentStep }
POST /releases/:id/rollback { reason }                    // 高危权限
POST /releases/:id/break                                  // 熔断
webhooks: ['step.failed', 'rollback.done'] -> oncall-IM
```
