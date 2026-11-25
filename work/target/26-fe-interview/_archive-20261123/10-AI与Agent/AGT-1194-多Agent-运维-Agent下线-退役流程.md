---
title: [1194] 一个 Agent 要下线，退役流程怎么做才不留尾巴
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 治理]
type: 面试题
---

## 1194：一个 Agent 要下线，退役流程怎么做才不留尾巴

**答**：
- 退役四步：引用清查（谁在调用它——注册表调用记录 + 代码 grep，双确认）、替代方案就位（能力由谁承接，评估证明不降级）、流量归零（调用方迁移完成，该 Agent 流量归零并观察两周）、资产处置（prompt/fixture 归档、产物按生命周期清理、注册表标记 retired）。
- 「软下线」缓冲：先拒绝新调用并提示替代方案，保留存量任务跑完——直接硬下会打断在途任务。
- 退役也是资产动作：下线 Agent 的评估集条目标记 deprecated（不删除），「它曾经防住的失败模式」注明承接方，防线不出现真空。
- 追问钩子：退役后突然又有调用怎么办？——注册表层面的「墓碑响应」：明确报错「已退役，替代为 X」而不是 404，调用方能程序化迁移；静默 404 会造成静默故障。

```ts
async function retire(agentId) {
  const callers = await registry.callersOf(agentId);
  require(callers.every(c => c.migrated), '存在未迁移调用方');
  registry.set(agentId, { status: 'tombstone', successor: 'coder-v2' }); // 墓碑
  await drain(agentId, { timeout: '7d' });          // 存量跑完
  await archive(agentId);                            // 资产归档
  evalSet.deprecate(agentId, { coveredBy: 'coder-v2' }); // 防线不真空
}
```

