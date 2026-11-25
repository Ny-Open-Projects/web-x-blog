---
title: [AIC-995] 大促封版前还剩一些遗留迁移没收尾，哪些部分应该坚决不让 AI 碰？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-995：大促封版前还剩一些遗留迁移没收尾，哪些部分应该坚决不让 AI 碰？
**答**：
- 原则：封版期「不新增不确定性」——结论：涉及资金/库存/消息可靠性等核心链路的迁移，和大范围结构改动，坚决不动，留到大促后。
- 具体红线：① 核心交易/价格逻辑的重写；② 涉及并发/时序的遗留行为（消息顺序、幂等）；③ 无法用自动化测试验证等效的改动——验证不了就不改。
- 可做的「安全区」：文档补全、测试补齐、类型标注、死代码标记（不删除）——这些不改变运行时行为，可低风险推进。
- 追问钩子：能说出「判断『能不能碰』的标准是『出问题能否快速发现并回滚』——封版期风险容忍度极低，宁可慢也不要赌」的候选人懂封版纪律。

```typescript
// 封版期迁移红线判定
function canTouchInFreeze(task) {
  if (task.coreChain && task.rewrites) return { ok:false, why:'核心链路重写' };
  if (task.hasConcurrency && !task.verifiable) return { ok:false, why:'时序行为无法验证' };
  if (!task.verifiable) return { ok:false, why:'缺乏等效验证手段' };
  return { ok:true, why:'可验证的非核心改动' };
}
// 安全区：不改变运行时行为的改动可在封版期低风险推进
const safeZone = {
  allowed: ['补全文档','补齐测试','加类型标注','标记死代码(不删除)'],
  reason: '均不改变运行时行为，出问题易回退',
};
function screenTasks(tasks) {
  return tasks.map(t => ({ ...t, ...canTouchInFreeze(t) }));
}
console.log(screenTasks([
  { coreChain:true, rewrites:true, verifiable:false },
  { coreChain:false, rewrites:false, verifiable:true },
])); // 第一项拦截，第二项放行
console.log('安全区:', safeZone.allowed.join('、'));
```
