---
title: [MFW-723] 笔试：手写 Saga 补偿链
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-723：笔试：手写 Saga 补偿链

**答**：实现 `executeSaga(steps)`。steps: `{ name, execute: () => Promise<any>, compensate?: (result) => Promise<void> }[]`。规则：1) 顺序执行 steps；2) 步骤 N 失败 → **逆序补偿**已完成的步骤（step N-1 补偿 → N-2 补偿 → ... → step 1 补偿）；3) 补偿失败：记录（不中断其他补偿——尽力补偿）；4) 返回 `{ ok, results, compensated: string[], compensationFailures }`（补偿链的可审计）。边界：steps 空（ok）；首步失败（无补偿——nothing to undo）；补偿本身抛错（记录继续下一个补偿）；无 compensate 的步骤成功后后续失败（跳过该步补偿——无法撤销的操作标注）。

```javascript
async function executeSaga(steps = []) {
  const results = [], completed = [], compensationFailures = [];
  for (let i = 0; i < steps.length; i++) {
    try {
      const result = await steps[i].execute();
      results.push({ step: steps[i].name, result });
      completed.push({ step: steps[i], result });
    } catch (e) {
      // 失败：逆序补偿
      const compensated = [];
      for (const c of completed.reverse()) {
        if (!c.step.compensate) continue;                // 无补偿：跳过
        try { await c.step.compensate(c.result); compensated.push(c.step.name); }
        catch (ce) {
          compensationFailures.push({ step: c.step.name, error: ce.message });
        }
      }
      return { ok: false, results, compensated, compensationFailures,
        failedStep: steps[i].name, error: e.message };
    }
  }
  return { ok: true, results, compensated: [], compensationFailures: [] };
}

// 自测
const log = [];
const steps = [
  { name: 'create-order', execute: async () => { log.push('order'); return { id: 'o1' }; },
    compensate: async () => { log.push('undo-order'); } },
  { name: 'charge-payment', execute: async () => { log.push('payment'); return { pid: 'p1' }; },
    compensate: async () => { log.push('refund'); } },
  { name: 'send-email', execute: async () => { throw new Error('smtp down'); } },   // 失败
];
let r = await executeSaga(steps);
console.log(r.ok === false && r.failedStep === 'send-email');
console.log(r.compensated.join(','));                    // charge-payment,create-order（逆序）
console.log(log.join(','));                              // order,payment,undo-order,refund（逆序补偿）
console.log(r.results.length === 2);                     // 前 2 步成功

// 补偿失败
const badSteps = [
  { name: 'a', execute: async () => 'r1', compensate: async () => { throw new Error('undo fail'); } },
  { name: 'b', execute: async () => { throw new Error('fail'); } },
];
r = await executeSaga(badSteps);
console.log(r.compensationFailures[0].step === 'a' && r.compensated.length === 0);
console.log(r.ok === false);                             // 补偿失败但不中断

// 首步失败（无补偿）
const firstFail = [{ name: 'x', execute: async () => { throw new Error('x'); } }];
r = await executeSaga(firstFail);
console.log(r.compensated.length === 0 && r.ok === false);

// 无 compensate 跳过
const noComp = [
  { name: 'irreversible', execute: async () => 'done' },   // 无补偿
  { name: 'fail', execute: async () => { throw new Error('x'); } },
];
r = await executeSaga(noComp);
console.log(r.compensated.length === 0);                 // 无补偿步骤跳过
console.log(r.ok === false);
```

**评分点**：
- 逆序补偿链正确（后完成的先补偿——栈语义）；补偿失败不中断其他补偿（尽力而为）
- 无 compensate 的步骤跳过（不可撤销操作标注——诚实）；首步失败无补偿
- 边界（空/首败/补偿失败）；补偿链可审计（compensated/failures 清单）
- 能说清「Saga 的补偿 = 正向操作 + 反向补偿的链式执行——跨服务事务的可行解（避免分布式锁）」属于加分
