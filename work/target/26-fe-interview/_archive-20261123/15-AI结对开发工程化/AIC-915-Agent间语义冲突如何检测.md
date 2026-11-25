---
title: [AIC-915] 两个 Agent 都改了「优惠券叠加规则」但写法不同（语法不冲突、语义冲突），如何检测这种语义冲突？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-915：两个 Agent 都改了「优惠券叠加规则」但写法不同（语法不冲突、语义冲突），如何检测这种语义冲突？
**答**：
- 语义冲突比文本冲突更危险：Git 能合并文本，但两处逻辑各改各的会导致运行结果矛盾——结论：要靠「契约与不变量」而非文本 diff 来发现。
- 手段一：为共享业务规则定义机器可读的「不变量/真值表」，合并后跑决策表测试，输出矛盾即语义冲突。
- 手段二：抽取两处改动的「符号级依赖」——如果它们读写同一状态/同一配置键，就标记为高风险需人工复核。
- 追问钩子：能提出「对每个共享领域概念建立唯一权威源（single source of truth），Agent 只能引用不能各自实现」的候选人，从架构上消灭语义冲突。

```typescript
// 语义冲突检测：真值表一致性 + 共享符号识别
const truth = [ {coupon:'A',discount:0.9,expect:90}, {coupon:'A',discount:1,expect:100} ];
function semanticConflict(impls, truthTable) {
  const results = impls.map(({name,fn}) => ({
    name,
    outputs: truthTable.map(t => fn(t.coupon, t.discount)),
  }));
  const conflict = results.some(r => r.outputs.some((o,i) => o !== truthTable[i].expect))
    || new Set(results.map(r => r.outputs.join(','))).size > 1;
  return { conflict, results };
}
const implA = (c,d) => 100*d;                    // Agent A：先减后折
const implB = (c,d) => Math.min(100, 100*d)+0;   // Agent B：另一种写法
console.log(semanticConflict([{name:'A',fn:implA},{name:'B',fn:implB}], truth));
```
