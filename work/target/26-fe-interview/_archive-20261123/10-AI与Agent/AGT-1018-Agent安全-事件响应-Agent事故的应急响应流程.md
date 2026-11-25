---
title: [1018] Agent 引发安全事故（误删/外发）时的应急响应怎么做
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 应急]
type: 面试题
---

## 1018：Agent 引发安全事故（误删/外发）时的应急响应怎么做

**答**：
- 应急四步：止血（暂停该类 Agent + 撤销活跃令牌 + 冻结涉事动作的下游影响）、定界（审计日志按任务聚合，列出副作用清单）、恢复（回滚误操作，能自动回滚的工具要在设计期就留 undo）、复盘（防线补丁 + 回归用例入库）。
- 「暂停开关」必须预置：每个 Agent 类有独立 kill switch（不是全局停摆——其他业务还要跑），一秒内生效。
- 副作用可回滚是设计期义务：外发类工具支持撤回窗口、写类工具支持事务/快照——事故应急的上限由设计期决定。
- 追问钩子：怎么判断影响面？——审计链按「副作用清单」反向扩散：这个 Agent 在窗口期内调了哪些写工具、影响哪些资源，逐个列清单而不是凭印象。

```ts
async function incident(agentId, window) {
  await killSwitch(agentId);                      // 1. 止血：停该类 Agent
  await revokeTokens({ agent: agentId });         // 撤令牌
  const sideEffects = await audit.effects(agentId, window); // 2. 定界
  for (const e of sideEffects.filter(e => e.undoable)) {
    await undo(e);                                // 3. 恢复：按可回滚项逐一撤销
  }
  await postmortem(sideEffects);                  // 4. 复盘 -> 防线 + 回归用例
}
```
