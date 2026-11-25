---
title: [ENG-278] 构建即服务（Build as a Service API）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-278：构建即服务怎么设计？
**答**：
- API 面：触发构建（commit/app/branch）→ 异步任务（buildId）→ 状态轮询/回调 → 产物与日志下载——构建是长任务，API 必须「提交-查询」异步模型。
- 幂等与去重：同 commit 重复触发返回已有 buildId（幂等）；排队任务可取消。
- 配额与隔离：按团队配额（并发构建数），租户级资源隔离（一个团队的构建风暴不影响别人）。
- 可观测：API 层暴露构建指标（排队时长/成功率/产物大小），与 ENG-269 遥测打通。
- 追问钩子：为什么构建 API 必须「提交-查询」异步而非同步返回产物——构建分钟级，同步 HTTP 会超时且客户端断线即失败；异步模型（buildId + 回调/轮询）让构建可排队、可重试、可观测，这是所有长任务服务的标准形态。

```typescript
// 构建 API
POST /builds { app, commit } -> { buildId, queuePosition }     // 幂等：同 commit 返回已有
GET /builds/:id -> { status: queued|running|done|failed, artifacts, logs }
DELETE /builds/:id -> 取消
// 配额
if (teamConcurrent(team) >= quota(team)) return 429 { retryAfter };
```
