---
title: [MFW-316] 元框架项目的定时任务编排
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-316：定时任务编排

**答**:
- 三种载体：平台 Cron（Vercel crons/Cloudflare triggers——零运维但粒度受限）、自建调度器（BullMQ repeatable/Redis ZSET——依赖队列基建）、外部调度器（K8s CronJob 触发 Hook——调度与执行分离最稳）
- 与 ISR 协同：定时预热（高频页 keep-warm 防冷首访）与定时失效（数据日切后 revalidateTag）——写进同一编排表审计
- 幂等与并发：多实例 cron 重叠触发（分布式锁 key=task:slot 去抖）+ 失败重试上限 + 执行日志（输入摘要与结果行数——可对账）
- 反模式：在 RSC 模块顶层 setInterval（每次部署 × 实例数重复注册——任务风暴）

```javascript
async function runGuarded(name, fn, { lockTtl = 600_000 } = {}) {
  const got = await redis.set(`cron:${name}:${slotOf(now)}`, 1, 'NX', 'PX', lockTtl)
  if (!got) return { skipped: 'already-running' }
  return runWithLog(name, fn)                                  // 摘要+行数入审计
}
// 红线：禁止模块顶层 setInterval 注册（部署 × 实例 = 任务风暴）
```
