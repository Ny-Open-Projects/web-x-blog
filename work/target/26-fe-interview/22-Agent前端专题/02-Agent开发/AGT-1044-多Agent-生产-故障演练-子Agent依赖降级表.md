---
title: [1044] 每个子 Agent 的依赖挂了怎么降级，降级表怎么建
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 降级]
type: 面试题
---

## 1044：每个子 Agent 的依赖挂了怎么降级，降级表怎么建

**答**：
- 降级表结构：依赖（模型 API/工具/存储）× 故障等级（慢/错/断）× 动作（重试/换路/降级实现/熔断任务）；每个 Agent 上线时降级表是验收项，没降级表不允许上线。
- 降级实现要「预写」：挂了再想必然手忙脚乱，降级路径（如「检索 Agent 挂了 → 用缓存快照 + 提示数据可能过期」）是代码不是文档。
- 定期演练验证降级表：混沌注入每个依赖的故障，核对实际行为与降级表一致——不一致就是 bug。
- 追问钩子：降级表的「最后一行」是什么？——「整体拒绝 + 明确告知用户系统维护中」，任何 Agent 链最终要有可用的失败终态，不能无限降级。

```ts
const DEGRADE = {
  'searcher': { slow: 'reduce_topk', down: 'cache_snapshot', // 检索挂了用快照
    note: '提示：数据可能非最新' },
  'coder': { slow: 'smaller_model', down: 'queue_and_retry' },
  'default': { down: 'reject_politely' },                  // 终态：明确告知
};
async function onDepFail(agent, level) {
  const act = DEGRADE[agent.id]?.[level] ?? DEGRADE.default[level];
  return ACTIONS[act](agent);
}
```
