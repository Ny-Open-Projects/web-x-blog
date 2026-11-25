---
title: [AIC-918] IM 消息模块多个 Agent 同时改状态机（发送中/已送达/已读），如何用「契约先行」减少冲突？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-918：IM 消息模块多个 Agent 同时改状态机（发送中/已送达/已读），如何用「契约先行」减少冲突？
**答**：
- 先把状态机本身抽成「单一权威定义」：一个状态枚举 + 一张合法转换表（如 发送中→已送达 合法、已读→发送中 非法），所有 Agent 面向这份契约编码。
- Agent 不改状态定义本身，只在其负责的「动作/副作用」上扩展；要改状态定义必须走评审，避免各改各的导致转换规则矛盾。
- 用「转换表测试」做集成门禁：合并后跑所有合法/非法转换用例，任何 Agent 的改动破坏了转换规则都会被抓出。
- 追问钩子：能说出「契约先行的本质是把易冲突的共享知识收敛为单一权威源，让并行改动发生在契约之外的独立区域」的候选人，理解了并行开发的架构前提。

```typescript
// 契约：单一权威状态机定义
const TRANSITIONS = {
  sending:['sent','failed'], sent:['read'], read:[], failed:['sending'],
};
function canTransition(from, to) { return (TRANSITIONS[from] || []).includes(to); }
// 集成门禁：转换表测试
const cases = [['sending','sent',true],['sending','read',false],['read','sending',false],['failed','sending',true]];
function verifyContract() {
  return cases.filter(([f,t,expected]) => canTransition(f,t) !== expected);
}
console.log('契约破坏:', verifyContract()); // 空数组=所有 Agent 改动未破坏状态机
```
