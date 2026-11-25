---
title: [942] 多 Agent 的共享记忆（团队记忆）该怎么设计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 记忆]
type: 面试题
---

## 942：多 Agent 的共享记忆（团队记忆）该怎么设计

**答**：
- 共享记忆三类：事实库（项目约定、接口契约，低频写高频读）、经验库（badcase 解法，检索增强）、任务暂存（黑板，生命周期与任务一致）。
- 写入门槛：Agent 不得随意写共享记忆——经验要经过「验证通过」标记才入库，防止错误经验污染全团队（一个 Agent 的错觉被所有 Agent 引用是灾难）。
- 冲突处理：新旧记忆冲突时按「时间 + 验证等级」裁决，并保留旧条目为 superseded，可回溯。
- 追问钩子：记忆会不会无限膨胀？——按引用频率衰减淘汰，60 天零引用的经验自动归档。

```ts
async function shareMemory(entry, agent) {
  const verified = await validator.check(entry, memoryStore); // 与现有记忆比对
  if (verified.conflict) {
    await memoryStore.supersede(verified.oldId, entry);       // 保留旧条目可回溯
  }
  if (verified.confidence > 0.8) {
    await memoryStore.add({ ...entry, by: agent, validated: true, refs: 0 });
  } else {
    await reviewQueue.push(entry);                            // 低置信走人工
  }
}
```

