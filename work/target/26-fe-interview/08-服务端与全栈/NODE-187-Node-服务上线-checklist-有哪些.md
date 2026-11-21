---
title: [NODE-187] Node 服务上线 checklist 有哪些？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-187：Node 服务上线 checklist 有哪些？
**答**：
- checklist 的价值：把事故复盘沉淀成发布前强制项；做成 CI/发布流水线的自动检查 + 人工勾选双轨。
- 五个域：**代码与契约**（测试/迁移可回滚/接口文档）、**运行时**（配置校验/密钥管理/优雅退出）、**稳定性**（压测/熔断演练/灰度方案）、**可观测**（指标告警/runbook/回滚预案）、**容量**（连接池与限流参数对齐预案）。
- 每项都要"可验证"：写"已测试"无效，要贴证据（压测报告链接、演练记录）。
- 与 NODE-099 容量预案、NODE-139 告警分级配套使用。

```yaml
# release-checklist.yaml —— 发布流水线强制检查项
release:
  - typecheck 与 lint 与测试通过
  - DB 迁移已 review 且有 down 迁移
  - 新接口有 OpenAPI 契约（NODE-157）
runtime:
  - 环境变量经 zod 校验（NODE-155），密钥来自 secret 管理
  - traceId 全链路贯通（NODE-133），错误告警带 runbook 链接
  - 优雅退出与 preStop 已验证（NODE-060/184）
  - 连接池与 agent 参数对齐容量预案（NODE-116/121）
stability:
  - 压测达到目标 QPS 的 1.5 倍（NODE-140）
  - 限流/熔断/降级开关演练过（NODE-143）
  - 灰度方案确认：按 uid 比例发布，观察 30 分钟（NODE-176）
observability:
  - RED 指标与告警已配置（NODE-135/139）
  - 回滚预案三件套：镜像 tag / 迁移回滚 / 配置回滚（NODE-177）
```
