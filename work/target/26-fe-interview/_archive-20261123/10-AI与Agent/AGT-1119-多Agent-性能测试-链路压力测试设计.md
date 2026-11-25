---
title: [1119] 多 Agent 链路的压力测试怎么设计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 压测]
type: 面试题
---

## 1119：多 Agent 链路的压力测试怎么设计

**答**：
- 压测目标三个：容量上限（多少并发任务开始排队/降级）、瓶颈定位（模型配额/工具并发/编排器 CPU 谁先到顶）、稳定性（长时间压力下无泄漏死锁）。
- Agent 压测特殊性：任务时长大（分钟级）、成本高（压测烧真金白银）——用录制回放模式压测（模型响应回放，只压真实瓶颈组件），全真压测只在上线前做小规模。
- 阶梯加压 + 拐点记录：并发 10/20/40/80 逐级，记录每级 P95、失败率、降级触发数；拐点即容量红线，告警阈值设在 70% 拐点。
- 追问钩子：回放压测能发现什么、发现不了什么？——能发现编排器/工具/存储瓶颈，发现不了模型 API 的真实限流行为（回放绕过了），所以配额相关的结论必须全真小规模验证。

```ts
const plan = [10, 20, 40, 80].map(c => ({ concurrency: c, duration: '5m' }));
for (const s of plan) {
  const r = await load({ ...s, mode: 'replay' });      // 回放压测
  record({ ...s, p95: r.p95, fail: r.failRate, degraded: r.degrades });
  if (r.failRate > 0.01) break;                        // 到拐点停止
}
setAlarm({ threshold: CAPACITY * 0.7 });               // 告警设在 70% 拐点
```

