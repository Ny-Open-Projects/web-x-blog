---
title: [TST-690] SDK 故障降级测试怎么设计断言？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-690：SDK 故障降级测试怎么设计断言？

**答**：
- 结论：断言分三层——不抛未捕获异常、核心流程可完成、降级提示可见。
- 场景覆盖：SDK 未加载、方法抛错、超时、返回非法值四类。
- 用 idempotencyKey 验证重试不重复执行副作用。
- 追问钩子：降级提示本身也有 bug，你怎么测？

```javascript
function assertDegraded(result, errors) {
  return {
    noUncaught: errors.filter(e => !e.handled).length === 0,
    coreFlowDone: result.orderCreated === true,
    hintVisible: result.degradedHint === true,
    noDoubleCharge: result.chargeCount === 1,
  };
}
const r = assertDegraded(
  { orderCreated: true, degradedHint: true, chargeCount: 1 },
  [{ msg: 'sdk timeout', handled: true }]);
console.log(Object.values(r).every(Boolean)); // true
```
