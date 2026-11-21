---
title: [AGT-367] 多 Agent 上下文共享——共享什么、隔离什么？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-367：多 Agent 系统中，上下文在 Agent 间怎么共享与隔离？

**答**:
- 共享白名单：任务目标与全局约束（所有 Agent 必须知道）、已确认事实（共享事实库——避免重复发现与结论冲突）、接口契约（上下游的输入输出 schema）——只共享这三类，其余隔离。
- 隔离原则：各 Agent 的推理过程/中间失败/私有工具结果不共享（噪音传播污染其他 Agent——AGT-228）；每个 Agent 的上下文只含"完成任务所需的最小集合"。
- 共享实现：共享事实库用结构化存储（带来源与时间戳，写入需校验——防止一个 Agent 的幻觉变成全局"事实"，这是多 Agent 幻觉扩散的主通道）+ 订阅通知（事实更新广播）。
- 一致性检查：定期对账（各 Agent 对同一事实的认知是否一致——不一致触发复核），共享事实库的幻觉检测比单 Agent 更重要（扩散效应）。

```javascript
const sharedFacts = {
  write(fact, agent) {
    if (!verify(fact)) return reject(agent);   // 写入校验防扩散
    store({ ...fact, source: agent, ts: now() });
    broadcast({ type: 'FACT_UPDATED', fact }); // 订阅广播
  },
  get(query, agent) {
    return store.search(query, { acl: agent.scope });
  },
};
// 共享三类：目标约束 / 已确认事实 / 契约；
// 推理过程与中间失败一律隔离。
```
