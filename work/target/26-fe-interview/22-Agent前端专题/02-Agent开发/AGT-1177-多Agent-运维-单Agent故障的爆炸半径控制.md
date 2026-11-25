---
title: [1177] 一个子 Agent 出 bug，怎么把爆炸半径控制住
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 可靠性]
type: 面试题
---

## 1177：一个子 Agent 出 bug，怎么把爆炸半径控制住

**答**：
- 爆炸半径三控制：调用面控制（该 Agent 只能被哪些编排路径调用——注册表声明）、数据面控制（它写的产物/记忆按命名空间隔离，坏数据不污染共享区）、行为面控制（异常行为熔断——失败率/幻觉率超阈值自动摘除流量）。
- 「自动摘除」的条件要保守：宁可摘错（降级路径顶上）不可漏摘（坏输出持续产出）；摘除事件必告警，人工复核后恢复。
- 上线前的爆炸半径预演：混沌演练里专门做「单 Agent 输出投毒」场景（让它持续输出错误内容），验证熔断与隔离是否生效。
- 追问钩子：摘除后「坏产物」怎么办？——按命名空间反向清理：该 Agent 在故障窗口内写的产物全部标记待审/回滚，共享区若被污染要沿引用链扩散清理。

```ts
const blastRadius = {
  callers: ['pipeline.doc-review'],                 // 调用面白名单
  ns: `artifacts/${agentId}/`,                      // 数据面命名空间
  breaker: { on: metrics => metrics.failRate > 0.2 || metrics.hallucination > 0.05,
    action: 'drain_to_fallback', alert: 'P1' },     // 行为面熔断
};
async function onPoisonSuspect(agentId, window) {
  await breaker.trip(agentId);
  await quarantine(await artifacts.by(agentId, window));   // 坏产物隔离
  await purgeSharedRefs(agentId, window);                  // 共享区扩散清理
}
```
