---
title: [AIC-920] 两个 Agent 对同一函数给出不同实现，冲突合并时如何「保留双方意图」而不是机械逐行取舍？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-920：两个 Agent 对同一函数给出不同实现，冲突合并时如何「保留双方意图」而不是机械逐行取舍？
**答**：
- 机械按行合并会丢失「为什么这么写」——结论：合并前先让各方产出「意图摘要」（这段改动想解决什么、约束是什么），基于意图做决策。
- 用「语义块」而非「行」作为合并单位：一个改动块（如参数校验逻辑）整体保留或整体替换，避免把两段逻辑切碎拼出四不像。
- 当两个意图都成立时，寻找「超集实现」——如 A 处理了空值、B 处理了越界，合并后应两者都覆盖，而非二选一；用合并后的测试集验证两条意图都满足。
- 追问钩子：能说出「合并的胜负应由需求与测试判定，而非谁后提交；无法自动裁决时升级到人或契约」的候选人，避免了合并中的独断。

```typescript
// 基于意图的合并：收集各方案覆盖的用例，取并集验证
const cases = [{n:'空值',ok:f=>f(null)===0},{n:'越界',ok:f=>f(1e9)<=100}];
const implA = v => (v ?? 0);           // 意图：处理空值
const implB = v => Math.min(100, v);   // 意图：处理越界
function intentCoverage(impls) {
  return cases.map(c => ({
    name:c.n,
    coveredBy: impls.filter(i => c.ok(i.fn)).map(i => i.name),
  }));
}
const merged = v => Math.min(100, v ?? 0); // 超集：两个意图都满足
console.log(intentCoverage([{name:'A',fn:implA},{name:'B',fn:implB}]));
console.log(cases.every(c => c.ok(merged))); // true=合并保留双方意图
```
