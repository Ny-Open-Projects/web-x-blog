---
title: [947] 多 Agent 系统上线前怎么做故障演练
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 混沌工程]
type: 面试题
---

## 947：多 Agent 系统上线前怎么做故障演练

**答**：
- 演练场景清单：某子 Agent 超时、某工具限流、模型 API 5xx、消息总线丢消息、黑板写冲突、审批人一直不批——每个场景预写「预期行为」（降级路径、告警、恢复时长）。
- 演练重点不是「挂了会不会发现」（监控能发现），而是「恢复路径是否符合设计」：降级链是否按预期走、预算是否正确回收、卡住的锁是否释放。
- 混沌注入在预发环境 + 影子流量跑，生产只做低风险注入（如单次工具延迟 500ms）。
- 追问钩子：演练发现的「预期外行为」怎么处理？——全部转成回归测试条目，下次演练验证修复，形成闭环。

```ts
const drills = [
  { name: 'worker_timeout', inject: () => stub(workers.coder, { delayMs: 60000 }),
    expect: t => t.events.includes('degraded:coder') && t.final.completed },
  { name: 'llm_5xx', inject: () => stub(llm, { failRate: 1, times: 3 }),
    expect: t => t.retries === 3 && t.final.completed },   // 重试后恢复
];
for (const d of drills) {
  const t = await runShadowTask(sampleTask());
  assert(d.expect(t), d.name);
}
```

