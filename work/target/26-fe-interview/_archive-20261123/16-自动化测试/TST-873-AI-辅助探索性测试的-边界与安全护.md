---
title: [TST-873] AI 辅助探索性测试的「边界与安全护栏」如何设计？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-873：AI 辅助探索性测试的「边界与安全护栏」如何设计？
**答**：
- 结论：AI 探索性测试要设「护栏」——限定操作范围（测试环境）、禁止破坏性动作（删库/真实支付）、预算上限（步数/token）、可随时人工接管。
- 范围护栏：只在隔离测试环境运行，白名单域名，禁止访问生产数据。
- 动作护栏：拦截危险操作（POST 删除、真实支付），用 mock 替代；读操作可放宽。
- 预算护栏：限制最大步数、时长、token 消耗，防止 Agent 陷入死循环烧钱。
- 追问钩子：AI Agent 在探索中「意外」发现一个真实生产 bug，护栏如何既限制风险又不掩盖有价值的发现？

```javascript
// AI 探索 Agent 的护栏中间件
function guardAction(action, guards) {
  if (!guards.allowedDomains.includes(action.domain))
    return { allowed: false, reason: '域名不在白名单' };
  if (guards.dangerousMethods.includes(action.method) && !action.mocked)
    return { allowed: false, reason: '危险操作必须 mock' };
  if (guards.stepsUsed >= guards.maxSteps)
    return { allowed: false, reason: '步数预算耗尽' };
  return { allowed: true };
}
const guards = { allowedDomains: ['test.example'], dangerousMethods: ['DELETE','PAY'],
  stepsUsed: 10, maxSteps: 50 };
console.log(guardAction({ domain: 'prod.example', method: 'GET' }, guards));
console.log(guardAction({ domain: 'test.example', method: 'DELETE', mocked: false }, guards));
```
