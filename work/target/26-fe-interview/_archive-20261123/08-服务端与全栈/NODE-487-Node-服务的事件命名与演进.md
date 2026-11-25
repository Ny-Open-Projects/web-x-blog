---
title: [NODE-487] Node 服务的事件命名与演进（事件契约）如何治理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-487：事件契约治理
**答**:
- 事件是长期契约：发布者改事件结构 → 所有消费者悄悄炸（比 API 更隐蔽——消费者可能很多且无调用关系可见性）。治理：事件注册表 + 契约版本化 + 兼容规则。
- 命名规范：域.实体.动作（order.paid / stock.deducted）——过去时（事件是已发生的事实）；事件 ID/时间/版本/trace 必带（信封协议）。
- 演进规则：只加不改删（同版本内）、破坏性变更 = 新版本事件（order.paid.v2）+ 双写过渡（新旧事件并存直到消费者迁移）+ 消费者迁移监控（按 consumer group 的版本使用统计 NODE-440 sunset 思想）。
- 消费者治理：注册消费关系（谁消费什么事件——依赖图可见 NODE-427 事件版）、消费者幂等强制（at-least-once NODE-381）、消费者 lag 独立监控（某消费者拖慢全体 → 按消费者独立队列/重试）。
- 工具：事件 schema 校验（生产/消费两端按注册表校验——坏事件在发布端拦截）、事件文档自动生成。
```yaml
# 事件注册表
events:
  order.paid:
    v1: { schema: paid.v1.avsc, producers: [order-svc], consumers: [points-svc, notify-svc] }
    v2: { schema: paid.v2.avsc, since: 2026-11-01, producers: [order-svc],
          consumers: [points-svc@v2] }        # 消费者按 group 标注版本
rules: { add-only-per-version: true, sunset-old-when: "consumers.migrated == 100%" }
```
