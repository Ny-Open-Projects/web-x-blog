---
title: [AIC-954] AI 重构后测试全绿，但线上出现「偶尔多请求一次」的静默行为变化，这类问题怎么抓？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-954：AI 重构后测试全绿，但线上出现「偶尔多请求一次」的静默行为变化，这类问题怎么抓？
**答**：
- 静默变化的特点是「不改变返回值，但改变了副作用/时序/频率」——结论：只测返回值的测试抓不到，必须把副作用也纳入观测。
- 手段：① 对副作用做断言（请求次数、定时器数量、事件监听注册/清理）；② 用录制回放——录制旧实现的副作用序列，重构后回放比对；③ 加监控指标（请求 QPS、错误率）在灰度期观察。
- AI 特别容易在 useEffect 依赖、节流防抖、清理函数上引入静默变化——这些点要列为重构 review 的重点检查项。
- 追问钩子：能指出「测试绿只说明断言覆盖的行为没变，没被断言的行为（尤其副作用）仍是盲区」的候选人，理解测试的覆盖边界。

```typescript
// 副作用录制回放：抓「返回值相同但副作用变了」
function recordEffects(run) {
  const log = [];
  const ctx = { fetch:(url)=>{ log.push('fetch:'+url); }, setTimer:()=>{ log.push('timer'); } };
  run(ctx);
  return log;
}
function compareEffects(oldRun, newRun) {
  const a = recordEffects(oldRun), b = recordEffects(newRun);
  return { equal: JSON.stringify(a)===JSON.stringify(b), old:a, new:b };
}
const oldBehavior = ctx => { ctx.fetch('/list'); };
const newBehavior = ctx => { ctx.fetch('/list'); ctx.fetch('/list'); }; // 静默多请求
console.log(compareEffects(oldBehavior, newBehavior)); // equal=false
```
