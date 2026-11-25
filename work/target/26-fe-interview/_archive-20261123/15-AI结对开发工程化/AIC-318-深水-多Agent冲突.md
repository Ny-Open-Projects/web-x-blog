---
title: [AIC-318] 两个 Agent 同时改同一模块产出冲突，除了文件锁还有什么更聪明的策略？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-318：两个 Agent 同时改同一模块产出冲突，除了文件锁还有什么更聪明的策略？
**答**：
- 接口先行：先由一个 Agent 定义模块接口（类型/签名），其他 Agent 面向接口实现，天然无冲突。
- 语义分区：按职责切分而非按文件切分（一个管逻辑一个管样式），减少同文件碰撞。
- 合并仲裁：冲突时让 AI 基于两个意图描述做三方合并建议，人最终裁决。
- 预算约束：每个 Agent 只允许触碰清单内文件，越界自动拒绝。

```javascript
const coordStrategies = {
  interfaceFirst: 'Agent A 定义 types.ts → B/C 实现，零冲突',
  budget: 'agent B allowlist: [price/*.ts]，越界拒绝',
  merge: '冲突 → AI 三方合并建议（基于双方意图）→ 人裁决',
};
r
```
